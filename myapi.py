from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

# mock data (dictionary)
students = {
    1: {
        "name": "john doe",
        "age": 17,
        "year": "year 12"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")  # Route
def index():
    return {"name": "Welcome to home"}


@app.get("/get-student/{student_id}")  # Route with Path Parameter
def get_student(student_id: int = Path(None, description="The Student's ID", gt=0)):
    return students[student_id]


@app.get("/get-by-name")  # Query Parameter
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Data Not Found!"}


@app.post("/create-strudent/{student_id}")  # Post Method
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exist"}

    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")  # Put / Update Method
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student doesn't exist!"}

    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student doesn't exist!"}

    del students[student_id]
    return {"message": "Student has successfully deleted!"}
