from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..utils.database import get_db
from ..services.chapter_service import ChapterService
from ..models import Chapter
from ..middleware.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[dict])
async def get_chapters(
    db: AsyncSession = Depends(get_db)
):
    chapter_service = ChapterService(db)
    chapters = await chapter_service.get_all_chapters()

    # Return a simplified representation of chapters
    return [
        {
            "id": chapter.id,
            "title": chapter.title,
            "slug": chapter.slug,
            "chapter_number": chapter.chapter_number,
            "content_preview": chapter.content[:100] + "..." if len(chapter.content) > 100 else chapter.content
        }
        for chapter in chapters
    ]

@router.get("/{slug}", response_model=dict)
async def get_chapter(
    slug: str,
    current_user_id: int = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    chapter_service = ChapterService(db)
    # Use the personalization method if user is authenticated
    result = await chapter_service.get_chapter_with_personalization(slug, current_user_id)

    if not result:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Chapter not found")

    return {
        "id": result["chapter"]["id"],
        "title": result["chapter"]["title"],
        "content": result["chapter"]["content"],
        "interactive_elements": result["chapter"]["interactive_elements"],
        "metadata": result["chapter"]["metadata"]
    }

@router.get("/{slug}/urdu", response_model=dict)
async def get_chapter_urdu(
    slug: str,
    current_user_id: int = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    chapter_service = ChapterService(db)
    chapter = await chapter_service.get_chapter_by_slug(slug)

    if not chapter:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Chapter not found")

    if not chapter.content_urdu:
        from fastapi import HTTPException
        raise HTTPException(status_code=422, detail="Urdu translation not available")

    # Apply personalization to Urdu content as well
    result = await chapter_service.get_chapter_with_personalization(slug, current_user_id)
    if not result:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Chapter not found")

    # Use Urdu content but with personalization applied
    content = chapter.content_urdu
    # Note: In a real implementation, personalization would be applied to the Urdu content
    # For now, we'll return the original Urdu content

    return {
        "id": result["chapter"]["id"],
        "title": result["chapter"]["title"],
        "content": content,
        "interactive_elements": result["chapter"]["interactive_elements"],
        "metadata": result["chapter"]["metadata"]
    }