from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String)
    background = Column(JSON)  # User's technical background information
    preferences = Column(JSON)  # Language, accessibility settings, etc.
    role = Column(String, default="user")  # 'user' or 'admin'
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    progress = relationship("UserProgress", back_populates="user")
    interactions = relationship("ChapterInteraction", back_populates="user")
    questions = relationship("Question", back_populates="user")


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)  # Markdown format
    content_urdu = Column(Text)  # Optional Urdu translation
    slug = Column(String, unique=True, nullable=False)  # URL-friendly
    chapter_number = Column(Integer, nullable=False)  # For ordering
    interactive_elements = Column(JSON)  # Embedded interactive components
    content_metadata = Column(JSON)  # Additional content metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    progress = relationship("UserProgress", back_populates="chapter")
    interactions = relationship("ChapterInteraction", back_populates="chapter")
    learning_resources = relationship("LearningResource", back_populates="chapter")
    questions = relationship("Question", back_populates="chapter")


class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)
    progress_percentage = Column(Integer, default=0)  # 0-100
    completed = Column(Boolean, default=False)
    time_spent = Column(Integer, default=0)  # in seconds
    last_accessed = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="progress")
    chapter = relationship("Chapter", back_populates="progress")


class ChapterInteraction(Base):
    __tablename__ = "chapter_interactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)
    interaction_type = Column(String, nullable=False)  # 'click', 'hover', 'complete', 'quiz', 'summary'
    interaction_data = Column(JSON)  # Additional data about the interaction
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="interactions")
    chapter = relationship("Chapter", back_populates="interactions")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    chapter_id = Column(Integer, ForeignKey("chapters.id"))  # Optional
    question_text = Column(Text, nullable=False)
    answer_text = Column(Text, nullable=False)
    sources = Column(JSON)  # Citation information from textbook
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="questions")
    chapter = relationship("Chapter", back_populates="questions")


class LearningResource(Base):
    __tablename__ = "learning_resources"

    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)
    resource_type = Column(String, nullable=False)  # 'summary', 'quiz', 'booster'
    content = Column(Text, nullable=False)
    content_urdu = Column(Text)  # Optional Urdu translation
    resource_metadata = Column(JSON)  # Additional resource metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    chapter = relationship("Chapter", back_populates="learning_resources")