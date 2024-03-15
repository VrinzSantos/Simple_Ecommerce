from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.sales import Sales

templates = Jinja2Templates(directory="templates")
products = APIRouter()

class Product:
    def __init__(self, id, name, price, images):
        self.id = id
        self.name = name
        self.price = price
        self.images = images

@products.get('/', response_class=HTMLResponse)
async def display_products(request: Request):
    products_list = [
        Product(id=1, name="Pencil", price=10, images=["pencil.jpg"]),
        Product(id=2, name="Pen", price=50, images=["pen_set.jpg"]),
        Product(id=3, name="Eraser", price=30, images=["eraser.jpg"]),
        Product(id=4, name="Backpack", price=500, images=["backpack.jpg"]),
        Product(id=5, name="Notebook", price=20, images=["notebook.jpg"]),
        Product(id=6, name="Ruler", price=15, images=["ruler.jpg"]),
        Product(id=7, name="Calculator", price=250, images=["calculator.jpg"]),
        Product(id=8, name="Crosswise", price=20, images=["crosswise.jpg"]),
        Product(id=9, name="Highlighter", price=50, images=["highlighter.jpg"]),
        Product(id=10, name="Scissor", price=30, images=["scissor.jpg"]),
        Product(id=11, name="Glue", price=20, images=["glue.jpg"]),
        Product(id=12, name="Pentel Pen", price=30, images=["pentel_pen.jpg"])
        # Update image paths and add as many images as needed
    ]
    return templates.TemplateResponse("index.html", {"request": request, "products": products_list})

@products.post('/sales/', response_class=HTMLResponse)
async def buy_product(request: Request, sales_data: Sales):
    # Here you would save the sales_data to your database
    # For now, let's just return the received data
    return {"message": "Sale created successfully"}
