from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..utils.database import get_db
from ..middleware.auth import get_current_user
from ..models import User

router = APIRouter()

@router.get("/profile")
async def get_user_profile(
    current_user_id: int = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).filter(User.id == current_user_id))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "background": user.background,
        "preferences": user.preferences
    }

@router.put("/profile")
async def update_user_profile(
    background: dict = None,
    preferences: dict = None,
    current_user_id: int = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).filter(User.id == current_user_id))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if background is not None:
        user.background = background
    if preferences is not None:
        user.preferences = preferences
    
    await db.commit()
    await db.refresh(user)
    
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "background": user.background,
        "preferences": user.preferences
    }