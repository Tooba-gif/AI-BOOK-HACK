from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from typing import Optional
from ..models import User
from ..utils.auth import verify_password, get_password_hash
from ..utils.database import get_db

class AuthService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        result = await self.db.execute(select(User).filter(User.email == email))
        user = result.scalars().first()
        
        if not user or not verify_password(password, user.password_hash):
            return None
        return user

    async def create_user(self, email: str, password: str, name: str) -> User:
        # Check if user already exists
        result = await self.db.execute(select(User).filter(User.email == email))
        existing_user = result.scalars().first()
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists"
            )
        
        # Create new user
        hashed_password = get_password_hash(password)
        user = User(
            email=email,
            password_hash=hashed_password,
            name=name,
            role="user"
        )
        
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        
        return user

    async def get_user_by_email(self, email: str) -> Optional[User]:
        result = await self.db.execute(select(User).filter(User.email == email))
        return result.scalars().first()

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        result = await self.db.execute(select(User).filter(User.id == user_id))
        return result.scalars().first()