# Quickstart Guide: AI Native Textbook Generation

## Prerequisites
- Python 3.11+
- Node.js 18+
- Docker and Docker Compose
- Access to Neon PostgreSQL database
- Access to Qdrant vector database
- (Optional) Access to AI model API (OpenAI, etc.)

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd ai-textbook-platform
```

### 2. Set up environment variables
Copy the example environment file and update with your credentials:
```bash
cp .env.example .env
# Edit .env with your database URLs, API keys, etc.
```

### 3. Install backend dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 4. Install frontend dependencies
```bash
cd frontend
npm install
```

### 5. Set up databases
```bash
# For Neon (PostgreSQL)
# Create your Neon database and update the connection string in .env

# For Qdrant (Vector database)
# Run Qdrant using Docker
docker-compose up -d qdrant
```

### 6. Run database migrations
```bash
cd backend
python -m src.database.migrate
```

### 7. Load textbook content
```bash
cd backend
python -m src.content.load_chapters
```

### 8. Load textbook content to vector database for RAG
```bash
cd rag
python -m src.embedding.load_to_qdrant
```

## Running the Application

### Development Mode
```bash
# Terminal 1: Start backend
cd backend
python -m src.main

# Terminal 2: Start frontend
cd frontend
npm run dev

# Terminal 3: Start RAG service (if separate)
cd rag
python -m src.main
```

### Production Mode
```bash
# Using Docker Compose
docker-compose up -d
```

## Testing the Application

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

## Key Endpoints

### Frontend
- Main textbook: `http://localhost:3000`
- Chapter view: `http://localhost:3000/chapters/{chapter-slug}`
- User dashboard: `http://localhost:3000/dashboard`

### Backend API
- Health check: `GET http://localhost:8000/health`
- Chapters: `GET http://localhost:8000/api/chapters`
- Chat: `POST http://localhost:8000/api/chat`

## Troubleshooting

### Common Issues
1. **Database connection errors**: Verify your Neon and Qdrant connection strings in `.env`
2. **AI API errors**: Check your API keys and rate limits
3. **Frontend build errors**: Ensure Node.js version is 18+

### Performance
- For low-end mobile devices, consider enabling lightweight mode: `LIGHTWEIGHT_MODE=true`
- For reduced data usage: `DATA_SAVER_MODE=true`

## Next Steps
1. Customize the textbook content in the `content/` directory
2. Add more interactive elements to chapters
3. Fine-tune the RAG implementation for better accuracy
4. Implement additional personalization features