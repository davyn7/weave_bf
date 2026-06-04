# app/dealers/db.py

from app.connection import supabase
from app.dealers.schemas import (
    DealerBase,
    UserBase
)
from uuid import UUID

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