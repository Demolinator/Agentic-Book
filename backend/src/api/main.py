"""
FastAPI application main module with CORS configuration and error handling.
"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from typing import Dict, Any

from src.config import config

logger = logging.getLogger(__name__)

# Create FastAPI app instance
app = FastAPI(
    title="Hackathon RAG API",
    description="RAG-based chatbot API for the hackathon book",
    version="1.0.0"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exception handlers for Qdrant errors
@app.exception_handler(Exception)
async def qdrant_error_handler(request: Request, exc: Exception):
    """
    Handle Qdrant-related errors gracefully.
    
    Args:
        request: FastAPI request object
        exc: Exception that was raised
        
    Returns:
        JSONResponse with error message
    """
    logger.error(f"Qdrant error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Vector database error",
            "message": "An error occurred while accessing the vector database. Please try again later.",
            "detail": str(exc) if config.validate() else "Configuration error"
        }
    )


# Exception handler for OpenAI errors
@app.exception_handler(ValueError)
async def openai_error_handler(request: Request, exc: ValueError):
    """
    Handle OpenAI API errors gracefully.
    
    Args:
        request: FastAPI request object
        exc: ValueError that was raised
        
    Returns:
        JSONResponse with error message
    """
    logger.error(f"OpenAI error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "AI service error",
            "message": "An error occurred while processing your request. Please try again later.",
            "detail": str(exc)
        }
    )


@app.get("/")
async def root():
    """Root endpoint for health check."""
    return {"message": "Hackathon RAG API", "status": "running"}

