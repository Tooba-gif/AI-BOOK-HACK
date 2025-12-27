from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import func
from typing import List, Optional
from ..models import Chapter, UserProgress, ChapterInteraction, User
from ..utils.database import get_db
from .personalization_service import PersonalizationService

class ChapterService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_chapters(self) -> List[Chapter]:
        result = await self.db.execute(select(Chapter).order_by(Chapter.chapter_number))
        return result.scalars().all()

    async def get_chapter_by_slug(self, slug: str) -> Chapter:
        result = await self.db.execute(select(Chapter).filter(Chapter.slug == slug))
        return result.scalars().first()

    async def get_chapter_by_id(self, chapter_id: int) -> Chapter:
        result = await self.db.execute(select(Chapter).filter(Chapter.id == chapter_id))
        return result.scalars().first()

    async def get_chapter_with_progress(self, slug: str, user_id: int) -> dict:
        """Get chapter content with user's progress information"""
        chapter = await self.get_chapter_by_slug(slug)
        if not chapter:
            return None

        # Get user's progress for this chapter
        progress_result = await self.db.execute(
            select(UserProgress).filter(
                UserProgress.chapter_id == chapter.id,
                UserProgress.user_id == user_id
            )
        )
        progress = progress_result.scalars().first()

        return {
            "chapter": {
                "id": chapter.id,
                "title": chapter.title,
                "content": chapter.content,
                "interactive_elements": chapter.interactive_elements,
                "metadata": chapter.metadata
            },
            "progress": {
                "progress_percentage": progress.progress_percentage if progress else 0,
                "completed": progress.completed if progress else False,
                "time_spent": progress.time_spent if progress else 0
            } if progress else {
                "progress_percentage": 0,
                "completed": False,
                "time_spent": 0
            }
        }

    async def get_chapter_with_personalization(self, slug: str, user_id: int) -> dict:
        """Get chapter content with user's progress and personalization information"""
        chapter = await self.get_chapter_by_slug(slug)
        if not chapter:
            return None

        # Get user's progress for this chapter
        progress_result = await self.db.execute(
            select(UserProgress).filter(
                UserProgress.chapter_id == chapter.id,
                UserProgress.user_id == user_id
            )
        )
        progress = progress_result.scalars().first()

        # Get user's background for personalization
        user_result = await self.db.execute(
            select(User).filter(User.id == user_id)
        )
        user = user_result.scalars().first()

        # Apply personalization if user has background information
        content = chapter.content
        if user and user.background:
            personalization_service = PersonalizationService(self.db)
            personalized_data = await personalization_service.get_personalized_content(user_id, chapter.id)
            content = personalized_data.get("content", content)

        return {
            "chapter": {
                "id": chapter.id,
                "title": chapter.title,
                "content": content,
                "interactive_elements": chapter.interactive_elements,
                "metadata": chapter.metadata
            },
            "progress": {
                "progress_percentage": progress.progress_percentage if progress else 0,
                "completed": progress.completed if progress else False,
                "time_spent": progress.time_spent if progress else 0
            } if progress else {
                "progress_percentage": 0,
                "completed": False,
                "time_spent": 0
            }
        }

    async def update_user_progress(self, user_id: int, chapter_id: int, progress_percentage: int) -> UserProgress:
        """Update or create user progress for a chapter"""
        # Check if progress record already exists
        result = await self.db.execute(
            select(UserProgress).filter(
                UserProgress.user_id == user_id,
                UserProgress.chapter_id == chapter_id
            )
        )
        progress = result.scalars().first()

        if progress:
            # Update existing progress
            progress.progress_percentage = progress_percentage
            progress.completed = progress_percentage >= 100
            progress.updated_at = func.now()
        else:
            # Create new progress record
            progress = UserProgress(
                user_id=user_id,
                chapter_id=chapter_id,
                progress_percentage=progress_percentage,
                completed=progress_percentage >= 100
            )
            self.db.add(progress)

        await self.db.commit()
        await self.db.refresh(progress)
        return progress

    async def record_interaction(self, user_id: int, chapter_id: int, interaction_type: str, interaction_data: dict = None) -> ChapterInteraction:
        """Record a user interaction with a chapter"""
        interaction = ChapterInteraction(
            user_id=user_id,
            chapter_id=chapter_id,
            interaction_type=interaction_type,
            interaction_data=interaction_data or {}
        )
        self.db.add(interaction)
        await self.db.commit()
        await self.db.refresh(interaction)
        return interaction