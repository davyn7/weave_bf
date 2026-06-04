# app/buana/managers.py

from app.buana.schemas import (
    BranchBase,
    CMOBase,
    AssetBase
)
from app.buana.db import (
    get_branches_db,
    get_branch_db,
    add_branch_db,
    update_branch_db,
    delete_branch_db,
    delete_branches_db,
    get_cmos_db,
    get_cmo_db,
    add_cmo_db,
    update_cmo_db,
    delete_cmo_db,
    delete_cmos_db
)

# For Assets
from app.buana.db import (
    get_assets_db,
    get_asset_db,
    add_asset_db,
    update_asset_db,
    delete_asset_db,
    delete_assets_db
)

from uuid import UUID
from typing import Optional
import math
import random
import string

def generate_unique_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

class TestManager:

    def __init__(self):
        pass

    async def test(self):
        return "Hello, World!"

class BranchManager:

    def __init__(self, branch: BranchBase):
        self.branch = branch

    async def get_branches(self):
        return await get_branches_db()

    async def get_branch(self, branch_id: int):
        return await get_branch_db(branch_id)

    async def add_branch(self):
        return await add_branch_db(self.branch)

    async def update_branch(self, branch_id: int):
        return await update_branch_db(self.branch, branch_id)

    async def delete_branch(self, branch_id: int):
        return await delete_branch_db(branch_id)

    async def delete_branches(self):
        return await delete_branches_db()

class CMOManager:

    def __init__(self, cmo: CMOBase):
        self.cmo = cmo

    async def get_cmos(self):
        return await get_cmos_db()
    
    async def get_cmo(self, cmo_id: int):
        return await get_cmo_db(cmo_id)

    async def add_cmo(self):
        return await add_cmo_db(self.cmo)
    
    async def update_cmo(self, cmo_id: int):
        return await update_cmo_db(self.cmo, cmo_id)
    
    async def delete_cmo(self, cmo_id: int):
        return await delete_cmo_db(cmo_id)

    async def delete_cmos(self):
        return await delete_cmos_db()
        
class AssetManager:

    def __init__(self, asset: AssetBase):
        self.asset = asset

    async def get_assets(self):
        return await get_assets_db()
    
    async def get_asset(self, asset_id: int):
        return await get_asset_db(asset_id)

    async def add_asset(self):
        return await add_asset_db(self.asset)
    
    async def update_asset(self, asset_id: int):
        return await update_asset_db(self.asset, asset_id)
    
    async def delete_asset(self, asset_id: int):
        return await delete_asset_db(asset_id)
    
    async def delete_assets(self):
        return await delete_assets_db()