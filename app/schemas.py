# app/schemas.py

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

class ApplicationBase(BaseModel):
    DEALER_ID: Optional[int] = None # Foreign Key to DEALER_ID
    CUSTOMER_ID: Optional[int] = None # Foreign Key to CUSTOMER_ID
    CMO_ID: Optional[int] = None # Foreign Key to CMO_ID
    USER_ID: Optional[int] = None # Foreign Key to USER_ID
    ASSET_ID: Optional[int] = None # Foreign Key to ASSET_ID
    TENOR_YEAR: Optional[int] = None
    TENOR_MONTH: Optional[int] = None
    OTR: Optional[int] = None
    DP: Optional[int] = None
    INSURANCE: Optional[int] = None
    PROVISION: Optional[int] = None
    PRINCIPAL: Optional[int] = None
    MONTHLY_PAYMENT: Optional[int] = None
    INTEREST_RATE: Optional[float] = None
    ADMIN_FEE: Optional[int] = None
    FIRST_PAYMENT: Optional[int] = None
    STATUS: Optional[str] = None # Pending, Approved, Rejected, Cancelled, Completed

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