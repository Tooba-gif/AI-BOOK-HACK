from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from .services.rag_service import RAGService

router = APIRouter()
rag_service = RAGService()

class QuestionRequest(BaseModel):
    question: str
    chapter_id: Optional[str] = None  # Optional chapter ID to limit search scope

class ContentRequest(BaseModel):
    content: str
    chapter_id: str
    section_title: str = ""
    metadata: Optional[Dict] = {}

class AnswerResponse(BaseModel):
    answer: str
    citations: List[Dict]

@router.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        result = rag_service.answer_question(request.question)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")

@router.post("/add-content")
async def add_content(request: ContentRequest):
    try:
        doc_id = rag_service.add_content_to_kb(
            request.content,
            request.chapter_id,
            request.section_title,
            request.metadata
        )
        return {"doc_id": doc_id, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding content: {str(e)}")