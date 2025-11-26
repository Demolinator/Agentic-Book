# RAG Fundamentals

RAG (Retrieval-Augmented Generation) is a technique that combines information retrieval with text generation to create AI systems that can answer questions based on specific knowledge sources, rather than relying solely on pre-trained model knowledge.

## What is RAG?

RAG works by:

1. **Retrieving** relevant information from a knowledge base (like this book)
2. **Augmenting** the AI's context with that retrieved information
3. **Generating** answers based on the augmented context

This allows AI systems to:
- Answer questions about specific documents or knowledge bases
- Provide accurate, up-to-date information
- Cite sources for their answers
- Avoid "hallucinating" information not in the knowledge base

## How RAG Works

### Step 1: Knowledge Base Preparation

First, the knowledge base (like this book) is processed:

1. **Chunking**: Text is split into smaller pieces (chunks) of 200-300 tokens
2. **Embedding**: Each chunk is converted into a vector (numerical representation) using an embedding model
3. **Storage**: Vectors are stored in a vector database (like Qdrant) for fast similarity search

### Step 2: Question Processing

When a user asks a question:

1. **Question Embedding**: The question is converted into a vector using the same embedding model
2. **Similarity Search**: The vector database is searched for chunks with similar vectors
3. **Retrieval**: Top N most relevant chunks are retrieved (e.g., top 5 chunks)

### Step 3: Answer Generation

The retrieved chunks are used to generate an answer:

1. **Context Assembly**: Retrieved chunks are combined into a context
2. **Prompt Construction**: A prompt is created with the question and context
3. **Generation**: An AI language model (like OpenAI's GPT) generates an answer based on the context
4. **Source Citation**: The answer includes references to the source chunks

## RAG Architecture

```
┌─────────────┐
│   User      │
│  Question   │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Question       │
│  Embedding      │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│  Vector         │
│  Database       │──┐
│  (Qdrant)       │  │ Similarity Search
└─────────────────┘  │
       │              │
       │              │
       ▼              │
┌─────────────────┐  │
│  Top N Chunks   │◄─┘
│  Retrieved      │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│  Context +      │
│  Question       │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│  LLM            │
│  (OpenAI GPT)   │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│  Answer +       │
│  Sources        │
└─────────────────┘
```

## Key Components

### 1. Embedding Model

Converts text into numerical vectors that capture semantic meaning. Common models:

- **OpenAI text-embedding-3-small**: 1536 dimensions, good balance of quality and cost
- **OpenAI text-embedding-3-large**: Higher quality but more expensive
- **Open-source alternatives**: Sentence-BERT, Instructor, etc.

### 2. Vector Database

Stores and searches vectors efficiently. Options include:

- **Qdrant**: Fast, scalable, cloud-hosted option
- **Pinecone**: Managed vector database service
- **Weaviate**: Open-source vector database
- **Chroma**: Lightweight, embedded option

### 3. Chunking Strategy

How text is split into chunks affects retrieval quality:

- **Fixed-size chunks**: Simple but may split concepts
- **Semantic chunking**: Splits at natural boundaries
- **Overlapping chunks**: Ensures context at boundaries
- **Hierarchical chunks**: Multiple sizes for different query types

### 4. Retrieval Strategy

How relevant chunks are selected:

- **Top-K retrieval**: Return K most similar chunks
- **Similarity threshold**: Only return chunks above a threshold
- **Hybrid search**: Combine vector search with keyword search
- **Re-ranking**: Use a second model to re-rank results

### 5. Generation Model

The language model that generates answers:

- **OpenAI GPT-4**: High quality, good reasoning
- **OpenAI GPT-3.5**: Faster, lower cost
- **Claude**: Alternative high-quality model
- **Open-source LLMs**: Llama, Mistral, etc.

## RAG in This Project

This hackathon project implements RAG for answering questions about this book:

### Knowledge Base

- **Source**: All markdown files in `frontend/docs/`
- **Chunking**: Semantic chunking with 200-300 tokens, 50 token overlap
- **Embedding**: OpenAI text-embedding-3-small (1536 dimensions)
- **Storage**: Qdrant Cloud Free Tier

### Retrieval

- **Method**: Cosine similarity search
- **Top-K**: 5 most relevant chunks
- **Threshold**: No minimum threshold (returns top 5)

### Generation

- **Model**: OpenAI ChatKit SDK (GPT-3.5 or GPT-4)
- **Context**: Retrieved chunks + user question
- **Output**: Answer with optional source citations

### Features

1. **RAG Mode**: Answers questions using the entire book as context
2. **Selected-Text Mode**: Answers questions using only user-selected text (no RAG query)
3. **Source Citations**: Shows which chunks were used to generate answers

## Advantages of RAG

### 1. Accuracy

- Answers are based on actual source material
- Reduces hallucinations
- Provides verifiable information

### 2. Up-to-Date Information

- Knowledge base can be updated without retraining models
- New information can be added quickly
- Specific to your domain or documents

### 3. Transparency

- Source citations show where information came from
- Users can verify answers
- Builds trust in the system

### 4. Cost-Effective

- No need to fine-tune large models
- Can use smaller, cheaper models
- Update knowledge base without retraining

## Challenges and Solutions

### Challenge 1: Chunking Quality

**Problem**: Poor chunking can split important concepts.

**Solution**: Use semantic chunking with overlap, test different chunk sizes.

### Challenge 2: Retrieval Quality

**Problem**: Relevant chunks might not be retrieved.

**Solution**: Use better embeddings, increase top-K, try hybrid search.

### Challenge 3: Context Limits

**Problem**: Too many chunks exceed model context limits.

**Solution**: Limit number of chunks, use compression, prioritize most relevant.

### Challenge 4: Answer Quality

**Problem**: Model might ignore context or hallucinate.

**Solution**: Use better prompts, enforce context usage, add validation.

## Best Practices

1. **Chunking**: Use semantic chunking with overlap for better context
2. **Embeddings**: Choose appropriate embedding model for your domain
3. **Retrieval**: Retrieve enough chunks (5-10) but not too many
4. **Prompts**: Clearly instruct the model to use only provided context
5. **Validation**: Check that answers are actually in the retrieved chunks
6. **Citations**: Always provide source citations for transparency

## Conclusion

RAG is a powerful technique for building AI systems that can answer questions about specific knowledge bases. By combining retrieval with generation, RAG systems can provide accurate, verifiable answers while avoiding hallucinations.

This project demonstrates RAG implementation using modern tools (OpenAI, Qdrant, FastAPI) and best practices (semantic chunking, source citations, context validation).

---

**Previous**: [Spec-Driven Development ←](./spec-driven-development.md) | **Next**: [Implementation Guide →](./implementation-guide.md)

