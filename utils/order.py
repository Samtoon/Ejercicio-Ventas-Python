from functools import reduce
from models.DB.order import Order
from models.DTO.order import OrderDto, ProductDetailDto


def _sum_costs(dto1: ProductDetailDto, dto2: ProductDetailDto):
    return dto1.total_cost + dto2.total_cost

def process_db_order(order: Order):
    detailDtos: list["ProductDetailDto"] = []
    for detail in order.detalles:
        detailDtos.append(ProductDetailDto(
            product_id = detail.id_producto,
            name = detail.producto.nombre,
            amount = detail.cantidad,
            unit_cost = detail.producto.precio,
            total_cost = detail.producto.precio * detail.cantidad
        ))
    orderDto = OrderDto(
        client_id = order.id_cliente,
        date = order.fecha,
        details = detailDtos,
        total_cost = reduce(_sum_costs, detailDtos)
    )
    return orderDto