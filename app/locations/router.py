# app/locations/router.py

from fastapi import APIRouter

from app.locations.schemas import (
    ProvinceBase,
    CityBase,
    KecamatanBase,
    KelurahanBase,
)

from app.locations.managers import (
    LocationManager,
    LocationSearchManager
)

router = APIRouter(prefix="/locations", tags=["Locations"])

@router.get("/provinces")
async def get_provinces():
    try:
        manager = LocationSearchManager(None)
        return await manager.get_provinces()
    except Exception as e:
        raise e

@router.get("/cities/{province_id}")
async def get_cities(province_id: int):
    try:
        manager = LocationSearchManager(province_id=province_id)
        return await manager.get_cities()
    except Exception as e:
        raise e

@router.get("/kecamatans/{city_id}")
async def get_kecamatans(city_id: int):
    try:
        manager = LocationSearchManager(city_id=city_id)
        return await manager.get_kecamatans()
    except Exception as e:
        raise e

@router.get("/kelurahans/{kecamatan_id}")
async def get_kelurahans(kecamatan_id: int):
    try:
        manager = LocationSearchManager(kecamatan_id=kecamatan_id)
        return await manager.get_kelurahans()
    except Exception as e:
        raise e

@router.get("/postal_code/{kelurahan_id}")
async def get_postal_code(kelurahan_id: int):
    try:
        manager = LocationSearchManager(kelurahan_id=kelurahan_id)
        return await manager.get_postal_code()
    except Exception as e:
        raise e

# Location Routers

@router.post("/add_province")
async def add_province(province: ProvinceBase):
    try:
        manager = LocationManager(province=province)
        return await manager.add_province()
    except Exception as e:
        raise e

@router.post("/add_city")
async def add_city(city: CityBase):
    try:
        manager = LocationManager(city=city)
        return await manager.add_city()
    except Exception as e:
        raise e

@router.post("/add_kecamatan")
async def add_kecamatan(kecamatan: KecamatanBase):
    try:
        manager = LocationManager(kecamatan=kecamatan)
        return await manager.add_kecamatan()
    except Exception as e:
        raise e

@router.post("/add_kelurahan")
async def add_kelurahan(kelurahan: KelurahanBase):
    try:
        manager = LocationManager(kelurahan=kelurahan)
        return await manager.add_kelurahan()
    except Exception as e:
        raise e