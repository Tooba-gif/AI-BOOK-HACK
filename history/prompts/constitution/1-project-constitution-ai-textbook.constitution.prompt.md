---
id: 1
title: Project Constitution AI Textbook
stage: constitution
date: 2025-12-23
surface: agent
model: Qwen
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution,ai,textbook,physical-ai,humanoid-robotics]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - null
---

## Prompt

```
/sp.constitution Project Constitution : AI Native Textbook for Physical AI & Humanoid Robotics

1# Mission
Build a fully AI-native interaction , intelligent textbook that teaches the Physical AI & Humanoid Robotics course.
the product must be fast , simple ,beautiful and feel like a real Ai powered education platform not just a book.

2# Core development 
1. A docusaurus based interactive textbook with 6-8 short , clean ,modern chapters.
2. A fully function RAG chatbot answering question ONLY from the book.
3. User authentication (sign/login)using better auth.
4. Personalized chapter content based user background
5. One click urdu translation for every chapter.
6. Auto generated summaries , quizzes and learning boosters.

3# Success Criteria 
1. Clean UI , fast loading , mobile friendly.
2. Book readable in <45 minutes total.
3. RAG answers accurate , cited and grounded.
4. Personalization visibly improves text.
5. Urdu translation high quality and fast.
6. Fullly deployed:
 - frontend -> vercel
 - backend -> railway 
 - vectors -> qdrant
 - databased -> neon
 
4# Non Goals
-No extra animations beyond minimal useful motion .
-No overly long chapters ( clear knownledgement )
-No complex robotics code - only educational content.

5# Architecture Priciples 
-Keep frontend extrremely simple and readable.
-Keep backend modular (fastAPI+ services+ routes).
-All data must be stored cleanly in Neon and Qdrant.
-Use clean folde structure:
  - '/backend '
  - '/website'
  - '/rag'
  - '/agents'
-Use reuable agent skills for bonus scoring.

6# User Stories (Prioritized)
1. As a learner, I want to read the textbook smoothly.
2. As a learner, I want to ask the chatbot questions.
3. As a learner, I want to personalized content based on my background
4. As a learner, I want to urdu translation.
5. As a learner, I want to summarizes and quizzes.
6. As a admin, I want to clean architecture and deployment.

7# Constraints 
-Must work on free tier (Qdrant + neon).
-Must deploy within 90 seconds demo reading.
-Must support low-end devices (user reading on mobiles).
-Must avoid complexity and heavy dependencies.

8# Risk & Mitigation 
- RAG low accuracy -> use chunking+ miniLM embeddings.
- Token usage high -> implement in phases.
- User confusion -> keep UI minimal and clean.
- Backend errors -> add health checks + logging.

9# Definition of Done
- All chapters visible and readable.
- Chatbot fully funtional with grounded answers.
- Auth + peronalization + translation working.
- Quizzes + summaries per chapter generated.
- Fully deployed URLs live and stable.
- 90-seconds demo recorded.
```

## Response snapshot

Successfully created the project constitution for the AI Native Textbook for Physical AI & Humanoid Robotics. The constitution includes:

- Core Principles (AI-Native Education, Performance & Simplicity, Interactive Learning, RAG-Powered Intelligence, Personalization & Accessibility, Modular Architecture)
- Mission statement
- Core Development requirements
- Success Criteria
- Non Goals
- Architecture Principles
- User Stories (Prioritized)
- Constraints
- Risk & Mitigation strategies
- Definition of Done
- Governance section

Version 1.0.0 was created with all requirements from the user input incorporated.

## Outcome

- ✅ Impact: New constitution created for AI textbook project
- 🧪 Tests: N/A for documentation update
- 📁 Files: .specify/memory/constitution.md updated
- 🔁 Next prompts: Build Specification using /sp.specify
- 🧠 Reflection: All user requirements were successfully incorporated into the constitution document

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Implement feature specification based on this constitution