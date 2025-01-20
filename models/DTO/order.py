from collections.abc import Sequence
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProductDetailDto(BaseModel):
    product_id: int
    name: Optional[str] = None
    amount: int
    unit_cost: Optional[int] = None
    total_cost: Optional[int] = None

class OrderDto(BaseModel):
    client_id: str
    details: list["ProductDetailDto"]
    date: Optional[datetime] = None
    total_cost: Optional[int] = None