from fastapi import APIRouter, Form, HTTPException
from fastapi.templating import Jinja2Templates
from models.sales import Sales
from config.db import conn

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post('/sales/')
async def create_sales(productName: str = Form(...), quantity: int = Form(...), price: float = Form(...), totalPrice: float = Form(...)):
    try:
        # Calculate the total price
        total_price = price * quantity

        # Create a Sales object with the calculated total price
        sales_obj = Sales(productName=productName, quantity=quantity, price=price, totalPrice=total_price)

        # Save the sales data to the database
        conn.sales_db.sales.insert_one(sales_obj.dict())

        # Return a success message
        return {"message": "Purchase successfully"}

    except Exception as e:
        # Handle other exceptions
        raise HTTPException(status_code=500, detail="Internal server error")
