# Implementation Guide

This chapter provides a step-by-step guide on how this hackathon project was built, following the Spec-Driven Development workflow with Spec-Kit Plus.

## Project Overview

This project demonstrates:
- **Spec-Driven Development** using Spec-Kit Plus
- **AI-Driven Development** using Claude Code
- **RAG Implementation** with OpenAI and Qdrant
- **Full-Stack Development** with Docusaurus and FastAPI

## Development Workflow

### Phase 1: Constitution

We started by defining the project constitution (`.specify/memory/constitution.md`):

- **Core Principles**: Spec-Driven Development, Reusable Intelligence, AI-Driven Development
- **Technical Stack**: Docusaurus, FastAPI, Qdrant Cloud, OpenAI
- **Quality Requirements**: Educational clarity, security, documentation
- **Governance**: Amendment procedures and versioning

### Phase 2: Specification

Created detailed feature specification (`specs/001-hackathon-app/spec.md`):

- **4 User Stories**: Book, RAG chatbot, selected-text mode, agent skills
- **28 Functional Requirements**: Detailed requirements for each feature
- **10 Success Criteria**: Measurable outcomes
- **Key Entities**: Data models and relationships

### Phase 3: Planning

Developed implementation plan (`specs/001-hackathon-app/plan.md`):

- **Architecture**: Frontend/backend separation, API design
- **Technology Choices**: Docusaurus, FastAPI, Qdrant, OpenAI
- **Data Models**: Chunk, Question, Answer, SourceCitation
- **API Contracts**: OpenAPI specification

### Phase 4: Task Breakdown

Created 100 actionable tasks (`specs/001-hackathon-app/tasks.md`):

- **Phase 1**: Setup (8 tasks)
- **Phase 2**: Foundational (11 tasks)
- **Phase 2.5**: Architecture Documentation (4 ADRs)
- **Phase 3**: User Story 1 - Book (13 tasks)
- **Phase 4**: User Story 2 - RAG (22 tasks)
- **Phase 5**: User Story 3 - Selected-text (11 tasks)
- **Phase 6**: User Story 4 - Agent Skills (14 tasks)
- **Phase 7**: Polish (11 tasks)

### Phase 5: Architecture Documentation

Created ADRs before implementation:

- **ADR-001**: Docusaurus choice rationale
- **ADR-002**: FastAPI choice rationale
- **ADR-003**: RAG strategy (chunking, embeddings, retrieval)
- **ADR-004**: Deployment approach

### Phase 6: Implementation

Following the task breakdown, we implemented:

1. **Project Setup**: Created backend/ and frontend/ directories
2. **Backend Foundation**: FastAPI app with CORS and error handling
3. **Frontend Foundation**: Docusaurus configuration for GitHub Pages
4. **Book Chapters**: Created 7 educational chapters
5. **RAG Backend**: Ingestion and query services
6. **Chatbot UI**: React component for user interaction
7. **Selected-Text Mode**: Text selection and context passing
8. **Agent Skills**: Three reusable skills with P+Q+P pattern

## Technical Implementation Details

### Backend Structure

```
backend/
├── src/
│   ├── api/
│   │   ├── main.py          # FastAPI app, CORS, error handlers
│   │   └── endpoints/       # API endpoints (ingest, ask, ask_selected, skills)
│   ├── models/              # Data models (Chunk, Question, Answer, etc.)
│   ├── services/
│   │   ├── ingestion_service.py  # Chunking, embedding, storage
│   │   ├── rag_service.py       # RAG query and generation
│   │   └── skills/              # Agent skills (SummarizeSection, etc.)
│   └── config.py           # Environment variables and logging
├── requirements.txt
└── .env.example
```

### Frontend Structure

```
frontend/
├── docs/                    # Book chapters (markdown files)
│   ├── intro.md
│   ├── ai-driven-development.md
│   ├── spec-driven-development.md
│   ├── rag-fundamentals.md
│   ├── implementation-guide.md
│   ├── chatbot-usage.md
│   └── future-work.md
├── src/
│   ├── components/
│   │   ├── Chatbot.tsx      # Main chatbot component
│   │   └── SelectedTextHandler.tsx  # Text selection handler
│   ├── config.js           # API base URL configuration
│   └── css/
│       └── custom.css      # Custom styles
├── docusaurus.config.js    # Docusaurus configuration
└── sidebars.js             # Navigation sidebar
```

### RAG Implementation

**Ingestion Process**:
1. Read all markdown files from `frontend/docs/`
2. Chunk text using semantic chunking (200-300 tokens, 50 token overlap)
3. Create embeddings using OpenAI text-embedding-3-small
4. Store chunks in Qdrant Cloud collection "book_chunks"

**Query Process**:
1. Embed user question using same embedding model
2. Query Qdrant for top 5 similar chunks (cosine similarity)
3. Combine chunks into context
4. Generate answer using OpenAI ChatKit SDK with context
5. Return answer with source citations

**Selected-Text Mode**:
1. User selects text in the book
2. Selected text is passed directly to OpenAI (no RAG query)
3. Answer generated using only selected text as context
4. Clear message if answer cannot be found in selection

## Key Design Decisions

### 1. Chunking Strategy

**Decision**: Semantic chunking with 200-300 tokens, 50 token overlap

**Rationale**:
- Balances context preservation with retrieval precision
- Overlap ensures important information at boundaries isn't lost
- Size fits within model context limits

### 2. Embedding Model

**Decision**: OpenAI text-embedding-3-small (1536 dimensions)

**Rationale**:
- Good balance of quality and cost
- Consistent with OpenAI chat completions
- Sufficient for semantic similarity

### 3. Vector Database

**Decision**: Qdrant Cloud Free Tier

**Rationale**:
- Sufficient for hackathon scale (hundreds of chunks)
- Managed service, no infrastructure setup
- Fast similarity search

### 4. Retrieval Strategy

**Decision**: Top 5 chunks using cosine similarity

**Rationale**:
- Provides enough context without overwhelming model
- Standard metric for semantic similarity
- Fits within context window limits

## Development Tools and Commands

### Backend

```bash
# Setup
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Run
uvicorn src.api.main:app --reload
```

### Frontend

```bash
# Setup
cd frontend
npm install

# Development
npm start

# Build
npm run build

# Deploy to GitHub Pages
npm run deploy
```

## Testing

### Manual Testing

1. **Book Navigation**: Verify all chapters accessible, links work
2. **RAG Queries**: Ask questions, verify answers are from book content
3. **Selected-Text**: Select text, ask questions, verify context-only answers
4. **Agent Skills**: Test each skill with book content
5. **Error Handling**: Test with invalid inputs, API failures

### Success Criteria Validation

- SC-001: Navigation within 3 clicks ✓
- SC-002: Build completes in under 2 minutes ✓
- SC-003: 90% of answers accurate within 5 seconds
- SC-004: 85% of questions retrieve relevant chunks
- SC-005: 95% of valid selections get accurate answers
- SC-006: 100% of "not found" cases clearly stated
- SC-007: Responsive design works on 320px-1920px
- SC-008: 90% of skill invocations produce matching outputs
- SC-009: All skills documented with P+Q+P
- SC-010: 100% of errors show user-friendly messages

## Deployment

### GitHub Pages (Frontend)

1. Configure `docusaurus.config.js` with GitHub Pages settings
2. Push to repository
3. Enable GitHub Pages in repository settings
4. Run `npm run deploy` or use GitHub Actions

### Backend Hosting

Options:
- **Local Development**: `uvicorn src.api.main:app --reload`
- **Cloud Hosting**: Render, Railway, Fly.io (free tiers available)
- **Environment Variables**: Set OPENAI_API_KEY, QDRANT_URL, QDRANT_API_KEY

## Lessons Learned

1. **Spec-Driven Development**: Clear specifications reduce ambiguity and rework
2. **AI Assistance**: AI tools accelerate development while maintaining quality
3. **RAG Implementation**: Proper chunking and retrieval are critical for quality
4. **Documentation**: ADRs and PHRs capture valuable knowledge for future projects
5. **Testing**: Manual testing is essential for validating RAG quality

## Conclusion

This project demonstrates how Spec-Driven Development, combined with AI-Driven Development, can create high-quality software efficiently. The structured workflow (Constitution → Specify → Plan → Tasks → Implement) ensures clarity, traceability, and reusable intelligence capture.

By following this guide, you can understand how each component was built and why certain decisions were made. This knowledge can be applied to future projects using similar methodologies.

---

**Previous**: [RAG Fundamentals ←](./rag-fundamentals.md) | **Next**: [How to Use the Chatbot →](./chatbot-usage.md)

