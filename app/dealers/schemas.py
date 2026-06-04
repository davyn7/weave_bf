# app/dealers/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from uuid import UUID

class DealerBase(BaseModel):
    BRANCH_ID: Optional[int] = None # Foreign Key to BRANCH_ID
    NAME: Optional[str] = None
    ADDRESS: Optional[str] = None
    PROVINCE_ID: Optional[int] = None # Foreign Key to PROVINCE_ID
    CITY_ID: Optional[int] = None # Foreign Key to CITY_ID
    KECAMATAN_ID: Optional[int] = None # Foreign Key to KECAMATAN_ID
    KELURAHAN_ID: Optional[int] = None # Foreign Key to KELURAHAN_ID
    POSTAL_CODE: Optional[str] = None
    PHONE_NUMBER: Optional[str] = None
    EMAIL: Optional[str] = None
    DESCRIPTION: Optional[str] = None
    UNIQUE_CODE: Optional[str] = None

class UserBase(BaseModel):
    DEALER_ID: Optional[int] = None # Foreign Key to DEALER_ID
    FIRST_NAME: Optional[str] = None
    LAST_NAME: Optional[str] = None
    PHONE_NUMBER: Optional[str] = None
    EMAIL: Optional[str] = None
    DEALER_PIC: Optional[bool] = False
    UNIQUE_CODE: Optional[str] = None
    IS_ACTIVE: Optional[bool] = False