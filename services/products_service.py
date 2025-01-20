from sqlmodel import Session, select
from models.DTO.product import ProductPatchDto, ProductRegistrationDto
from models.DB.product import Product
from utils.database import engine

def register_product(product: ProductRegistrationDto):
    newProduct = Product(
        nombre = product.name,
        precio = product.price,
        fabricante = product.made_by
    )
    with Session(engine) as session:
        session.add(newProduct)
        session.commit()
        session.refresh(newProduct)
        return newProduct

def update_product_by_id(product_id: int, new_data: ProductPatchDto):
    with Session(engine) as session:
        statement = select(Product).where(Product.id_producto == product_id)
        results = session.exec(statement)
        product = results.one()
        product.precio = new_data.price
        session.add(product)
        session.commit()
    
def delete_product_by_id(product_id: int):
    with Session(engine) as session:
        statement = select(Product).where(Product.id_producto == product_id)
        results = session.exec(statement)
        product = results.one()
        session.delete(product)
        session.commit()

def get_products():
    with Session(engine) as session:
        statement = select(Product)
        products = session.exec(statement).all()
        return products
    
def get_product_by_id(product_id: int):
    with Session(engine) as session:
        statement = select(Product).where(Product.id_producto == product_id)
        results = session.exec(statement)
        product = results.one()
        return product