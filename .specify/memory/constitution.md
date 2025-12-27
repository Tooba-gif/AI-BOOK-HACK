<!--
Sync Impact Report:
- Version change: N/A → 1.0.0 (initial version)
- Modified principles: All principles completely redefined for this project
- Added sections: Mission, Core Development, Success Criteria, Non Goals, Architecture Principles, User Stories, Constraints, Risks & Mitigation, Definition of Done
- Removed sections: Original template placeholders
- Templates requiring updates: ✅ .specify/templates/plan-template.md, ✅ .specify/templates/spec-template.md, ✅ .specify/templates/tasks-template.md, ⚠️ README.md (if exists and needs alignment)
- Follow-up TODOs: None
-->
# AI Native Textbook for Physical AI & Humanoid Robotics Constitution

## Core Principles

### I. AI-Native Education
All features must leverage AI capabilities to enhance the learning experience; The product must feel like an intelligent, interactive platform rather than a static textbook; Every component should demonstrate the power of AI in education.

### II. Performance & Simplicity
The platform must be fast-loading, simple to navigate, and beautiful in design; All features should prioritize user experience and intuitive interaction; Complexity must be hidden behind clean, simple interfaces.

### III. Interactive Learning (NON-NEGOTIABLE)
Every chapter must include interactive elements that engage the learner; Content should adapt to different learning styles and backgrounds; All educational content must be accessible and engaging.

### IV. RAG-Powered Intelligence
The chatbot must provide accurate, cited, and grounded answers exclusively from the textbook content; RAG implementation must ensure high-quality responses with proper source attribution; All AI interactions should enhance understanding of Physical AI & Humanoid Robotics concepts.

### V. Personalization & Accessibility
Content must be personalized based on user background and learning preferences; Urdu translation must be available one-click for every chapter; The platform must be accessible across different languages and user needs.

### VI. Modular Architecture
The backend must be modular using FastAPI with clear separation of services and routes; Frontend must remain extremely simple and readable; All data must be stored cleanly in Neon and Qdrant databases.

## Mission
Build a fully AI-native interactive, intelligent textbook that teaches the Physical AI & Humanoid Robotics course. The product must be fast, simple, beautiful and feel like a real AI-powered education platform not just a book.

## Core Development
1. A Docusaurus-based interactive textbook with 6-8 short, clean, modern chapters.
2. A fully functional RAG chatbot answering questions ONLY from the book.
3. User authentication (sign/login) using Better Auth.
4. Personalized chapter content based on user background.
5. One-click Urdu translation for every chapter.
6. Auto-generated summaries, quizzes and learning boosters.

## Success Criteria
1. Clean UI, fast loading, mobile friendly.
2. Book readable in <45 minutes total.
3. RAG answers accurate, cited and grounded.
4. Personalization visibly improves text.
5. Urdu translation high quality and fast.
6. Fully deployed:
   - frontend -> Vercel
   - backend -> Railway
   - vectors -> Qdrant
   - database -> Neon

## Non Goals
- No extra animations beyond minimal useful motion.
- No overly long chapters (clear knowledge delivery).
- No complex robotics code - only educational content.

## Architecture Principles
- Keep frontend extremely simple and readable.
- Keep backend modular (FastAPI + services + routes).
- All data must be stored cleanly in Neon and Qdrant.
- Use clean folder structure:
  - '/backend'
  - '/website'
  - '/rag'
  - '/agents'
- Use reusable agent skills for bonus scoring.

## User Stories (Prioritized)
1. As a learner, I want to read the textbook smoothly.
2. As a learner, I want to ask the chatbot questions.
3. As a learner, I want personalized content based on my background.
4. As a learner, I want Urdu translation.
5. As a learner, I want summaries and quizzes.
6. As an admin, I want clean architecture and deployment.

## Constraints
- Must work on free tier (Qdrant + Neon).
- Must deploy within 90 seconds for demo reading.
- Must support low-end devices (users reading on mobiles).
- Must avoid complexity and heavy dependencies.

## Risk & Mitigation
- RAG low accuracy -> use chunking + miniLM embeddings.
- Token usage high -> implement in phases.
- User confusion -> keep UI minimal and clean.
- Backend errors -> add health checks + logging.

## Definition of Done
- All chapters visible and readable.
- Chatbot fully functional with grounded answers.
- Auth + personalization + translation working.
- Quizzes + summaries per chapter generated.
- Fully deployed URLs live and stable.
- 90-seconds demo recorded.

## Governance
This constitution supersedes all other practices for this project; All amendments must be documented with clear rationale; All PRs/reviews must verify compliance with these principles; Features must align with the mission of creating an AI-native educational platform.

**Version**: 1.0.0 | **Ratified**: 2025-06-13 | **Last Amended**: 2025-12-23