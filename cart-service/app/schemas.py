from pydantic import BaseModel
from typing import List

class CartItem(BaseModel):
    product_id: int
    quantity: int

class TransactionCreate(BaseModel):
    user_id: int
    items: List[CartItem]
