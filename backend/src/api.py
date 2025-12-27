from fastapi import APIRouter
from . import auth, chapters, progress, users, chat, personalization, translation

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"message": "pong"}

# Include authentication routes
router.include_router(auth.router, prefix="/auth", tags=["auth"])

# Include chapter routes
router.include_router(chapters.router, prefix="/chapters", tags=["chapters"])

# Include progress routes
router.include_router(progress.router, prefix="/progress", tags=["progress"])

# Include user routes
router.include_router(users.router, prefix="/user", tags=["user"])

# Include chat routes
router.include_router(chat.router, prefix="/chat", tags=["chat"])

# Include personalization routes
router.include_router(personalization.router, prefix="/personalization", tags=["personalization"])

# Include translation routes
router.include_router(translation.router, prefix="/translation", tags=["translation"])