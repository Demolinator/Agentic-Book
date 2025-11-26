<!--
Sync Impact Report:
- Version change: [none] → 1.0.0 (initial constitution)
- Modified principles: N/A (new constitution)
- Added sections: Core Principles, Technical Stack, Quality Requirements, Spec-Driven Development and Reusable Intelligence, Governance
- Removed sections: N/A
- Templates requiring updates:
  - ✅ spec-template.md (aligned with constitution principles)
  - ✅ plan-template.md (aligned with constitution principles)
  - ✅ tasks-template.md (aligned with constitution principles)
  - ✅ All command templates verified for consistency
- Follow-up TODOs: None
-->

# AI-Driven and Spec-Driven Faculty Hackathon Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
Every significant feature MUST follow the Spec-Kit Plus workflow: Constitution → Specify → Plan → Tasks → Implement. No feature implementation begins without a specification, plan, and task breakdown. This ensures clarity, traceability, and reusable intelligence capture.

**Rationale**: Spec-driven development transforms ad-hoc coding into systematic, documented, and reusable intelligence. Each feature generates both working code and permanent reasoning artifacts (specs, plans, ADRs, prompt histories) that compound value across projects.

### II. Reusable Intelligence as First-Class Artifacts
Code is ephemeral; intelligence is permanent. Every feature MUST capture reasoning patterns, architectural decisions, and effective prompts as first-class artifacts (ADRs, PHRs, specs, plans). These artifacts are read by AI agents and humans to accelerate future work.

**Rationale**: Intelligence compounds—Project 1 teaches lessons that Project 10 inherits. ADRs explain "WHY" behind decisions; PHRs log what prompts work vs fail; specs and plans become reusable templates for similar features.

### III. AI-Driven Development with Clear Boundaries
Use AI tools (Claude Code, OpenAI, etc.) to accelerate development, but maintain clear boundaries: AI generates code based on specifications; humans review, test, and own the final implementation. All AI interactions that produce effective results MUST be logged as prompt history records.

**Rationale**: AI tools are force multipliers when guided by clear specifications. Logging effective prompts creates a searchable playbook for future AI collaboration, avoiding repeated mistakes.

### IV. Educational Clarity and Simplicity
All code MUST be simple, readable, and well-commented so students can learn from it. Avoid over-engineering. Prefer clear, straightforward implementations over clever abstractions unless complexity is justified and documented in ADRs.

**Rationale**: This is a hackathon project for learning. Complex code that works but is incomprehensible defeats the educational purpose. Simple, documented code teaches better and is easier to maintain.

### V. Security and Secrets Management (NON-NEGOTIABLE)
All sensitive information (API keys, tokens, Qdrant credentials) MUST be kept out of source control. Secrets MUST be loaded only from environment variables or secure configuration files (e.g., `.env` files that are gitignored). Never hard-code credentials.

**Rationale**: Exposed credentials compromise security and violate best practices. Environment-based configuration is standard, testable, and secure.

### VI. Architecture Decision Documentation
All major architecture decisions (framework choice, RAG strategy, chunking strategy, deployment approach) MUST be documented as ADRs (Architectural Decision Records) using Spec-Kit Plus templates. ADRs explain the "WHY" behind choices, not just the "WHAT" was built.

**Rationale**: ADRs create institutional memory. Future developers (and AI agents) understand why FastAPI was chosen over Flask, why a specific chunking strategy was used, etc. This prevents repeated debates and enables informed evolution.

## Technical Stack

### Required Technologies
- **Frontend/Book**: Docusaurus for the book site and documentation, deployed to GitHub Pages
- **Backend API**: Python FastAPI for the backend API
- **Vector Database**: Qdrant Cloud Free Tier as the vector database for storing book embeddings
- **AI Services**: OpenAI for embeddings and chat completions (Agents SDK / ChatKit or standard API)
- **Source Control**: GitHub for source control and CI/CD where possible
- **Configuration**: Environment variables or `.env` files for all API keys and secrets (never hard-coded)

### Stack Rationale
This stack balances educational value, free-tier availability, and production-readiness. Docusaurus provides excellent documentation tooling; FastAPI is modern and Python-friendly; Qdrant Cloud Free Tier enables vector search without infrastructure management; OpenAI provides reliable embeddings and chat completions.

## Quality Requirements

### Docusaurus Book Standards
- The book MUST be organized into clear chapters covering: AI-Driven Development, Spec-Driven Development, RAG fundamentals, implementation guide, how to use the chatbot, and future work
- The site MUST build and run locally with a simple, documented command sequence
- The site MUST deploy successfully to GitHub Pages
- All chapters MUST be internally linked and navigable
- Content MUST be clear, consistent, and educational

### RAG Backend Standards
- The RAG backend MUST ingest all book content into Qdrant as chunks with embeddings
- The RAG backend MUST answer questions using only the ingested book content as context
- The RAG backend MUST handle errors from Qdrant and OpenAI gracefully with clear error messages
- The RAG backend MUST return answers with optional source citations (chunk IDs or references)
- If the answer cannot be found in the book context, the chatbot MUST clearly state this instead of hallucinating

### Selected-Text Mode Standards
- Selected-text mode MUST accept user-selected text and a question
- Selected-text mode MUST answer strictly based on that provided text, without pulling in unrelated external knowledge
- Selected-text mode MUST clearly tell the user if the answer cannot be found in that selected context
- Selected-text mode MUST NOT perform RAG queries when in selected-text mode—it uses only the provided context

### Code Quality Standards
- Code MUST be simple, readable, and well-commented for student learning
- Code MUST avoid unnecessary over-engineering
- All major functions and classes MUST have docstrings
- Error handling MUST be explicit and user-friendly
- Logging MUST be included for debugging and monitoring

## Spec-Driven Development and Reusable Intelligence

### Feature Specification Requirements
Every significant feature (book, RAG backend, chatbot UI, selected-text mode, agent skills) MUST have:
- A short specification in the `.specify` directory describing what it does, inputs/outputs, and acceptance criteria
- An implementation plan describing architecture and main steps
- A task list breaking work into small, testable steps

### Prompt History Capture
When particularly effective prompts are discovered (for generating book content, RAG prompts, or agent skills), they MUST be captured as prompt history records (PHRs) for reuse. PHRs document what prompts work vs fail, creating a searchable playbook for future AI collaboration.

### Reusable Agent Skills Design
Where appropriate, design reusable skills/subagents (for example: summarizing sections, generating quiz questions, explaining terms) using clear persona, questions, and principles (P+Q+P pattern) so they can be reused in future projects. Skills MUST be documented with their persona, analytical questions, and decision principles.

## Governance

This Constitution supersedes all other development practices for this project. All PRs and reviews MUST verify compliance with Constitution principles.

### Amendment Procedure
- Amendments require documentation of rationale and impact
- Constitution version MUST follow semantic versioning:
  - **MAJOR**: Backward incompatible governance/principle removals or redefinitions
  - **MINOR**: New principle/section added or materially expanded guidance
  - **PATCH**: Clarifications, wording, typo fixes, non-semantic refinements
- All amendments MUST update the Sync Impact Report at the top of this file
- Amendments MUST propagate to dependent templates (spec, plan, tasks) for consistency

### Compliance Review
- Before implementation: Verify specification aligns with Constitution principles
- During planning: Verify plan respects Constitution constraints (security, simplicity, spec-driven flow)
- During implementation: Verify code follows Constitution standards (security, clarity, documentation)
- Before merge: Verify all Constitution requirements are met (ADRs for major decisions, PHRs for effective prompts, specs/plans/tasks for all features)

### Complexity Justification
If any feature requires violating Constitution principles (e.g., adding unnecessary complexity), it MUST be:
1. Documented in an ADR explaining why the violation is necessary
2. Justified with specific problem statements and rejected simpler alternatives
3. Reviewed and approved before implementation

**Version**: 1.0.0 | **Ratified**: 2025-01-27 | **Last Amended**: 2025-01-27
