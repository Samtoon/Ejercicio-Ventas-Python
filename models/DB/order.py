from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import TIMESTAMP, String, func
import datetime

if TYPE_CHECKING:
    from models.DB.client import Client
    from models.DB.detail import Detail

class Order(SQLModel, table = True):
    __tablename__ = "pedidos"

    id_pedido: int | None = Field(default=None, primary_key=True)
    id_cliente: str | None = Field(default=None, sa_type=String(12), foreign_key="clientes.id_cliente")
    fecha: datetime.datetime | None = Field(sa_type=TIMESTAMP, default=func.now())

    cliente: "Client" = Relationship(back_populates="pedidos")
    detalles: list["Detail"] = Relationship(back_populates="pedido")
    