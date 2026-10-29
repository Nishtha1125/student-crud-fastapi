# Student CRUD API

A simple Student Management REST API built using Python and FastAPI.

## Features
- Create a student
- View all students
- View a student by ID
- Update student details
- Delete a student
- Search students by name

## Technologies Used
- Python
- FastAPI
- Uvicorn
- Pydantic

## How to Run

1. Install the required packages:

   `pip install -r requirements.txt`

2. Start the application:

   `python -m uvicorn student_crud:app --reload`

3. Open the API documentation:

   `http://127.0.0.1:8000/docs`

## Storage
Student records are stored in an in-memory list. The data resets when the application restarts.