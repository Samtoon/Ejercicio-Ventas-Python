from pydantic import BaseModel

class ProductRegistrationDto(BaseModel):
    name: str
    price: int
    made_by: str

class ProductPatchDto(BaseModel):
    price: int