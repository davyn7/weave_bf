# app/router.py

from fastapi import APIRouter
from app.managers import (
    CustomerManager
)
from app.schemas import (
    CustomerBase
)
from uuid import UUID

router = APIRouter()

# Initialize DB Testing

@router.post("/populate", tags=["Testing"])
async def populate():
    pass

@router.delete("/clear", tags=["Testing"])
async def clear():
    pass

# Customer Routers

@router.get("/customers", tags=["Customers"])
async def get_customers():
    try:
        manager = CustomerManager(None)
        return await manager.get_customers()
    except Exception as e:
        raise e

@router.get("/customers/{customer_id}", tags=["Customers"])
async def get_customer(customer_id: int):
    try:
        manager = CustomerManager(None)
        return await manager.get_customer(customer_id)
    except Exception as e:
        raise e

@router.post("/add_customer", tags=["Customers"])
async def add_customer(customer: CustomerBase):
    try:
        manager = CustomerManager(customer)
        return await manager.add_customer()
    except Exception as e:
        raise e

@router.put("/update_customer/{customer_id}", tags=["Customers"])
async def update_customer(customer_id: int, customer: CustomerBase):
    try:
        manager = CustomerManager(customer)
        return await manager.update_customer(customer_id)
    except Exception as e:
        raise e

@router.delete("/delete_customer/{customer_id}", tags=["Customers"])
async def delete_customer(customer_id: int):
    try:
        manager = CustomerManager(None)
        return await manager.delete_customer(customer_id)
    except Exception as e:
        raise e

@router.delete("/delete_customers", tags=["Customers"])
async def delete_customers():
    try:
        manager = CustomerManager(None)
        return await manager.delete_customers()
    except Exception as e:
        raise e