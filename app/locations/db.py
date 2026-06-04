# app/locations/db.py

from app.connection import supabase
from app.locations.schemas import (
    ProvinceBase,
    CityBase,
    KecamatanBase,
    KelurahanBase
)
from uuid import UUID

# Location DB Operations

async def add_province_db(province: ProvinceBase):
    province_data = province.model_dump(mode="json")
    response = supabase.table("PROVINCES").insert(province_data).execute()
    return response.data

async def add_city_db(city: CityBase):
    city_data = city.model_dump(mode="json")
    response = supabase.table("CITIES").insert(city_data).execute()
    return response.data

async def add_kecamatan_db(kecamatan: KecamatanBase):
    kecamatan_data = kecamatan.model_dump(mode="json")
    response = supabase.table("KECAMATAN").insert(kecamatan_data).execute()
    return response.data

async def add_kelurahan_db(kelurahan: KelurahanBase):
    kelurahan_data = kelurahan.model_dump(mode="json")
    response = supabase.table("KELURAHAN").insert(kelurahan_data).execute()
    return response.data

# Location Search DB Operations

async def get_provinces_db():
    response = supabase.table("PROVINCES").select("*").execute()
    return response.data

async def get_cities_db(province_id: int):
    response = supabase.table("CITIES").select("*").eq("PROVINCE_ID", province_id).execute()
    return response.data

async def get_kecamatans_db(city_id: int):
    response = supabase.table("KECAMATAN").select("*").eq("CITY_ID", city_id).execute()
    return response.data

async def get_kelurahans_db(kecamatan_id: int):
    response = supabase.table("KELURAHAN").select("*").eq("KECAMATAN_ID", kecamatan_id).execute()
    return response.data

async def get_postal_code_db(kelurahan_id: int):
    response = supabase.table("KELURAHAN").select("POSTAL_CODE").eq("id", kelurahan_id).execute()
    return response.data