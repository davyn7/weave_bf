# app/schemas.py

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