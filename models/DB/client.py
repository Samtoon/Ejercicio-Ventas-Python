from typing import TYPE_CHECKING
from collections.abc import Sequence
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import String

if TYPE_CHECKING:
    from models.DB.order import Order

class Client(SQLModel, table=True):
    __tablename__ = "clientes"

    id_cliente: str = Field(sa_type=String(12), max_length=12, primary_key=True)
    nombres: str = Field(sa_type=String(25), max_length=25, unique = True)
    apellidos: str = Field(sa_type=String(25), max_length=25)
    email: str = Field(sa_type=String(100), max_length=100)
    celular: str = Field(sa_type=String(14), max_length=14)
    contrasena: str = Field(sa_type=String(100), max_length=100)

    pedidos: list["Order"] = Relationship(back_populates="cliente")