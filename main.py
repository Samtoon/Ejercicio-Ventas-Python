from typing import Union

from fastapi import FastAPI
from controllers import products, auth, clients, orders

app = FastAPI()

app.include_router(products.router)
app.include_router(auth.router)
app.include_router(clients.router)
app.include_router(orders.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}