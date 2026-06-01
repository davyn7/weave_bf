# app/router.py

from fastapi import APIRouter
from app.managers import (
    LocationManager,
    LocationSearchManager,
    CustomerManager
)
from app.schemas import (
    ProvinceBase,
    CityBase,
    KecamatanBase,
    KelurahanBase,
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

# Location Routers

@router.post("/add_province", tags=["Location"])
async def add_province(province: ProvinceBase):
    try:
        manager = LocationManager(province=province)
        return await manager.add_province()
    except Exception as e:
        raise e

@router.post("/add_city", tags=["Location"])
async def add_city(city: CityBase):
    try:
        manager = LocationManager(city=city)
        return await manager.add_city()
    except Exception as e:
        raise e

@router.post("/add_kecamatan", tags=["Location"])
async def add_kecamatan(kecamatan: KecamatanBase):
    try:
        manager = LocationManager(kecamatan=kecamatan)
        return await manager.add_kecamatan()
    except Exception as e:
        raise e

@router.post("/add_kelurahan", tags=["Location"])
async def add_kelurahan(kelurahan: KelurahanBase):
    try:
        manager = LocationManager(kelurahan=kelurahan)
        return await manager.add_kelurahan()
    except Exception as e:
        raise e

# Location Search Routers

@router.get("/cities/{province_id}", tags=["Location Search"])
async def get_cities(province_id: int):
    try:
        manager = LocationSearchManager(province_id=province_id)
        return await manager.get_cities()
    except Exception as e:
        raise e

@router.get("/kecamatans/{city_id}", tags=["Location Search"])
async def get_kecamatans(city_id: int):
    try:
        manager = LocationSearchManager(city_id=city_id)
        return await manager.get_kecamatans()
    except Exception as e:
        raise e

@router.get("/kelurahans/{kecamatan_id}", tags=["Location Search"])
async def get_kelurahans(kecamatan_id: int):
    try:
        manager = LocationSearchManager(kecamatan_id=kecamatan_id)
        return await manager.get_kelurahans()
    except Exception as e:
        raise e

@router.get("/postal_code/{kelurahan_id}", tags=["Location Search"])
async def get_postal_code(kelurahan_id: int):
    try:
        manager = LocationSearchManager(kelurahan_id=kelurahan_id)
        return await manager.get_postal_code()
    except Exception as e:
        raise e

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