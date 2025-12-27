from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from ..utils.database import get_db
from ..services.auth_service import AuthService
from ..utils.auth import create_access_token
from ..models import User

router = APIRouter()

@router.post("/register")
async def register(
    email: str,
    password: str,
    name: str,
    db: AsyncSession = Depends(get_db)
):
    auth_service = AuthService(db)
    user = await auth_service.create_user(email, password, name)
    
    # Create access token
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return {
        "user_id": user.id,
        "email": user.email,
        "name": user.name,
        "token": access_token
    }

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    auth_service = AuthService(db)
    user = await auth_service.authenticate_user(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return {
        "user_id": user.id,
        "email": user.email,
        "name": user.name,
        "token": access_token
    }

@router.post("/logout")
async def logout():
    # In a real implementation, you might add the token to a blacklist
    return {"success": True}