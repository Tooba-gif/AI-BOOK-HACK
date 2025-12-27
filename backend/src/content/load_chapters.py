"""
Content loader for AI Native Textbook Generation
This script loads textbook content into the database
"""
import asyncio
import sys
import os
from datetime import datetime

# Add the src directory to the path so we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from ..models import Chapter, User, LearningResource, Base
from ..config.settings import settings
from ..utils.database import get_db


# Sample textbook content for Physical AI & Humanoid Robotics
CHAPTERS_CONTENT = [
    {
        "chapter_number": 1,
        "title": "Introduction to Physical AI & Humanoid Robotics",
        "slug": "introduction-to-physical-ai",
        "content": """# Chapter 1: Introduction to Physical AI & Humanoid Robotics

## What is Physical AI?

Physical AI refers to the intersection of artificial intelligence and physical systems. Unlike traditional AI that operates in digital spaces, Physical AI works with real-world environments and objects.

## Humanoid Robotics

Humanoid robots are robots with human-like features. They are designed to interact with human environments and potentially assist humans in various tasks.

## Interactive Elements

This textbook includes interactive elements to enhance your learning:

- Click on highlighted terms for definitions
- Use the chatbot to ask questions about the content
- Personalize content based on your background

## Summary

This chapter introduced the fundamental concepts of Physical AI and Humanoid Robotics. Continue to the next chapter to explore more advanced topics.""",
        "interactive_elements": [
            {
                "type": "definition",
                "term": "Physical AI",
                "definition": "AI systems that interact with and operate in the physical world"
            },
            {
                "type": "definition", 
                "term": "Humanoid Robotics",
                "definition": "Robots with human-like features designed to interact with human environments"
            }
        ],
        "content_metadata": {
            "tags": ["introduction", "physical-ai", "humanoid-robotics"],
            "difficulty": "beginner",
            "estimated_reading_time": 5
        }
    },
    {
        "chapter_number": 2,
        "title": "History and Evolution of Humanoid Robots",
        "slug": "history-evolution-humanoid-robots",
        "content": """# Chapter 2: History and Evolution of Humanoid Robots

## Early Developments

The concept of humanoid robots has fascinated humans for centuries. Early mechanical automata in the 18th century laid the groundwork for modern robotics.

## Modern Era

The 20th century saw significant advances with robots like WABOT-1 from Waseda University in 1972, considered one of the first full-scale anthropomorphic robots.

## Recent Innovations

Today's humanoid robots like Boston Dynamics' Atlas and SoftBank's Pepper showcase remarkable capabilities in mobility and interaction.

## Summary

This chapter traced the development of humanoid robotics from early concepts to modern implementations.""",
        "interactive_elements": [
            {
                "type": "definition",
                "term": "WABOT-1",
                "definition": "The first full-scale anthropomorphic robot, developed at Waseda University in 1972"
            },
            {
                "type": "quiz",
                "question": "Which robot is considered the first full-scale anthropomorphic robot?",
                "options": ["Atlas", "Pepper", "WABOT-1", "ASIMO"],
                "answer": "WABOT-1"
            }
        ],
        "content_metadata": {
            "tags": ["history", "humanoid-robots", "evolution"],
            "difficulty": "beginner",
            "estimated_reading_time": 7
        }
    },
    {
        "chapter_number": 3,
        "title": "Sensors and Perception in Physical AI",
        "slug": "sensors-perception-physical-ai",
        "content": """# Chapter 3: Sensors and Perception in Physical AI

## Types of Sensors

Physical AI systems rely on various sensors to perceive their environment:

- Visual sensors (cameras, LIDAR)
- Tactile sensors (force, pressure, temperature)
- Proprioceptive sensors (position, acceleration, orientation)

## Sensor Fusion

Modern Physical AI systems combine data from multiple sensors to form a comprehensive understanding of their environment.

## Computer Vision

Visual perception is crucial for humanoid robots to recognize objects, people, and navigate spaces.

## Summary

This chapter covered the essential role of sensors in enabling Physical AI systems to perceive and interact with their environment.""",
        "interactive_elements": [
            {
                "type": "interactive_diagram",
                "title": "Humanoid Robot Sensor Layout",
                "description": "Explore the placement of different sensors on a humanoid robot"
            }
        ],
        "content_metadata": {
            "tags": ["sensors", "perception", "computer-vision"],
            "difficulty": "intermediate",
            "estimated_reading_time": 8
        }
    },
    {
        "chapter_number": 4,
        "title": "Actuators and Movement Systems",
        "slug": "actuators-movement-systems",
        "content": """# Chapter 4: Actuators and Movement Systems

## Types of Actuators

Humanoid robots use various actuator types for movement:

- Servo motors for precise joint control
- Hydraulic systems for high power applications
- Pneumatic systems for lightweight solutions

## Balance and Locomotion

Maintaining balance and achieving stable walking is one of the greatest challenges in humanoid robotics.

## Control Systems

Advanced control algorithms coordinate multiple actuators to achieve human-like movement.

## Summary

This chapter explored the mechanical systems that enable humanoid robots to move and interact with their environment.""",
        "interactive_elements": [
            {
                "type": "simulation",
                "title": "Walking Gait Simulation",
                "description": "Visualize how humanoid robots achieve stable walking"
            }
        ],
        "content_metadata": {
            "tags": ["actuators", "movement", "locomotion", "balance"],
            "difficulty": "intermediate",
            "estimated_reading_time": 9
        }
    },
    {
        "chapter_number": 5,
        "title": "Artificial Intelligence for Humanoid Robots",
        "slug": "ai-humanoid-robots",
        "content": """# Chapter 5: Artificial Intelligence for Humanoid Robots

## Machine Learning in Robotics

Modern humanoid robots use machine learning to adapt to new situations and improve performance over time.

## Natural Language Processing

Communication with humans requires sophisticated NLP systems for understanding and generating human language.

## Decision Making

AI systems must make real-time decisions based on sensor data and goals.

## Summary

This chapter examined the AI systems that enable humanoid robots to function intelligently in human environments.""",
        "interactive_elements": [
            {
                "type": "chat_simulation",
                "title": "Human-Robot Conversation",
                "description": "Experience a simulated conversation with a humanoid robot"
            }
        ],
        "content_metadata": {
            "tags": ["ai", "machine-learning", "nlp", "decision-making"],
            "difficulty": "intermediate",
            "estimated_reading_time": 10
        }
    },
    {
        "chapter_number": 6,
        "title": "Human-Robot Interaction",
        "slug": "human-robot-interaction",
        "content": """# Chapter 6: Human-Robot Interaction

## Social Robotics

Humanoid robots must understand social cues and norms to interact effectively with humans.

## Communication Modalities

Effective interaction combines speech, gestures, facial expressions, and body language.

## Trust and Acceptance

Building trust between humans and robots is essential for successful interaction.

## Applications

Humanoid robots are finding applications in healthcare, education, customer service, and companionship.

## Summary

This chapter explored the principles of effective human-robot interaction and important application areas.""",
        "interactive_elements": [
            {
                "type": "scenario",
                "title": "Healthcare Assistance",
                "description": "Experience how a humanoid robot might assist in a healthcare setting"
            }
        ],
        "content_metadata": {
            "tags": ["hri", "social-robotics", "communication", "applications"],
            "difficulty": "intermediate",
            "estimated_reading_time": 8
        }
    },
    {
        "chapter_number": 7,
        "title": "Ethics and Safety in Physical AI",
        "slug": "ethics-safety-physical-ai",
        "content": """# Chapter 7: Ethics and Safety in Physical AI

## Safety Considerations

Physical AI systems must operate safely around humans, requiring robust safety mechanisms and fail-safes.

## Ethical Implications

The deployment of humanoid robots raises important ethical questions about employment, privacy, and human relationships.

## Regulatory Framework

Standards and regulations are evolving to address the unique challenges of physical AI systems.

## Future Considerations

As Physical AI becomes more sophisticated, ongoing ethical evaluation will be essential.

## Summary

This chapter addressed the critical safety and ethical considerations in developing and deploying Physical AI systems.""",
        "interactive_elements": [
            {
                "type": "ethics_case_study",
                "title": "Autonomous Decision Making",
                "description": "Explore ethical dilemmas in autonomous robot decision making"
            }
        ],
        "content_metadata": {
            "tags": ["ethics", "safety", "regulations", "privacy"],
            "difficulty": "advanced",
            "estimated_reading_time": 10
        }
    },
    {
        "chapter_number": 8,
        "title": "Future of Physical AI and Humanoid Robotics",
        "slug": "future-physical-ai-humanoid-robotics",
        "content": """# Chapter 8: Future of Physical AI and Humanoid Robotics

## Emerging Technologies

New developments in materials science, AI, and manufacturing are driving advances in humanoid robotics.

## Societal Impact

Humanoid robots will increasingly become part of our daily lives, changing how we work and live.

## Research Challenges

Significant technical challenges remain in areas like dexterity, general intelligence, and energy efficiency.

## Conclusion

The field of Physical AI and Humanoid Robotics is rapidly evolving, with the potential to transform human society. Continued research and responsible development will be key to realizing the benefits while addressing the challenges.

## Final Summary

This textbook has provided an introduction to Physical AI and Humanoid Robotics, covering history, technology, interaction, ethics, and future directions. The field continues to evolve rapidly, offering exciting opportunities for researchers and practitioners.""",
        "interactive_elements": [
            {
                "type": "future_vision",
                "title": "2030 Scenario",
                "description": "Visualize a future where humanoid robots are integrated into daily life"
            }
        ],
        "content_metadata": {
            "tags": ["future", "emerging-tech", "societal-impact", "research"],
            "difficulty": "beginner",
            "estimated_reading_time": 8
        }
    }
]


async def load_chapters():
    """Load textbook chapters into the database"""
    print("Loading textbook content...")
    
    # Create async engine
    engine = create_async_engine(settings.database_url)
    
    # Create tables if they don't exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Get database session
    async for db in get_db():
        # Check if chapters already exist
        existing_chapters = await db.execute(select(Chapter))
        existing_chapters = existing_chapters.scalars().all()
        
        if existing_chapters:
            print(f"Found {len(existing_chapters)} existing chapters. Skipping content loading.")
            return
        
        # Add chapters to the database
        for chapter_data in CHAPTERS_CONTENT:
            chapter = Chapter(
                chapter_number=chapter_data["chapter_number"],
                title=chapter_data["title"],
                slug=chapter_data["slug"],
                content=chapter_data["content"],
                content_urdu=None,  # Will be populated by translation service
                interactive_elements=chapter_data["interactive_elements"],
                content_metadata=chapter_data["content_metadata"],
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            db.add(chapter)
        
        await db.commit()
        print(f"Successfully loaded {len(CHAPTERS_CONTENT)} chapters into the database.")
        
        # Create a default user if one doesn't exist
        default_user = await db.execute(select(User).where(User.email == "admin@example.com"))
        default_user = default_user.scalars().first()
        
        if not default_user:
            from ..models import User
            from ..utils.auth import get_password_hash
            default_user = User(
                email="admin@example.com",
                password_hash=get_password_hash("admin123"),
                name="Admin User",
                role="admin",
                background=None,
                preferences={"language": "en", "background": "general"}
            )
            db.add(default_user)
            await db.commit()
            print("Created default admin user: admin@example.com / admin123")


if __name__ == "__main__":
    asyncio.run(load_chapters())