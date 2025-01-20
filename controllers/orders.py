from datetime import datetime
from fastapi import APIRouter
from services import orders_service
from models.DTO.order import OrderDto

router = APIRouter(
    prefix="/orders"
)

@router.get("/{order_id}")
async def get_order_by_id(order_id: int):
    return "La orden"

@router.post("/")
async def create_order(orderDto: OrderDto):
    orders_service.register_order(orderDto)
    return "Orden registrada con éxito"

@router.get("/by_client_id/{client_id}")
async def get_orders_by_client_id(client_id: str):
    dtos = orders_service.get_orders_by_client_id(client_id)
    return dtos

@router.get("/")
async def get_orders(startDate: datetime | None = None, endDate: datetime | None = None):
    dtos = orders_service.get_orders(startDate, endDate)
    return dtos
