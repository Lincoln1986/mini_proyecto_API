from fastapi import FastAPI , HTTPException, status
from pydantic import BaseModel,EmailStr, Field

app = FastAPI(
    title="Mi student API",
    description="API para gestión de estudiantes",
    version="1.0"
)

class StudentCreate(BaseModel):
    name: str = Field(..., description="Nombre del estudiante")
    email: EmailStr
    program: str = Field(..., description="Registro del program que cursa el estudiante")
    active: bool
    
class Student(StudentCreate):
    id: int
    
    
students = [
    {
        "id": 1,
        "name": "Jensy Benavides",
        "email": "jensy.benavides@example.com",
        "program": "Melodías y música",
        "active": True
    },
    {
        "id": 2,
        "name": "Camilo Cuellar",
        "email": "Camilo.cuellar@example.com",
        "program": "Arquitectura",
        "active": True
    },
    {
        "id": 3,
        "name": "Diana Sanchez",
        "email": "diana.sanchez@example.com",
        "program": "Inglés",
        "active": True
    },
    {
        "id": 4,
        "name": "Daniel Moreno",
        "email": "daniel.moreno@example.com",
        "program": "Inglés",
        "active": True
    },
    {
        "id": 5,
        "name": "Sofia Niño",
        "email": "sofia.nino@example.com",
        "program": "Leyes en Colombia",
        "active": True
    }
]

@app.get("/")
def home():
    return {
            "message": "Bienvenido a mi segunda API de estudiantes",
            "endpoints": [
            "GET /students/{id} - Obtener un estudiante por su ID",
            "POST /students - Crear un nuevo estudiante",
            "GET /students?active=true - Obtener todos los estudiantes activos",
            "GET /students?active=false - Obtener todos los estudiantes inactivos"
            ]
        }


@app.get("/students/{student_id}", response_model=Student)
def get_students_by_id(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El estudiante solicitado no fue encontrado")


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student_data: StudentCreate):
    new_id = len(students) + 1
    new_student = {
        "id": new_id,
        "name": student_data.name,
        "email": student_data.email,
        "program": student_data.program,
        "active": student_data.active
    }
    students.append(new_student)
    return new_student

@app.get("/students", response_model=list[Student])
def get_students(active: bool = None):
    if active is None:
        return students
    return [student for student in students if student["active"] == active]