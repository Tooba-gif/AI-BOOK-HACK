# AI Native Textbook for Physical AI & Humanoid Robotics

An interactive, AI-powered textbook platform for learning Physical AI & Humanoid Robotics.

## Features

- Interactive textbook content with multimedia elements
- AI-powered Q&A chatbot that answers questions based exclusively on textbook content
- Personalized content based on user background
- One-click Urdu translation for all content
- Auto-generated summaries, quizzes, and learning boosters

## Architecture

- **Frontend**: React/Docusaurus-based interactive textbook
- **Backend**: FastAPI service with user management and content delivery
- **RAG Service**: Retrieval-Augmented Generation service for AI chatbot
- **Database**: PostgreSQL (Neon) for user data and content metadata
- **Vector Store**: Qdrant for textbook content embeddings

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Node.js 18+
- Python 3.11+

### Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your credentials
3. Run with Docker Compose: `docker-compose up --build`

### Development

For development, run services separately:

- Backend: `cd backend && uvicorn src.main:app --reload`
- Frontend: `cd frontend && npm run dev`
- RAG: `cd rag && uvicorn src.main:app --reload`

## Project Structure

```
AI-Textbook/
├── backend/                 # FastAPI backend service
│   ├── src/
│   │   ├── models/          # Database models (User, Chapter, etc.)
│   │   ├── services/        # Business logic services
│   │   ├── api/             # API endpoints
│   │   ├── middleware/      # Authentication and other middleware
│   │   ├── utils/           # Utility functions
│   │   └── config/          # Configuration settings
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile.backend   # Backend Docker configuration
├── frontend/                # Docusaurus frontend
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── services/        # API service clients
│   │   ├── hooks/           # React hooks
│   │   └── css/             # Custom styles
│   ├── package.json         # Node.js dependencies
│   └── Dockerfile.frontend  # Frontend Docker configuration
├── rag/                     # RAG service for AI chatbot
│   ├── src/
│   │   ├── embedding/       # Text embedding functionality
│   │   ├── retrieval/       # Content retrieval from vector DB
│   │   ├── generation/      # Response generation using LLM
│   │   ├── services/        # RAG orchestration service
│   │   └── config/          # Configuration settings
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile.rag       # RAG service Docker configuration
├── specs/1-textbook-generation/
│   ├── spec.md              # Feature specification
│   ├── plan.md              # Implementation plan
│   ├── research.md          # Research findings
│   ├── data-model.md        # Data models
│   ├── quickstart.md        # Quickstart guide
│   ├── contracts/           # API contracts
│   └── tasks.md             # Task breakdown
├── docs/                    # Documentation
│   ├── developer-documentation.md
│   ├── user-guide.md
│   ├── security.md
│   └── performance.md
├── docker-compose.yml       # Multi-service orchestration
├── .env.example            # Environment variables template
└── README.md               # Project overview
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### Chapters
- `GET /api/chapters` - Get all chapters
- `GET /api/chapters/{slug}` - Get a specific chapter (with personalization)
- `GET /api/chapters/{slug}/urdu` - Get chapter in Urdu

### Progress
- `GET /api/progress` - Get user progress across all chapters
- `POST /api/progress/{chapter_id}` - Update user progress for a chapter

### Chat
- `POST /api/chat` - Ask question to AI assistant

### Personalization
- `GET /api/personalization/{chapter_id}` - Get personalized content for a chapter

### Translation
- `GET /api/translation/{chapter_id}` - Get Urdu translation for a chapter
- `POST /api/translation/{chapter_id}` - Add/update Urdu translation

### User Management
- `GET /api/user/profile` - Get user profile
- `PUT /api/user/profile` - Update user profile

## Performance Metrics

- First Contentful Paint (FCP) < 2.5 seconds on low-end mobile devices
- Time to Interactive (TTI) < 4 seconds on low-end mobile devices
- Page weight per chapter < 300KB to ensure fast loading on slow networks
- Chatbot response time: First token visible within 2 seconds
- Cold start time for the platform < 5 seconds
- Demo ready within 90 seconds of deployment

## Security Features

- JWT-based authentication with configurable expiration
- Passwords hashed using bcrypt
- Rate limiting to prevent abuse
- Input validation and sanitization
- API keys stored securely in environment variables
- Content filtering for AI responses

## Documentation

- [Developer Documentation](./docs/developer-documentation.md) - Technical details for developers
- [User Guide](./docs/user-guide.md) - Guide for using the platform
- [Security Guidelines](./docs/security.md) - Security measures and best practices
- [Performance Optimization](./docs/performance.md) - Performance strategies and metrics

## Deployment

- Frontend: Deploy to Vercel
- Backend: Deploy to Railway
- Vector Store: Qdrant Cloud
- Database: Neon PostgreSQL

## Contributing

See the specifications in `specs/1-textbook-generation/` for detailed requirements and implementation tasks.

## License

[To be defined]