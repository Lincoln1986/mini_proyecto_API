from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
app = FastAPI(title="Mi API con FastAPI", description="Esta es una API de ejemplo para FastAPI", version="1.0.0")

class EchoRequest(BaseModel):
    message: str = Field(..., example="Hola, FastAPI!")
    
@app.get("/")
def root () -> dict:
    return {"message": "¡Walcome a mi apei!"}

@app.get("health/")
def health_check() -> dict:
    return {"status": "Healthy"}

@app.post("/echo/")
def echo(request: EchoRequest) -> dict:
    return {"echo": request.message}

@app.get("great/{name}")
def greet(name: str) -> dict:
    return {"message": f"¡Hola, {name}! ¿Cómo estás?"}