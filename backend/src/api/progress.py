from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..utils.database import get_db
from ..middleware.auth import get_current_user
from ..services.chapter_service import ChapterService

router = APIRouter()

@router.get("/")
async def get_user_progress(
    current_user_id: int = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    chapter_service = ChapterService(db)
    chapters = await chapter_service.get_all_chapters()
    
    progress_list = []
    for chapter in chapters:
        progress_data = await chapter_service.get_chapter_with_progress(chapter.slug, current_user_id)
        if progress_data:
            progress_list.append({
                "chapter_id": chapter.id,
                "chapter_title": chapter.title,
                "progress_percentage": progress_data["progress"]["progress_percentage"],
                "completed": progress_data["progress"]["completed"]
            })
    
    return {"progress": progress_list}

@router.post("/{chapter_id}")
async def update_chapter_progress(
    chapter_id: int,
    progress_percentage: int,
    current_user_id: int = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    if progress_percentage < 0 or progress_percentage > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Progress percentage must be between 0 and 100"
        )
    
    chapter_service = ChapterService(db)
    progress = await chapter_service.update_user_progress(
        current_user_id, chapter_id, progress_percentage
    )
    
    return {
        "chapter_id": chapter_id,
        "progress_percentage": progress.progress_percentage,
        "completed": progress.completed
    }