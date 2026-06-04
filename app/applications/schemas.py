# app/applications/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from uuid import UUID

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