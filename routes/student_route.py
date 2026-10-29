
from fastapi import APIRouter, Response, status
from models.student_model import Student, StudentCreate

from controller.student_controller import (
    get_students_all_controller,
    create_student_controller,
    get_student_controller,
    update_student_controller,
    delete_student_controller,
    search_student_controller # for bonus challenge
)

router = APIRouter(prefix="/students", tags=["Students"])


# Create student
@router.post("/", response_model=Student, status_code=201)
def create_student(student: StudentCreate):
    return create_student_controller(student)


# Get all students
@router.get("/", response_model=list[Student])
def get_all_students():
    return get_students_all_controller()


# Search students by name -- bonus challenge
@router.get("/search/")
def search_student(name: str):
    return search_student_controller(name)

# Get student by ID
@router.get("/{studentid}", response_model=Student)
def get_student(studentid: int):
    return get_student_controller(studentid)


# Update student
@router.put("/{studentid}", response_model=Student)
def update_student(studentid: int, student: StudentCreate):
    return update_student_controller(studentid, student)


# Delete student
@router.delete("/{studentid}", status_code=204)
def delete_student(studentid: int):
    delete_student_controller(studentid)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
