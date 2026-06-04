# app/buana/router.py

from fastapi import APIRouter
from app.buana.managers import (
    BranchManager,
    CMOManager,
    AssetManager
)
from app.buana.schemas import (
    BranchBase,
    CMOBase,
    AssetBase
)
from pydantic import BaseModel
from typing import List
from uuid import UUID

router = APIRouter(prefix="/buana", tags=["Buana"])

# Branch Routers

@router.get("/branches")
async def get_branches():
    try:
        manager = BranchManager(None)
        return await manager.get_branches()
    except Exception as e:
        raise e

@router.get("/branches/{branch_id}")
async def get_branch(branch_id: int):
    try:
        manager = BranchManager(None)
        return await manager.get_branch(branch_id)
    except Exception as e:
        raise e

@router.post("/add_branch")
async def add_branch(branch: BranchBase):
    try:
        manager = BranchManager(branch)
        return await manager.add_branch()
    except Exception as e:
        raise e

@router.put("/update_branch/{branch_id}")
async def update_branch(branch_id: int, branch: BranchBase):
    try:
        manager = BranchManager(branch)
        return await manager.update_branch(branch_id)
    except Exception as e:
        raise e

@router.delete("/delete_branch/{branch_id}")
async def delete_branch(branch_id: int):
    try:
        manager = BranchManager(None)
        return await manager.delete_branch(branch_id)
    except Exception as e:
        raise e

@router.delete("/delete_branches")
async def delete_branches():
    try:
        manager = BranchManager(None)
        return await manager.delete_branches()
    except Exception as e:
        raise e

# CMO Routers

@router.get("/cmos")
async def get_cmos():
    try:
        manager = CMOManager(None)
        return await manager.get_cmos()
    except Exception as e:
        raise e

@router.get("/cmos/{cmo_id}")
async def get_cmo(cmo_id: int):
    try:
        manager = CMOManager(None)
        return await manager.get_cmo(cmo_id)
    except Exception as e:
        raise e

@router.post("/add_cmo")
async def add_cmo(cmo: CMOBase):
    try:
        manager = CMOManager(cmo)
        return await manager.add_cmo()
    except Exception as e:
        raise e

@router.put("/update_cmo/{cmo_id}")
async def update_cmo(cmo_id: int, cmo: CMOBase):
    try:
        manager = CMOManager(cmo)
        return await manager.update_cmo(cmo_id)
    except Exception as e:
        raise e

@router.delete("/delete_cmo/{cmo_id}")
async def delete_cmo(cmo_id: int):
    try:
        manager = CMOManager(None)
        return await manager.delete_cmo(cmo_id)
    except Exception as e:
        raise e

@router.delete("/delete_cmos")
async def delete_cmos():
    try:
        manager = CMOManager(None)
        return await manager.delete_cmos()
    except Exception as e:
        raise e

# Asset Routers

@router.get("/assets")
async def get_assets():
    try:
        manager = AssetManager(None)
        return await manager.get_assets()
    except Exception as e:
        raise e
        
@router.get("/assets/{asset_id}")
async def get_asset(asset_id: int):
    try:
        manager = AssetManager(None)
        return await manager.get_asset(asset_id)
    except Exception as e:
        raise e
        
@router.post("/add_asset")
async def add_asset(asset: AssetBase):
    try:
        manager = AssetManager(asset)
        return await manager.add_asset()
    except Exception as e:
        raise e

@router.put("/update_asset/{asset_id}")
async def update_asset(asset_id: int, asset: AssetBase):
    try:
        manager = AssetManager(asset)
        return await manager.update_asset(asset_id)
    except Exception as e:
        raise e
        
@router.delete("/delete_asset/{asset_id}")
async def delete_asset(asset_id: int):
    try:
        manager = AssetManager(None)
        return await manager.delete_asset(asset_id)
    except Exception as e:
        raise e
        
@router.delete("/delete_assets")
async def delete_assets():
    try:
        manager = AssetManager(None)
        return await manager.delete_assets()
    except Exception as e:
        raise e