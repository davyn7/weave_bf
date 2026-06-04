# app/router.py

from fastapi import APIRouter
from app.managers import (
    TestManager,
    BranchManager,
    CMOManager,
    ApplicationManager,
    AssetManager
)
from app.schemas import (
    BranchBase,
    CMOBase,
    ApplicationBase,
    AssetBase,
)
from pydantic import BaseModel
from typing import List
from uuid import UUID

router = APIRouter()

# Initialize DB Testing

@router.post("/populate", tags=["Testing"])
async def populate():
    pass

@router.delete("/clear", tags=["Testing"])
async def clear():
    pass

# Branch Routers

@router.get("/branches", tags=["Branch"])
async def get_branches():
    try:
        manager = BranchManager(None)
        return await manager.get_branches()
    except Exception as e:
        raise e

@router.get("/branches/{branch_id}", tags=["Branch"])
async def get_branch(branch_id: int):
    try:
        manager = BranchManager(None)
        return await manager.get_branch(branch_id)
    except Exception as e:
        raise e

@router.post("/add_branch", tags=["Branch"])
async def add_branch(branch: BranchBase):
    try:
        manager = BranchManager(branch)
        return await manager.add_branch()
    except Exception as e:
        raise e

@router.put("/update_branch/{branch_id}", tags=["Branch"])
async def update_branch(branch_id: int, branch: BranchBase):
    try:
        manager = BranchManager(branch)
        return await manager.update_branch(branch_id)
    except Exception as e:
        raise e

@router.delete("/delete_branch/{branch_id}", tags=["Branch"])
async def delete_branch(branch_id: int):
    try:
        manager = BranchManager(None)
        return await manager.delete_branch(branch_id)
    except Exception as e:
        raise e

@router.delete("/delete_branches", tags=["Branch"])
async def delete_branches():
    try:
        manager = BranchManager(None)
        return await manager.delete_branches()
    except Exception as e:
        raise e

# CMO Routers

@router.get("/cmos", tags=["CMO"])
async def get_cmos():
    try:
        manager = CMOManager(None)
        return await manager.get_cmos()
    except Exception as e:
        raise e

@router.get("/cmos/{cmo_id}", tags=["CMO"])
async def get_cmo(cmo_id: int):
    try:
        manager = CMOManager(None)
        return await manager.get_cmo(cmo_id)
    except Exception as e:
        raise e

@router.post("/add_cmo", tags=["CMO"])
async def add_cmo(cmo: CMOBase):
    try:
        manager = CMOManager(cmo)
        return await manager.add_cmo()
    except Exception as e:
        raise e

@router.put("/update_cmo/{cmo_id}", tags=["CMO"])
async def update_cmo(cmo_id: int, cmo: CMOBase):
    try:
        manager = CMOManager(cmo)
        return await manager.update_cmo(cmo_id)
    except Exception as e:
        raise e

@router.delete("/delete_cmo/{cmo_id}", tags=["CMO"])
async def delete_cmo(cmo_id: int):
    try:
        manager = CMOManager(None)
        return await manager.delete_cmo(cmo_id)
    except Exception as e:
        raise e

@router.delete("/delete_cmos", tags=["CMO"])
async def delete_cmos():
    try:
        manager = CMOManager(None)
        return await manager.delete_cmos()
    except Exception as e:
        raise e

# Application Routers

@router.get("/applications", tags=["Applications"])
async def get_applications():
    try:
        manager = ApplicationManager(None)
        return await manager.get_applications()
    except Exception as e:
        raise e

@router.get("/applications/{application_id}", tags=["Applications"])
async def get_application(application_id: int):
    try:
        manager = ApplicationManager(None)
        return await manager.get_application(application_id)
    except Exception as e:
        raise e

@router.post("/add_application", tags=["Applications"])
async def add_application(application: ApplicationBase):
    try:
        manager = ApplicationManager(application)
        return await manager.add_application()
    except Exception as e:
        raise e

@router.put("/update_application/{application_id}", tags=["Applications"])
async def update_application(application_id: int, application: ApplicationBase):
    try:
        manager = ApplicationManager(application)
        return await manager.update_application(application_id)
    except Exception as e:
        raise e

@router.delete("/delete_application/{application_id}", tags=["Applications"])
async def delete_application(application_id: int):
    try:
        manager = ApplicationManager(None)
        return await manager.delete_application(application_id)
    except Exception as e:
        raise e

@router.delete("/delete_applications", tags=["Applications"])
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

@router.get("/application_credit_simulation", tags=["Applications"])
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

@router.post("/test_application_credit_simulation", tags=["Applications"])
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

# Asset Routers

@router.get("/assets", tags=["Assets"])
async def get_assets():
    try:
        manager = AssetManager(None)
        return await manager.get_assets()
    except Exception as e:
        raise e
        
@router.get("/assets/{asset_id}", tags=["Assets"])
async def get_asset(asset_id: int):
    try:
        manager = AssetManager(None)
        return await manager.get_asset(asset_id)
    except Exception as e:
        raise e
        
@router.post("/add_asset", tags=["Assets"])
async def add_asset(asset: AssetBase):
    try:
        manager = AssetManager(asset)
        return await manager.add_asset()
    except Exception as e:
        raise e

@router.put("/update_asset/{asset_id}", tags=["Assets"])
async def update_asset(asset_id: int, asset: AssetBase):
    try:
        manager = AssetManager(asset)
        return await manager.update_asset(asset_id)
    except Exception as e:
        raise e
        
@router.delete("/delete_asset/{asset_id}", tags=["Assets"])
async def delete_asset(asset_id: int):
    try:
        manager = AssetManager(None)
        return await manager.delete_asset(asset_id)
    except Exception as e:
        raise e
        
@router.delete("/delete_assets", tags=["Assets"])
async def delete_assets():
    try:
        manager = AssetManager(None)
        return await manager.delete_assets()
    except Exception as e:
        raise e