from app.connection import supabase
from app.schemas import (
    BranchBase,
    CMOBase,
    DealerBase,
    UserBase,
    ApplicationBase,
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

# Dealer DB Operations

async def get_dealers_db():
    response = supabase.table("DEALERS").select("*").execute()
    return response.data

async def get_dealer_db(dealer_id: int):
    response = supabase.table("DEALERS").select("*").eq("id", dealer_id).execute()
    return response.data

async def add_dealer_db(dealer: DealerBase):
    dealer_data = dealer.model_dump(mode="json")
    response = supabase.table("DEALERS").insert(dealer_data).execute()
    return response.data

async def update_dealer_db(dealer: DealerBase, dealer_id: int):
    dealer_data = dealer.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("DEALERS").update(dealer_data).eq("id", dealer_id).execute()
    return response.data

async def delete_dealer_db(dealer_id: int):
    response = supabase.table("DEALERS").delete().eq("id", dealer_id).execute()
    return response.data

async def delete_dealers_db():
    response = supabase.table("DEALERS").delete().neq("id", 0).execute()
    return response.data

async def get_dealer_by_code_db(dealer_code: str):
    response = supabase.table("DEALERS").select("*").eq("UNIQUE_CODE", dealer_code).execute()
    return response.data[0]

# User DB Operations

async def get_users_db():
    response = supabase.table("USERS").select("*").execute()
    return response.data

async def get_user_db(user_id: int):
    response = supabase.table("USERS").select("*").eq("id", user_id).execute()
    return response.data

async def add_user_db(user: UserBase):
    user_data = user.model_dump(mode="json")
    response = supabase.table("USERS").insert(user_data).execute()
    return response.data

async def update_user_db(user: UserBase, user_id: int):
    user_data = user.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("USERS").update(user_data).eq("id", user_id).execute()
    return response.data

async def delete_user_db(user_id: int):
    response = supabase.table("USERS").delete().eq("id", user_id).execute()
    return response.data

async def delete_users_db():
    response = supabase.table("USERS").delete().neq("id", 0).execute()
    return response.data

async def get_new_users_db():
    response = supabase.table("USERS").select("*").eq("IS_ACTIVE", False).execute()
    return response.data

async def approve_user_db(user_id: int, unique_code: str):
    response = supabase.table("USERS").update({"IS_ACTIVE": True, "UNIQUE_CODE": unique_code}).eq("id", user_id).execute()
    return response.data

# Application DB Operations

async def get_applications_db():
    response = supabase.table("APPLICATIONS").select("*").execute()
    return response.data

async def get_application_db(application_id: int):
    response = supabase.table("APPLICATIONS").select("*").eq("id", application_id).execute()
    return response.data

async def add_application_db(application: ApplicationBase):
    application_data = application.model_dump(mode="json")
    response = supabase.table("APPLICATIONS").insert(application_data).execute()
    return response.data

async def update_application_db(application: ApplicationBase, application_id: int):
    application_data = application.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("APPLICATIONS").update(application_data).eq("id", application_id).execute()
    return response.data

async def delete_application_db(application_id: int):
    response = supabase.table("APPLICATIONS").delete().eq("id", application_id).execute()
    return response.data

async def delete_applications_db():
    response = supabase.table("APPLICATIONS").delete().neq("id", 0).execute()
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