# app/rates/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from uuid import UUID

class InterestRateBase(BaseModel):
    TENOR_YEAR: Optional[int] = None
    TENOR_MONTH: Optional[int] = None
    TYPE: Optional[str] = None # New or Used
    RATE: Optional[float] = None
    DEPRECIATION: Optional[float] = None
    TJH: Optional[float] = None
    ADMIN_FEE: Optional[float] = None
    FIDUCIAL_FEE: Optional[float] = None
    INSURANCE_POLICY_FEE: Optional[float] = None

class InsuranceBase(BaseModel):
    PROVINCE_ID: Optional[int] = None # Foreign Key to PROVINCE_ID
    UPPER_LIMIT: Optional[float] = None
    LOWER_LIMIT: Optional[float] = None
    RATE: Optional[float] = None

# Testing

class InsuranceSpec(BaseModel):
    UPPER_LIMIT: int
    LOWER_LIMIT: int
    RATE: float

class BatchAddInsurancesRequest(BaseModel):
    provinces: list[int]
    specs: list[InsuranceSpec]