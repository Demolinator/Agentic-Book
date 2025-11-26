---
id: phr-20250127-000000
title: Initial Hackathon Constitution Creation
stage: constitution
date: 2025-01-27
surface: cursor
model: claude
feature: hackathon
branch: main
user: talal
command: /sp.constitution
labels: [constitution, initial-setup, hackathon]
links:
  spec: 
  ticket: 
  adr: 
  pr: 
files:
  - .specify/memory/constitution.md
tests:
  - N/A (constitution phase)
---

## Prompt

/sp.constitution 

Project principles and standards:

Build an AI-Driven and Spec-Driven demo application for the faculty hackathon.

Create a Docusaurus-based "book" that explains AI-Driven Development, Spec-Driven Development, RAG, and how this project is built.

Develop a RAG-based chatbot that answers questions strictly from the book content.

Support a special mode where the user selects text in the book and asks questions only about that selected text.

Use Spec-Kit Plus phases (Constitution → Specify → Plan → Tasks → Implement) for every major feature.

Capture reusable intelligence (specs, plans, ADRs, prompt histories) as first-class artifacts, not just code.

Technical stack:

Docusaurus for the book site and documentation, deployed to GitHub Pages.

Python FastAPI for the backend API.

Qdrant Cloud Free Tier as the vector database for storing book embeddings.

OpenAI for embeddings and chat completions (Agents SDK / ChatKit or standard API).

GitHub for source control and CI/CD where possible.

Environment variables or .env files for all API keys and secrets (never hard-coded).

Quality requirements:

The Docusaurus book must be organized into clear chapters covering: AI-Driven Development, Spec-Driven Development, RAG fundamentals, implementation guide, how to use the chatbot, and future work.

The site must build and run locally with a simple, documented command sequence, and be deployed successfully to GitHub Pages.

The RAG backend must:

Ingest all book content into Qdrant as chunks with embeddings.

Answer questions using only the ingested book content as context.

Handle errors from Qdrant and OpenAI gracefully with clear error messages.

The selected-text mode must:

Accept user-selected text and a question.

Answer strictly based on that provided text, without pulling in unrelated external knowledge.

Clearly tell the user if the answer cannot be found in that selected context.

All major architecture decisions (framework choice, RAG strategy, chunking strategy, deployment approach) must be documented as ADRs using Spec-Kit Plus templates.

All sensitive information (API keys, tokens, Qdrant credentials) must be kept out of source control and loaded only from environment variables or secure configuration.

Code should be simple, readable, and well-commented so that students can learn from it, avoiding unnecessary over-engineering.

Spec-Driven Development and reusable intelligence:

Every significant feature (book, RAG backend, chatbot UI, selected-text mode, agent skills) must have:

A short specification in the .specify directory (what it does, inputs/outputs, acceptance criteria).

An implementation plan describing architecture and main steps.

A task list breaking work into small, testable steps.

When particularly effective prompts are discovered (for generating book content, RAG prompts, or agent skills), they should be captured as prompt history records for reuse.

Where appropriate, design reusable skills/subagents (for example: summarizing sections, generating quiz questions, explaining terms) using clear persona, questions, and principles so they can be reused in future projects.

## Response snapshot

Created comprehensive constitution document at `.specify/memory/constitution.md` with:

1. **Core Principles** (6 principles):
   - Spec-Driven Development (NON-NEGOTIABLE)
   - Reusable Intelligence as First-Class Artifacts
   - AI-Driven Development with Clear Boundaries
   - Educational Clarity and Simplicity
   - Security and Secrets Management (NON-NEGOTIABLE)
   - Architecture Decision Documentation

2. **Technical Stack Section**: Documented required technologies (Docusaurus, FastAPI, Qdrant Cloud, OpenAI, GitHub) with rationale.

3. **Quality Requirements Section**: Detailed standards for:
   - Docusaurus book (chapters, deployment, navigation)
   - RAG backend (ingestion, querying, error handling)
   - Selected-text mode (strict context usage)
   - Code quality (simplicity, documentation, error handling)

4. **Spec-Driven Development and Reusable Intelligence Section**: Requirements for specs/plans/tasks, PHR capture, and reusable agent skills design.

5. **Governance Section**: Amendment procedure, compliance review process, complexity justification requirements.

6. **Version**: 1.0.0 (initial constitution), ratified and last amended 2025-01-27.

The constitution follows Spec-Kit Plus template structure, fills all placeholders, includes Sync Impact Report, and is ready for use in subsequent phases (specify, plan, tasks, implement).

## Outcome

- ✅ Impact: Established foundational governance for hackathon project. Constitution defines non-negotiable principles, technical stack, quality requirements, and spec-driven workflow. All downstream work (specs, plans, tasks, implementations) will inherit these standards.
- 🧪 Tests: N/A (constitution phase)
- 📁 Files: `.specify/memory/constitution.md` (created/updated)
- 🔁 Next prompts: `/sp.specify` for feature specifications (book, RAG backend, chatbot UI, selected-text mode, agent skills)
- 🧠 Reflection: Constitution successfully captures project requirements with clear, testable principles. Structure follows Spec-Kit Plus best practices with proper versioning, governance, and reusable intelligence focus.

## Evaluation notes (flywheel)

- Failure modes observed: None (initial creation)
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to `/sp.specify` phase to create feature specifications that inherit constitution principles

