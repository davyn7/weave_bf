# app/buana/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from uuid import UUID

class AssetBase(BaseModel):
    DEALER_ID: Optional[int] = None # Foreign Key to DEALER_ID
    BRAND: Optional[str] = None
    MODEL: Optional[str] = None
    YEAR: Optional[int] = None
    COLOR: Optional[str] = None
    CONDITION: Optional[str] = None # New or Used
    PLATE_NUMBER: Optional[str] = None

class BranchBase(BaseModel):
    NAME: Optional[str] = None
    ADDRESS: Optional[str] = None
    PROVINCE_ID: Optional[int] = None # Foreign Key to PROVINCE_ID
    CITY_ID: Optional[int] = None # Foreign Key to CITY_ID
    POSTAL_CODE: Optional[str] = None
    PHONE_NUMBER: Optional[str] = None
    EMAIL: Optional[str] = None
    DESCRIPTION: Optional[str] = None

class CMOBase(BaseModel):
    BRANCH_ID: Optional[int] = None # Foreign Key to BRANCH_ID
    FIRST_NAME: Optional[str] = None
    LAST_NAME: Optional[str] = None
    PHONE_NUMBER: Optional[str] = None
    EMAIL: Optional[str] = None
    DESCRIPTION: Optional[str] = None

class SurveyBase(BaseModel):
    APPLICATION_ID: Optional[int] = None # Foreign Key to APPLICATION_ID
    pass