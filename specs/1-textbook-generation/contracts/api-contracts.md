# API Contracts: AI Native Textbook Generation

## User Authentication

### POST /api/auth/register
Register a new user
- Request: {email: string, password: string, name: string}
- Response: {user_id: string, email: string, name: string, token: string}
- Error: 400 (validation error), 409 (email already exists)

### POST /api/auth/login
Authenticate a user
- Request: {email: string, password: string}
- Response: {user_id: string, email: string, name: string, token: string}
- Error: 400 (invalid credentials), 401 (unauthorized)

### POST /api/auth/logout
Logout a user
- Request: {token: string} (in headers)
- Response: {success: boolean}
- Error: 401 (unauthorized)

## Chapter Management

### GET /api/chapters
Retrieve all textbook chapters
- Request: {token: string} (in headers, optional for public content)
- Response: {chapters: [{id: string, title: string, slug: string, chapter_number: number, content_preview: string}]}
- Error: 401 (unauthorized if private content)

### GET /api/chapters/{slug}
Retrieve a specific chapter
- Request: {token: string} (in headers, optional for public content)
- Response: {chapter: {id: string, title: string, content: string, interactive_elements: object, metadata: object}}
- Error: 401 (unauthorized if private content), 404 (chapter not found)

### GET /api/chapters/{slug}/urdu
Retrieve a specific chapter in Urdu
- Request: {token: string} (in headers, optional for public content)
- Response: {chapter: {id: string, title: string, content: string, interactive_elements: object, metadata: object}}
- Error: 401 (unauthorized if private content), 404 (chapter not found), 422 (Urdu translation not available)

## AI Chatbot

### POST /api/chat
Submit a question to the AI chatbot
- Request: {token: string} (in headers), {question: string, chapter_id: string (optional)}
- Response: {answer: string, sources: [{chapter_id: string, section: string}]}
- Error: 400 (invalid question), 401 (unauthorized), 422 (question outside textbook scope)

## User Progress

### GET /api/progress
Retrieve user's progress across all chapters
- Request: {token: string} (in headers)
- Response: {progress: [{chapter_id: string, chapter_title: string, progress_percentage: number, completed: boolean}]}
- Error: 401 (unauthorized)

### POST /api/progress/{chapter_id}
Update user's progress for a specific chapter
- Request: {token: string} (in headers), {progress_percentage: number}
- Response: {success: boolean, progress: {chapter_id: string, progress_percentage: number, completed: boolean}}
- Error: 400 (invalid progress), 401 (unauthorized), 404 (chapter not found)

## Personalization

### GET /api/user/profile
Retrieve user profile including background information
- Request: {token: string} (in headers)
- Response: {user: {id: string, email: string, name: string, background: object, preferences: object}}
- Error: 401 (unauthorized)

### PUT /api/user/profile
Update user profile including background information
- Request: {token: string} (in headers), {background: object, preferences: object}
- Response: {user: {id: string, email: string, name: string, background: object, preferences: object}}
- Error: 400 (invalid data), 401 (unauthorized)

## Learning Resources

### GET /api/chapters/{slug}/summary
Retrieve chapter summary
- Request: {token: string} (in headers)
- Response: {summary: string}
- Error: 401 (unauthorized), 404 (chapter not found)

### GET /api/chapters/{slug}/quiz
Retrieve chapter quiz
- Request: {token: string} (in headers)
- Response: {quiz: {questions: [{id: string, question: string, options: string[], type: string}]}}
- Error: 401 (unauthorized), 404 (chapter not found)

### GET /api/chapters/{slug}/booster
Retrieve learning booster for chapter
- Request: {token: string} (in headers)
- Response: {booster: {type: string, content: string}}
- Error: 401 (unauthorized), 404 (chapter not found)