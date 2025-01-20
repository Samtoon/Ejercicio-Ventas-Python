from fastapi import APIRouter

router = APIRouter(
    prefix="/clients"
)

@router.get("/{client_id}/orders")
async def get_orders_by_client_id(client_id: str):
    return "Tus pedidos"