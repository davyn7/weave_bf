# app/applications/router.py

from fastapi import APIRouter

from app.applications.schemas import (
    ApplicationBase
)

from app.applications.managers import (
    ApplicationManager
)
from pydantic import BaseModel
from typing import List
from uuid import UUID

router = APIRouter(prefix="/applications", tags=["Applications"])

# Application Routers

@router.get("/applications")
async def get_applications():
    try:
        manager = ApplicationManager(None)
        return await manager.get_applications()
    except Exception as e:
        raise e

@router.get("/applications/{application_id}")
async def get_application(application_id: int):
    try:
        manager = ApplicationManager(None)
        return await manager.get_application(application_id)
    except Exception as e:
        raise e

@router.post("/add_application")
async def add_application(application: ApplicationBase):
    try:
        manager = ApplicationManager(application)
        return await manager.add_application()
    except Exception as e:
        raise e

@router.put("/update_application/{application_id}")
async def update_application(application_id: int, application: ApplicationBase):
    try:
        manager = ApplicationManager(application)
        return await manager.update_application(application_id)
    except Exception as e:
        raise e

@router.delete("/delete_application/{application_id}")
async def delete_application(application_id: int):
    try:
        manager = ApplicationManager(None)
        return await manager.delete_application(application_id)
    except Exception as e:
        raise e

@router.delete("/delete_applications")
async def delete_applications():
    try:
        manager = ApplicationManager(None)
        return await manager.delete_applications()
    except Exception as e:
        raise e

# @router.get("/calculate_insurance_rate", tags=["Applications"])
# async def calculate_insurance_rate(
#     otr: int,
#     province_id: int,
#     tenor_year: int,
#     TYPE: str
# ):
#     try:
#         manager = ApplicationManager(None)
#         return await manager.calculate_insurance_rate(
#             otr=otr,
#             province_id=province_id,
#             tenor_year=tenor_year,
#             TYPE=TYPE,
#         )
#     except Exception as e:
#         raise e

@router.get("/application_credit_simulation")
async def application_credit_simulation(application_id: int, PROVISION: int = 0):
    try:
        manager = ApplicationManager(None)
        application_dict = await manager.get_application(application_id)
        application_dict = application_dict[0]
        application = ApplicationBase(**application_dict)
        new_manager = ApplicationManager(application)
        return await new_manager.application_credit_simulation(PROVISION=PROVISION)
    except Exception as e:
        raise e

class CreditSimulationRequest(BaseModel):
    OTR: int
    DP: int
    TENOR_YEAR: int
    TENOR_MONTH: int
    TYPE: str
    PROVINCE_ID: int

@router.post("/test_application_credit_simulation")
async def test_application_credit_simulation(payload: CreditSimulationRequest):
    try:
        manager = ApplicationManager(None)
        return await manager.test_application_credit_simulation(OTR=payload.OTR, DP=payload.DP, TENOR_YEAR=payload.TENOR_YEAR, TENOR_MONTH=payload.TENOR_MONTH, TYPE=payload.TYPE, PROVINCE_ID=payload.PROVINCE_ID)
    except Exception as e:
        raise e

# @router.put("/add_application_credit_simulation", tags=["Applications"])
# async def add_application_credit_simulation(application: ApplicationBase):
#     try:
#         manager = ApplicationManager(application)
#         return await manager.add_application_credit_simulation()
#     except Exception as e:
#         raise e
