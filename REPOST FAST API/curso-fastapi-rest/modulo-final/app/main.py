from fastapi import FastAPI
from app.database.connection import Base, engine
from app.routes import product_routes

# Crea las tablas en SQLite si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Inventario v1",
    description="API para administrar un inventario básico de productos usando FastAPI, SQLAlchemy y SQLite.",
    version="1.0.0"
)

app.include_router(product_routes.router)


@app.get("/")
def root():
    return {"message": "API Inventario v1 funcionando correctamente"}
