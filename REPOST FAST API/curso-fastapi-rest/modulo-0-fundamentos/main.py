from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Mini API de Estudiantes", description="Una API simple para gestionar la información de estudiantes", version="1.0")

students = [
    {
        "id": 1,
        "name": "Laura Gómez",
        "email": "laura.gomez@email.com",
        "program": "Análisis y Desarrollo de Software",
        "active": True
    },
    {
        "id": 2,
        "name": "Andrés Martínez",
        "email": "andres.martinez@email.com",
        "program": "Producción Multimedia",
        "active": False
    }
]

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  
    program: str
    active: bool
    
@app.get("/students/{id}", status_code=200)
def get_student(id: int):
    
    for student in students:
        if student["id"] == id:
            return student
    
    
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students", status_code=201)
def create_student(student_data: StudentCreate):
    
    new_id = students[-1]["id"] + 1 if students else 1
    
    
    new_student = student_data.dict()
    new_student["id"] = new_id
    
    
    students.append(new_student)
    
    return new_student

@app.get("/students", status_code=200)
def get_students(active: bool = Query(None)):
    
    if active is None:
        return students
    
    
    filtered_students = [s for s in students if s["active"] == active]
    return filtered_students