# app/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from uuid import UUID

class CustomerBase(BaseModel):
    CUST_NAME: Optional[str] = None
    CUST_TYPE: Optional[str] = None
    CUST_ID_TYPE: Optional[str] = None
    CUST_ID_NUMBER: Optional[str] = None
    CUST_FOTO_ID: Optional[str] = None
    CUST_BIRTH_PLACE: Optional[str] = None
    CUST_BIRTH_DATE: Optional[date] = None
    CUST_GENDER: Optional[str] = None
    CUST_ADDRESS: Optional[str] = None
    CUST_ALM_KEL: Optional[str] = None
    CUST_ALM_KEC: Optional[str] = None
    CUST_ALM_KOT: Optional[str] = None
    CUST_MARITAL_STATUS: Optional[str] = None
    CUST_NPWP: Optional[str] = None
    CUST_PHONE_NUMBER: Optional[str] = None
    CUST_EMAIL: Optional[str] = None