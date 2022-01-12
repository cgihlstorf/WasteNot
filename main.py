from os import name
from fastapi import Depends, FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

import importlib

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app_path = Path.cwd()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def sign_up(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@app.get("/home")
async def show_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/entry")
async def show_home(request: Request):
    print(request)
    return templates.TemplateResponse("form.html", {"request": request})

@app.get("/home/thankyou")
async def show_home(request: Request):
    return templates.TemplateResponse("tthankyou.html", {"request": request})


@app.get("/home/data")
async def send_data(request: Request):
    food_items = importlib.import_module('food_data') # a dict of Title: depth
    # print(food_items)
    data = food_items.data
    # print(data)
    return data