from pydantic import BaseModel, Field, ConfigDict


class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, description="Nombre del producto, mínimo 3 caracteres")
    price: float = Field(..., gt=0, description="Precio del producto, debe ser mayor que 0")
    stock: int = Field(..., ge=0, description="Cantidad en stock, debe ser mayor o igual que 0")
    category: str = Field(..., min_length=3, description="Categoría del producto, mínimo 3 caracteres")


class ProductCreate(ProductBase):
    """Esquema usado para crear un producto."""
    pass


class ProductUpdate(ProductBase):
    """Esquema usado para actualizar un producto (PUT completo)."""
    pass


class ProductResponse(ProductBase):
    """Esquema usado para devolver un producto al cliente."""
    id: int

    model_config = ConfigDict(from_attributes=True)
