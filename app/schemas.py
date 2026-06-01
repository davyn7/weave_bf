# app/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from uuid import UUID

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

class DealerBase(BaseModel):
    pass

class UserBase(BaseModel):
    # Foreign Key to DEALER_ID
    pass

class CustomerBase(BaseModel):
    FIRST_NAME: Optional[str] = None
    LAST_NAME: Optional[str] = None
    PHONE_NUMBER: Optional[str] = None
    EMAIL: Optional[str] = None
    TYPE: Optional[str] = None
    NIK: Optional[str] = None
    NPWP: Optional[str] = None
    GENDER: Optional[str] = None
    BIRTH_PLACE: Optional[str] = None
    BIRTH_DATE: Optional[date] = None
    MARITAL_STATUS: Optional[str] = None
    ADDRESS: Optional[str] = None
    KELURAHAN: Optional[str] = None
    KECAMATAN: Optional[str] = None
    KOTA: Optional[str] = None
    PROVINSI: Optional[str] = None
    CUST_ID_TYPE: Optional[str] = None
    CUST_FOTO_ID: Optional[str] = None

class SpouseBase(BaseModel):
    # Foreign Key to CUSTOMER_ID
    pass

class GuarantorBase(BaseModel):
    # Foreign Key to CUSTOMER_ID
    pass

class AssetBase(BaseModel):
    # Foreign Key to DEALER_ID
    pass

class ApplicationBase(BaseModel):
    # Foreign Key to DEALER_ID
    # Foreign Key to CUSTOMER_ID
    # Foreign Key to USER_ID
    pass