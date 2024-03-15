from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from routes import sales

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount static files
app.mount("/images", StaticFiles(directory="images"), name="images")

# Include routers
app.include_router(sales.router)

@app.get('/purchase-success', response_class=HTMLResponse)
async def purchase_success():
    with open("purchase_success.html", "r") as file:
        html_content = file.read()
    return html_content

@app.get('/', response_class=HTMLResponse)
async def display_products(request: Request):
    products_list = [
        {"id": 1, "name": "Pencil", "price": 10, "images": ["pencil.jpg"]},
        {"id": 2, "name": "Pen Set", "price": 50, "images": ["pen_set.jpg"]},
        {"id": 3, "name": "Eraser", "price": 30, "images": ["eraser.jpg"]},
        {"id": 4, "name" : "Backpack", "price" : 500, "images" : ["backpack.jpg"]},
        {"id": 5, "name" : "Notebook", "price" :20, "images" :["notebook.jpg"]},
        {"id": 6, "name" : "Ruler", "price" : 15, "images" : ["ruler.jpg"]},
        {"id": 7, "name" : "Calculator", "price" : 250, "images" : ["calculator.jpg"]},
        {"id": 8, "name" : "Crosswise", "price" : 20, "images" : ["crosswise.jpg"]},
        {"id": 9, "name" : "Highlighter", "price" : 50, "images" : ["highlighter.jpg"]},
        {"id" : 0, "name" : "Scissor", "price" : 30, "images" : ["scissors.jpg"]},
        {"id" : 11, "name" :"Glue", "price" : 20, "images" : ["glue.jpg"]},
        {"id" : 12, "name" :"Pentel Pen", "price" : 30, "images" :["pentel_pen.jpg"]}
    ]
    return templates.TemplateResponse("index.html", {"request": request, "products": products_list})
