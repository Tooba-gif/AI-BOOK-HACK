from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, Any
from ..utils.database import get_db
from ..middleware.auth import get_current_user
from ..services.translation_service import TranslationService

router = APIRouter()

@router.get("/{chapter_id}")
async def get_urdu_translation(
    chapter_id: int,
    current_user_id: int = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get the Urdu translation for a chapter.
    """
    translation_service = TranslationService(db)
    
    try:
        urdu_content = await translation_service.get_urdu_translation(chapter_id)
        
        if not urdu_content:
            raise HTTPException(status_code=422, detail="Urdu translation not available")
        
        return {
            "chapter_id": chapter_id,
            "content": urdu_content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting translation: {str(e)}")

@router.post("/{chapter_id}")
async def add_urdu_translation(
    chapter_id: int,
    content: str,
    current_user_id: int = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Add or update the Urdu translation for a chapter.
    This endpoint would typically be used by content administrators.
    """
    translation_service = TranslationService(db)
    
    try:
        success = await translation_service.add_translation(chapter_id, content)
        
        if not success:
            raise HTTPException(status_code=404, detail="Chapter not found")
        
        return {
            "chapter_id": chapter_id,
            "status": "success",
            "message": "Translation updated successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding translation: {str(e)}")