# app/locations/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional, List

class ProvinceBase(BaseModel):
    NAME: Optional[str] = None

class CityBase(BaseModel):
    PROVINCE_ID: Optional[int] = None # Foreign Key to PROVINCE_ID
    NAME: Optional[str] = None
    TYPE: Optional[str] = None # Kota or Kabupaten

class KecamatanBase(BaseModel):
    CITY_ID: Optional[int] = None # Foreign Key to CITY_ID
    NAME: Optional[str] = None

class KelurahanBase(BaseModel):
    KECAMATAN_ID: Optional[int] = None # Foreign Key to KECAMATAN_ID
    NAME: Optional[str] = None
    POSTAL_CODE: Optional[str] = None