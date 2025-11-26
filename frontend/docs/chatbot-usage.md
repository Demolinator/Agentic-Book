# How to Use the Chatbot

This chapter explains how to use the embedded RAG chatbot to ask questions about this book. The chatbot can answer questions using the entire book content or just selected text.

## Chatbot Features

The chatbot supports two modes:

1. **RAG Mode**: Answers questions using the entire book as context
2. **Selected-Text Mode**: Answers questions using only selected text

## RAG Mode - Asking Questions About the Book

### How to Use

1. **Find the Chatbot**: The chatbot interface is embedded in this page (or available on other pages)
2. **Type Your Question**: Enter your question in the input field
3. **Submit**: Click the send button or press Enter
4. **View Answer**: The chatbot will display the answer with optional source citations

### Example Questions

- "What is Spec-Driven Development?"
- "How does RAG work?"
- "What are the benefits of AI-Driven Development?"
- "Explain the chunking strategy used in this project"
- "What is the difference between RAG mode and selected-text mode?"

### Understanding Answers

- **Answer Text**: The main response generated from book content
- **Source Citations**: Links or references to the chapters/sections used
- **Confidence Indicators**: Some answers may include confidence levels

### Limitations

- **Book Content Only**: The chatbot only uses information from this book
- **No External Knowledge**: It won't answer questions about topics not covered in the book
- **Clear Messages**: If an answer cannot be found, the chatbot will clearly state this

## Selected-Text Mode - Asking About Specific Text

### How to Use

1. **Select Text**: Highlight any text in the book pages
2. **Ask Button**: A button will appear saying "Ask about this selection"
3. **Click Button**: Opens the chatbot with selected text as context
4. **Type Question**: Enter your question about the selected text
5. **Get Answer**: The chatbot answers using only the selected text

### Example Use Cases

- Select a paragraph about "chunking strategy" and ask "What is the recommended chunk size?"
- Select a section about "RAG architecture" and ask "How does retrieval work?"
- Select code examples and ask "Explain this code"

### Key Features

- **Context-Specific**: Answers only use the selected text, not the entire book
- **No RAG Query**: Faster responses since no vector search is performed
- **Focused Answers**: Perfect for understanding specific sections

## Best Practices

### For RAG Mode

1. **Be Specific**: Ask clear, specific questions
2. **Use Keywords**: Include relevant terms from the book
3. **One Question at a Time**: Ask one question per message
4. **Check Sources**: Review source citations to verify information

### For Selected-Text Mode

1. **Select Relevant Text**: Choose text that contains the information you need
2. **Complete Context**: Select enough text to provide context
3. **Clear Questions**: Ask questions that can be answered from the selection
4. **Verify Answers**: Check that answers match the selected text

## Troubleshooting

### No Answer Provided

**Problem**: Chatbot says "Answer cannot be found"

**Solutions**:
- Try rephrasing your question
- Use different keywords
- Check if the topic is covered in the book
- Try selected-text mode with relevant text

### Irrelevant Answers

**Problem**: Answer doesn't match the question

**Solutions**:
- Be more specific in your question
- Use selected-text mode for focused queries
- Check source citations to see what was used

### Slow Responses

**Problem**: Chatbot takes too long to respond

**Solutions**:
- Use selected-text mode for faster responses
- Check network connection
- Verify backend API is running

### Error Messages

**Problem**: Error message appears

**Solutions**:
- Check if backend API is accessible
- Verify API keys are configured
- Check browser console for details
- Try refreshing the page

## Chatbot Interface

The chatbot interface includes:

- **Message History**: Previous questions and answers
- **Input Field**: Where you type questions
- **Send Button**: Submit your question
- **Source Citations**: Links to source material
- **Loading Indicator**: Shows when processing

## Technical Details

### API Endpoints

- **POST /ask**: RAG mode - answers using entire book
- **POST /ask_selected**: Selected-text mode - answers using selected text only

### Response Format

```json
{
  "answer": "The answer text...",
  "sources": [
    {
      "chunk_id": "chunk_123",
      "chapter": "rag-fundamentals",
      "relevance_score": 0.95,
      "snippet": "Relevant text snippet..."
    }
  ],
  "confidence": 0.9
}
```

### Error Handling

- **API Errors**: User-friendly error messages
- **No Results**: Clear message when answer cannot be found
- **Network Errors**: Retry suggestions and error details

## Privacy and Security

- **No Data Storage**: Questions and answers are not permanently stored
- **API Keys**: All API keys are server-side only
- **Source Citations**: Only book content is used, no external data

## Tips for Best Results

1. **Read First**: Read the relevant chapter before asking questions
2. **Be Specific**: More specific questions get better answers
3. **Use Keywords**: Include terms from the book in your questions
4. **Check Sources**: Always review source citations
5. **Try Both Modes**: Use RAG mode for general questions, selected-text for specific sections

## Conclusion

The chatbot provides an interactive way to learn about the topics covered in this book. By using RAG mode for general questions and selected-text mode for specific sections, you can get accurate, context-aware answers based on the book content.

Experiment with different questions and modes to find what works best for your learning style!

---

**Previous**: [Implementation Guide ←](./implementation-guide.md) | **Next**: [Future Work →](./future-work.md)

