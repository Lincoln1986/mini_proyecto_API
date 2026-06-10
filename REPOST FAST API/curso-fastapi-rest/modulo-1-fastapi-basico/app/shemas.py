from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0) # gt significa greater than osea que mayor o igual a 0 lo que quiere decir que el precio no puede ser negativo
    stock: int = Field(ge=0) # ge significa greater than es decir que mayor o igual a 0 lo que quiere decir que el stock no puede ser negativo
    
class ProductResponse(ProductCreate):
    id: int = Field(gt=0) # ID >0
    
class ProductUpdate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)