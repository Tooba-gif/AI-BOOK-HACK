from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, Any
from ..utils.database import get_db
from ..middleware.auth import get_current_user
from ..services.personalization_service import PersonalizationService

router = APIRouter()

@router.get("/{chapter_id}")
async def get_personalized_chapter(
    chapter_id: int,
    current_user_id: int = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get a chapter with content personalized based on user's background.
    """
    personalization_service = PersonalizationService(db)
    
    try:
        personalized_content = await personalization_service.get_personalized_content(
            current_user_id, 
            chapter_id
        )
        
        if not personalized_content:
            raise HTTPException(status_code=404, detail="Chapter not found")
        
        return personalized_content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting personalized content: {str(e)}")