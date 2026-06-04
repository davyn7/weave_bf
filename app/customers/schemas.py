# app/customers/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional, List

class CustomerBase(BaseModel):
    DEALER_ID: Optional[int] = None # Foreign Key to DEALER_ID
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
    MARITAL_STATUS: Optional[bool] = False
    ADDRESS: Optional[str] = None
    KELURAHAN: Optional[str] = None
    KECAMATAN: Optional[str] = None
    CITY: Optional[str] = None
    PROVINCE: Optional[str] = None
    PROVINCE_ID: Optional[int] = None
    KTP_PHOTO: Optional[str] = None
    GUARANTOR: Optional[bool] = False

class SpouseBase(BaseModel):
    CUSTOMER_ID: Optional[int] = None # Foreign Key to CUSTOMER_ID
    FIRST_NAME: Optional[str] = None
    LAST_NAME: Optional[str] = None
    PHONE_NUMBER: Optional[str] = None
    EMAIL: Optional[str] = None
    NIK: Optional[str] = None
    NPWP: Optional[str] = None
    GENDER: Optional[str] = None
    BIRTH_PLACE: Optional[str] = None
    BIRTH_DATE: Optional[date] = None

class GuarantorBase(BaseModel):
    CUSTOMER_ID: Optional[int] = None # Foreign Key to CUSTOMER_ID
    FIRST_NAME: Optional[str] = None
    LAST_NAME: Optional[str] = None
    PHONE_NUMBER: Optional[str] = None
    EMAIL: Optional[str] = None
    NIK: Optional[str] = None
    NPWP: Optional[str] = None
    GENDER: Optional[str] = None
    BIRTH_PLACE: Optional[str] = None
    BIRTH_DATE: Optional[date] = None