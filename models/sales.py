from pydantic import BaseModel

class Sales(BaseModel):
    productName: str
    quantity: int
    price: float
    totalPrice: float