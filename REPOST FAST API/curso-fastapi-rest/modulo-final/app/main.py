from fastapi import FastAPI

from .database import Base, engine
from .routers import products

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Inventario",
    version="1.0.0"
)

app.include_router(products.router)


@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Inventario"}