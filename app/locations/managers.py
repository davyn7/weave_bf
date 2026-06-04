# app/locations/managers.py

from app.locations.schemas import (
    ProvinceBase,
    CityBase,
    KecamatanBase,
    KelurahanBase,
)
from app.locations.db import (
    add_province_db,
    add_city_db,
    add_kecamatan_db,
    add_kelurahan_db,
    get_provinces_db,
    get_cities_db,
    get_kecamatans_db,
    get_kelurahans_db,
    get_postal_code_db,
)
from uuid import UUID
from typing import Optional
import math
import random
import string

class LocationManager:

    def __init__(self, province: Optional[ProvinceBase] = None, city: Optional[CityBase] = None, kecamatan: Optional[KecamatanBase] = None, kelurahan: Optional[KelurahanBase] = None):
        self.province = province
        self.city = city
        self.kecamatan = kecamatan
        self.kelurahan = kelurahan

    async def add_province(self):
        return await add_province_db(self.province)    

    async def add_city(self):
        return await add_city_db(self.city)

    async def add_kecamatan(self):
        return await add_kecamatan_db(self.kecamatan)

    async def add_kelurahan(self):
        return await add_kelurahan_db(self.kelurahan)

class LocationSearchManager:

    def __init__(self, province_id: Optional[int] = None, city_id: Optional[int] = None, kecamatan_id: Optional[int] = None, kelurahan_id: Optional[int] = None):
        self.province_id = province_id
        self.city_id = city_id
        self.kecamatan_id = kecamatan_id
        self.kelurahan_id = kelurahan_id

    async def get_provinces(self):
        return await get_provinces_db()

    async def get_cities(self):
        return await get_cities_db(self.province_id)

    async def get_kecamatans(self):
        return await get_kecamatans_db(self.city_id)

    async def get_kelurahans(self):
        return await get_kelurahans_db(self.kecamatan_id)

    async def get_postal_code(self):
        return await get_postal_code_db(self.kelurahan_id)