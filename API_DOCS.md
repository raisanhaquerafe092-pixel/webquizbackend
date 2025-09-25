# Quiz Web App Backend API Documentation

## Overview
This Django REST Framework backend provides APIs for managing quiz questions, study materials, and educational content.

## Base URL
```
http://localhost:8000/
```

## API Endpoints

### MCQ Questions
- **GET** `/mcq/question/` - List all MCQ questions
- **POST** `/mcq/question/` - Create new MCQ question
- **GET** `/mcq/question/{id}/` - Get specific MCQ question
- **PUT** `/mcq/question/{id}/` - Update MCQ question
- **DELETE** `/mcq/question/{id}/` - Delete MCQ question

**Query Parameters:**
- `class_name` - Filter by class name
- `subject` - Filter by subject

**Example Request:**
```
GET /mcq/question/?class_name=nine&subject=math
```

### Short Questions
- **GET** `/short/question/` - List all short questions
- **POST** `/short/question/` - Create new short question
- **GET** `/short/question/{id}/` - Get specific short question
- **PUT** `/short/question/{id}/` - Update short question
- **DELETE** `/short/question/{id}/` - Delete short question

### Long Questions
- **GET** `/long/question/` - List all long questions
- **POST** `/long/question/` - Create new long question
- **GET** `/long/question/{id}/` - Get specific long question
- **PUT** `/long/question/{id}/` - Update long question
- **DELETE** `/long/question/{id}/` - Delete long question

### Chapters/Content
- **GET** `/content/chapter/` - List all chapters
- **POST** `/content/chapter/` - Create new chapter
- **GET** `/content/chapter/{id}/` - Get specific chapter
- **PUT** `/content/chapter/{id}/` - Update chapter
- **DELETE** `/content/chapter/{id}/` - Delete chapter

**Query Parameters:**
- `class_name` - Filter by class name
- `subject` - Filter by subject

## Data Models

### MCQ Model
```json
{
  "id": 1,
  "class_name": "nine",
  "subject": "math",
  "question": "What is 2 + 2?",
  "option1": "3",
  "option2": "4",
  "option3": "5", 
  "option4": "6",
  "correct_option": 2
}
```

### Chapter Model
```json
{
  "id": 1,
  "class_name": "nine",
  "subject": "math",
  "title": "Basic Arithmetic",
  "index": 1,
  "content": "This chapter covers basic arithmetic operations..."
}
```

## Authentication
Currently, no authentication is required for API access. This is suitable for development but should be secured for production.

## CORS Settings
CORS is enabled for all origins in development. Configure properly for production.

## Error Responses
The API returns standard HTTP status codes:
- 200: Success
- 201: Created
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create superuser:
```bash
python manage.py createsuperuser
```

4. Start server:
```bash
python manage.py runserver
```

5. Access admin panel: http://localhost:8000/admin/
6. API root: http://localhost:8000/mcq/question/

## Sample Data
You can add sample data through the Django admin interface or by making POST requests to the API endpoints.