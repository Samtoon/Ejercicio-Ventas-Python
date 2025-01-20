from fastapi import APIRouter
from models.DTO.product import ProductRegistrationDto, ProductPatchDto
from services import products_service

router = APIRouter(
    prefix="/products"
)

@router.get("/")
async def get_products():
    products = products_service.get_products()
    return products

@router.get("/{product_id}")
async def get_product_by_id(product_id: int):
    product = products_service.get_product_by_id(product_id)
    return product

@router.post("/")
async def register_product(product: ProductRegistrationDto):
    newProduct = products_service.register_product(product)
    return newProduct

@router.patch("/{product_id}")
async def patch_product_price_by_id(product_id: int, product: ProductPatchDto):
    products_service.update_product_by_id(product_id, product)
    return product

@router.delete("/{product_id}")
async def delete_product_by_id(product_id: int):
    products_service.delete_product_by_id(product_id)
    return f"El producto {product_id} ha sido eliminado exitosamente"