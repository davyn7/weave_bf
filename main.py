from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from supabase import create_client, Client
from app.router import router
from app.locations.router import router as locations_router
from app.rates.router import router as rates_router
from app.customers.router import router as customers_router
from app.dealers.router import router as dealers_router
from app.applications.router import router as applications_router

load_dotenv()

app = FastAPI()

app.include_router(router)
app.include_router(locations_router)
app.include_router(rates_router)
app.include_router(customers_router)
app.include_router(dealers_router)
app.include_router(applications_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}