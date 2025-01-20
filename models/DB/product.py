from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import String

if TYPE_CHECKING:
    from models.DB.detail import Detail

class Product(SQLModel, table = True):
    __tablename__ = "productos"

    id_producto: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(sa_type=String(45), max_length=45)
    precio: int
    fabricante: str = Field(sa_type=String(45), max_length=45)

    detalles: list["Detail"] = Relationship(back_populates = "producto")

