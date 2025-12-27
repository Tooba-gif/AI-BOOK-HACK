import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config.settings import settings

app = FastAPI(
    title="AI Textbook RAG Service",
    description="Retrieval-Augmented Generation service for AI textbook",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI Textbook RAG Service"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Include API routes
from .api import router as api_router
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)