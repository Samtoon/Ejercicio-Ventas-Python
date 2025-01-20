from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import ForeignKeyConstraint

if TYPE_CHECKING:
    from models.DB.order import Order
    from models.DB.product import Product

class Detail(SQLModel, table = True):
    __tablename__ = "detalles"

    id_producto: int | None = Field(default=None, primary_key = True, foreign_key = "productos.id_producto")
    id_pedido: int | None = Field(default = None, primary_key = True, foreign_key = "pedidos.id_pedido")
    cantidad: int

    pedido: "Order" = Relationship(back_populates = "detalles")
    producto: "Product" = Relationship(back_populates = "detalles")


