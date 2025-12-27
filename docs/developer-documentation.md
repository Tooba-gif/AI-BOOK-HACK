# AI Native Textbook for Physical AI & Humanoid Robotics - Developer Documentation

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
├── docker-compose.yml       # Multi-service orchestration
├── .env.example            # Environment variables template
├── README.md               # Project overview
└── .gitignore              # Git ignore rules
```

## Architecture Overview

The application follows a microservice architecture with three main components:

1. **Backend Service**: FastAPI application handling user management, content delivery, progress tracking, and API orchestration
2. **Frontend Service**: Docusaurus-based interactive textbook interface
3. **RAG Service**: Retrieval-Augmented Generation service for the AI chatbot

## Key Components

### Backend
- **Authentication**: JWT-based authentication using Better Auth principles
- **Database**: PostgreSQL (Neon) for user data and content metadata
- **Models**: SQLAlchemy models for all entities (User, Chapter, etc.)
- **Services**: Business logic for chapters, user progress, personalization, and translation
- **API**: FastAPI endpoints following REST principles

### RAG Service
- **Embedding**: Sentence Transformers for creating vector embeddings
- **Retrieval**: Qdrant vector database for semantic search
- **Generation**: OpenAI GPT models for response generation
- **Orchestration**: RAG service combining all components

### Frontend
- **Framework**: Docusaurus for documentation-style interface
- **Components**: Interactive textbook reading, chatbot, personalization
- **State Management**: React hooks for authentication and UI state
- **API Clients**: Service modules for backend communication

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

## Environment Variables

The application requires the following environment variables:

```
# Database
DATABASE_URL=postgresql+asyncpg://user:password@db:5432/textbook

# Qdrant
QDRANT_URL=http://qdrant:6333

# AI Services
OPENAI_API_KEY=your_openai_api_key_here

# Better Auth
BETTER_AUTH_SECRET=your_secret_key_here
BETTER_AUTH_URL=http://localhost:8000

# Application
ENVIRONMENT=development
```

Copy `.env.example` to `.env` and fill in your credentials.

## Development Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your credentials
3. Install dependencies:
   - Backend: `pip install -r requirements.txt`
   - Frontend: `npm install`
4. Run with Docker Compose: `docker-compose up --build`

## Running the Application

### Development Mode
```bash
# Terminal 1: Start backend
cd backend
uvicorn src.main:app --reload

# Terminal 2: Start frontend
cd frontend
npm run dev

# Terminal 3: Start RAG service
cd rag
uvicorn src.main:app --reload
```

### Production Mode
```bash
docker-compose up -d
```

## Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm run test
```

## Deployment

- Frontend: Deploy to Vercel
- Backend: Deploy to Railway
- Vector Store: Qdrant Cloud
- Database: Neon PostgreSQL

## Troubleshooting

### Common Issues
1. **Database connection errors**: Verify your Neon and Qdrant connection strings in `.env`
2. **AI API errors**: Check your API keys and rate limits
3. **Frontend build errors**: Ensure Node.js version is 18+

### Performance
- For low-end mobile devices, consider enabling lightweight mode: `LIGHTWEIGHT_MODE=true`
- For reduced data usage: `DATA_SAVER_MODE=true`