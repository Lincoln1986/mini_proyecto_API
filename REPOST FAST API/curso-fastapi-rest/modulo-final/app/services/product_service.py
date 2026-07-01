from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    """Capa de lógica de negocio. Usa el repositorio, no la sesión directamente."""

    def __init__(self, db: Session):
        self.repository = ProductRepository(db)

    def list_products(self):
        return self.repository.get_all()

    def get_product(self, product_id: int):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto con id {product_id} no encontrado"
            )
        return product

    def create_product(self, product_data: ProductCreate):
        return self.repository.create(product_data)

    def update_product(self, product_id: int, product_data: ProductUpdate):
        product = self.get_product(product_id)
        return self.repository.update(product, product_data)

    def delete_product(self, product_id: int):
        product = self.get_product(product_id)
        self.repository.delete(product)
        return {"message": f"Producto con id {product_id} eliminado correctamente"}
