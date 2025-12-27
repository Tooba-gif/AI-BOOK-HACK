# Data Model: AI Native Textbook Generation

## User Entity
- **Fields**:
  - id: UUID (Primary Key)
  - email: String (Unique, Required)
  - password_hash: String (Required)
  - name: String
  - background: JSON (User's technical background information)
  - preferences: JSON (Language, accessibility settings, etc.)
  - created_at: DateTime
  - updated_at: DateTime
  - role: String (Enum: 'user', 'admin')

- **Relationships**:
  - One-to-Many: User -> UserProgress
  - One-to-Many: User -> UserInteraction

- **Validation rules**:
  - Email must be valid email format
  - Password must meet security requirements
  - Role must be either 'user' or 'admin'

## Chapter Entity
- **Fields**:
  - id: UUID (Primary Key)
  - title: String (Required)
  - content: Text (Required, Markdown format)
  - content_urdu: Text (Optional, Urdu translation)
  - slug: String (Required, URL-friendly)
  - chapter_number: Integer (Required, for ordering)
  - interactive_elements: JSON (Embedded interactive components)
  - metadata: JSON (Additional content metadata)
  - created_at: DateTime
  - updated_at: DateTime

- **Relationships**:
  - One-to-Many: Chapter -> UserProgress
  - One-to-Many: Chapter -> ChapterInteraction

- **Validation rules**:
  - Title and content must not be empty
  - Chapter number must be unique within textbook
  - Slug must be URL-friendly and unique

## Question Entity
- **Fields**:
  - id: UUID (Primary Key)
  - user_id: UUID (Foreign Key to User)
  - chapter_id: UUID (Foreign Key to Chapter, Optional)
  - question_text: Text (Required)
  - answer_text: Text (Required, AI-generated)
  - sources: JSON (Citation information from textbook)
  - created_at: DateTime
  - updated_at: DateTime

- **Relationships**:
  - Many-to-One: Question -> User
  - Many-to-One: Question -> Chapter (Optional)

- **Validation rules**:
  - Question text must not be empty
  - Answer text must not be empty
  - Sources must be properly formatted citation data

## UserProgress Entity
- **Fields**:
  - id: UUID (Primary Key)
  - user_id: UUID (Foreign Key to User)
  - chapter_id: UUID (Foreign Key to Chapter)
  - progress_percentage: Float (0-100)
  - completed: Boolean
  - time_spent: Integer (in seconds)
  - last_accessed: DateTime
  - created_at: DateTime
  - updated_at: DateTime

- **Relationships**:
  - Many-to-One: UserProgress -> User
  - Many-to-One: UserProgress -> Chapter

- **Validation rules**:
  - Progress percentage must be between 0 and 100
  - User and chapter combination must be unique

## ChapterInteraction Entity
- **Fields**:
  - id: UUID (Primary Key)
  - user_id: UUID (Foreign Key to User)
  - chapter_id: UUID (Foreign Key to Chapter)
  - interaction_type: String (Enum: 'click', 'hover', 'complete', 'quiz', 'summary')
  - interaction_data: JSON (Additional data about the interaction)
  - created_at: DateTime

- **Relationships**:
  - Many-to-One: ChapterInteraction -> User
  - Many-to-One: ChapterInteraction -> Chapter

- **Validation rules**:
  - Interaction type must be one of the allowed values
  - Interaction data must be valid JSON

## LearningResource Entity
- **Fields**:
  - id: UUID (Primary Key)
  - chapter_id: UUID (Foreign Key to Chapter)
  - resource_type: String (Enum: 'summary', 'quiz', 'booster')
  - content: Text (Required)
  - content_urdu: Text (Optional, Urdu translation)
  - metadata: JSON (Additional resource metadata)
  - created_at: DateTime
  - updated_at: DateTime

- **Relationships**:
  - Many-to-One: LearningResource -> Chapter

- **Validation rules**:
  - Resource type must be one of the allowed values
  - Content must not be empty