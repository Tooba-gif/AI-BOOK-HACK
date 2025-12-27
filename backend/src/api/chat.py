from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Optional
import httpx
from ..utils.database import get_db
from ..middleware.auth import get_current_user
from ..models import Question, Chapter
from ..utils.logging import logger

router = APIRouter()

class ChatRequest(BaseModel):
    question: str
    chapter_id: Optional[int] = None  # Optional chapter ID to limit search scope

class ChatResponse(BaseModel):
    answer: str
    sources: List[Dict]

@router.post("/", response_model=ChatResponse)
async def chat_with_bot(
    request: ChatRequest,
    current_user_id: int = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    try:
        # Prepare request to RAG service
        rag_payload = {
            "question": request.question
        }

        if request.chapter_id:
            rag_payload["chapter_id"] = str(request.chapter_id)

        # Call the RAG service
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://rag:8001/api/ask",  # Using service name from docker-compose
                json=rag_payload,
                timeout=30.0
            )

        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error communicating with RAG service"
            )

        rag_result = response.json()

        # Save the question and answer to the database
        from sqlalchemy.future import select
        chapter = None
        if request.chapter_id:
            result = await db.execute(select(Chapter).filter(Chapter.id == request.chapter_id))
            chapter = result.scalars().first()

        question_record = Question(
            user_id=current_user_id,
            chapter_id=chapter.id if chapter else None,
            question_text=request.question,
            answer_text=rag_result["answer"],
            sources=rag_result["citations"]
        )

        db.add(question_record)
        await db.commit()
        await db.refresh(question_record)

        logger.info(f"Question answered for user {current_user_id}: {request.question[:50]}...")

        return ChatResponse(
            answer=rag_result["answer"],
            sources=rag_result["citations"]
        )
    except httpx.RequestError as e:
        logger.error(f"Error calling RAG service: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error communicating with AI service"
        )
    except Exception as e:
        logger.error(f"Unexpected error in chat endpoint: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )