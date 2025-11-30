"""
Ingestion service for processing book content and storing in Qdrant.
"""
import os
import uuid
import logging
from pathlib import Path
from typing import List, Dict, Any
import tiktoken

from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from src.config import config
from src.models.chunk import TextChunk

logger = logging.getLogger(__name__)

# Initialize OpenAI client
openai_client = OpenAI(api_key=config.OPENAI_API_KEY)

# Initialize tiktoken for token counting
encoding = tiktoken.get_encoding("cl100k_base")  # Used by text-embedding-3-small


def chunk_text(text: str, chunk_size: int = 250, overlap: int = 50) -> List[str]:
    """
    Split text into semantic chunks with overlap.
    
    Args:
        text: Text to chunk
        chunk_size: Target chunk size in tokens (default: 250)
        overlap: Overlap size in tokens (default: 50)
    
    Returns:
        List of text chunks
    """
    # Tokenize the text
    tokens = encoding.encode(text)
    
    chunks = []
    start = 0
    
    while start < len(tokens):
        # Calculate end position
        end = start + chunk_size
        
        # Extract chunk tokens
        chunk_tokens = tokens[start:end]
        
        # Decode back to text
        chunk_text = encoding.decode(chunk_tokens)
        chunks.append(chunk_text)
        
        # Move start position with overlap
        start = end - overlap
    
    logger.info(f"Chunked text into {len(chunks)} chunks")
    return chunks


def create_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Create embeddings for a list of texts using OpenAI.
    
    Args:
        texts: List of texts to embed
    
    Returns:
        List of embedding vectors (1536 dimensions for text-embedding-3-small)
    """
    try:
        response = openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )
        
        embeddings = [item.embedding for item in response.data]
        logger.info(f"Created {len(embeddings)} embeddings")
        return embeddings
    
    except Exception as e:
        logger.error(f"Error creating embeddings: {str(e)}")
        raise


def store_chunks(chunks: List[TextChunk], collection_name: str = "book_chunks") -> None:
    """
    Store chunks in Qdrant Cloud.
    
    Args:
        chunks: List of TextChunk objects to store
        collection_name: Name of the Qdrant collection
    """
    try:
        # Initialize Qdrant client
        qdrant_client = QdrantClient(
            url=config.QDRANT_URL,
            api_key=config.QDRANT_API_KEY
        )
        
        # Create collection if it doesn't exist
        try:
            qdrant_client.get_collection(collection_name)
            logger.info(f"Collection {collection_name} already exists")
        except Exception:
            # Collection doesn't exist, create it
            qdrant_client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(
                    size=1536,  # text-embedding-3-small dimension
                    distance=Distance.COSINE
                )
            )
            logger.info(f"Created collection {collection_name}")
        
        # Prepare points for insertion
        points = []
        for chunk in chunks:
            point = PointStruct(
                id=chunk.chunk_id,
                vector=chunk.embedding,
                payload={
                    "text": chunk.text,
                    "chapter_id": chunk.chapter_id,
                    "chunk_index": chunk.chunk_index,
                    "token_count": chunk.token_count,
                    "metadata": chunk.metadata or {}
                }
            )
            points.append(point)
        
        # Upsert points (insert or update)
        qdrant_client.upsert(
            collection_name=collection_name,
            points=points
        )
        
        logger.info(f"Stored {len(chunks)} chunks in Qdrant")
    
    except Exception as e:
        logger.error(f"Error storing chunks in Qdrant: {str(e)}")
        raise


def ingest_book(docs_path: str = "frontend/docs") -> Dict[str, Any]:
    """
    Ingest all book content from markdown files.
    
    Args:
        docs_path: Path to the docs directory containing markdown files
    
    Returns:
        Dictionary with ingestion statistics
    """
    docs_dir = Path(docs_path)
    
    if not docs_dir.exists():
        raise FileNotFoundError(f"Docs directory not found: {docs_path}")
    
    all_chunks = []
    chapters_processed = 0
    
    # Process each markdown file
    for md_file in docs_dir.glob("*.md"):
        chapter_id = md_file.stem  # filename without extension
        
        logger.info(f"Processing chapter: {chapter_id}")
        
        # Read markdown file
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Chunk the content
        text_chunks = chunk_text(content)
        
        # Create embeddings for all chunks
        embeddings = create_embeddings(text_chunks)
        
        # Create TextChunk objects
        for idx, (chunk_text, embedding) in enumerate(zip(text_chunks, embeddings)):
            chunk = TextChunk(
                chunk_id=f"{chapter_id}_{idx}",
                text=chunk_text,
                embedding=embedding,
                chapter_id=chapter_id,
                chunk_index=idx,
                token_count=len(encoding.encode(chunk_text)),
                metadata={"file": md_file.name}
            )
            all_chunks.append(chunk)
        
        chapters_processed += 1
    
    # Store all chunks in Qdrant
    if all_chunks:
        store_chunks(all_chunks)
    
    return {
        "chapters_processed": chapters_processed,
        "total_chunks": len(all_chunks),
        "status": "success"
    }

