# app/buana/db.py

from app.connection import supabase
from app.buana.schemas import (
    BranchBase,
    CMOBase,
    AssetBase
)
from uuid import UUID

# Branch DB Operations

async def get_branches_db():
    response = supabase.table("BRANCHES").select("*").execute()
    return response.data

async def get_branch_db(branch_id: int):
    response = supabase.table("BRANCHES").select("*").eq("id", branch_id).execute()
    return response.data

async def add_branch_db(branch: BranchBase):
    branch_data = branch.model_dump(mode="json")
    response = supabase.table("BRANCHES").insert(branch_data).execute()
    return response.data

async def update_branch_db(branch: BranchBase, branch_id: int):
    branch_data = branch.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("BRANCHES").update(branch_data).eq("id", branch_id).execute()
    return response.data

async def delete_branch_db(branch_id: int):
    response = supabase.table("BRANCHES").delete().eq("id", branch_id).execute()
    return response.data

async def delete_branches_db():
    response = supabase.table("BRANCHES").delete().neq("id", 0).execute()
    return response.data

# CMO DB Operations

async def get_cmos_db():
    response = supabase.table("CMOS").select("*").execute()
    return response.data

async def get_cmo_db(cmo_id: int):
    response = supabase.table("CMOS").select("*").eq("id", cmo_id).execute()
    return response.data

async def add_cmo_db(cmo: CMOBase):
    cmo_data = cmo.model_dump(mode="json")
    response = supabase.table("CMOS").insert(cmo_data).execute()
    return response.data

async def update_cmo_db(cmo: CMOBase, cmo_id: int):
    cmo_data = cmo.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("CMOS").update(cmo_data).eq("id", cmo_id).execute()
    return response.data

async def delete_cmo_db(cmo_id: int):
    response = supabase.table("CMOS").delete().eq("id", cmo_id).execute()
    return response.data

async def delete_cmos_db():
    response = supabase.table("CMOS").delete().neq("id", 0).execute()
    return response.data

# Asset DB Operations

async def get_assets_db():
    response = supabase.table("ASSETS").select("*").execute()
    return response.data

async def get_asset_db(asset_id: int):
    response = supabase.table("ASSETS").select("*").eq("id", asset_id).execute()
    return response.data

async def add_asset_db(asset: AssetBase):
    asset_data = asset.model_dump(mode="json")
    response = supabase.table("ASSETS").insert(asset_data).execute()
    return response.data

async def update_asset_db(asset: AssetBase, asset_id: int):
    asset_data = asset.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("ASSETS").update(asset_data).eq("id", asset_id).execute()
    return response.data

async def delete_asset_db(asset_id: int):
    response = supabase.table("ASSETS").delete().eq("id", asset_id).execute()
    return response.data

async def delete_assets_db():
    response = supabase.table("ASSETS").delete().neq("id", 0).execute()
    return response.data