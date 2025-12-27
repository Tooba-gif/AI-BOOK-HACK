import os
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Database settings
    database_url: str = Field(default="postgresql+asyncpg://user:password@localhost:5432/textbook", env="DATABASE_URL")

    # Qdrant settings
    qdrant_url: str = Field(default="http://localhost:6333", env="QDRANT_URL")

    # OpenAI settings
    openai_api_key: str = Field(default="", env="OPENAI_API_KEY")

    # Auth settings
    secret_key: str = Field(default="your-secret-key-here", env="BETTER_AUTH_SECRET")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Application settings
    environment: str = Field(default="development", env="ENVIRONMENT")

    class Config:
        env_file = ".env"

settings = Settings()