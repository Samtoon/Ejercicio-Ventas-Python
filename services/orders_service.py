from collections.abc import Sequence
from datetime import datetime
from functools import reduce
from typing import Optional
from sqlalchemy.sql import func
from sqlmodel import Session, select
from models.DB.detail import Detail
from models.DB.order import Order
from utils.database import engine
from models.DTO.order import OrderDto, ProductDetailDto
from utils.order import process_db_order

def register_order(orderDto: OrderDto):
    with Session(engine) as session:
            newOrder = Order(
                id_cliente = orderDto.client_id
            )
            newDetails = [
                Detail(
                id_producto = detailDto.product_id,
                cantidad = detailDto.amount,
                pedido = newOrder
                )
                for detailDto
                in orderDto.details
            ]
            session.add_all(newDetails)
            session.commit()

def get_orders_by_client_id(client_id: str):
    with Session(engine) as session:
        statement = select(Order).where(Order.id_cliente == client_id)
        orders = session.exec(statement).all()
        orderDtos = list(map(process_db_order, orders))
        return orderDtos
    
def get_orders(startDate: Optional[datetime], endDate: Optional[datetime]):
     with Session(engine) as session:
          statement = select(Order)
          if startDate is not None: statement = statement.where(func.date(Order.fecha) >= startDate.date)
          if endDate is not None: statement = statement.where(func.date(Order.fecha) <= endDate.date)
          orders = session.exec(statement).all()
          orderDtos = list(map(process_db_order, orders))
          return orderDtos


    


    