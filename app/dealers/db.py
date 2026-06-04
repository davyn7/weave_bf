# app/dealers/db.py

from app.connection import supabase
from app.dealers.schemas import (
    DealerBase,
    SalespersonBase
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

# Salesperson DB Operations

async def get_salespersons_db():
    response = supabase.table("SALESPERSONS").select("*").execute()
    return response.data

async def get_salesperson_db(salesperson_id: int):
    response = supabase.table("SALESPERSONS").select("*").eq("id", salesperson_id).execute()
    return response.data

async def add_salesperson_db(salesperson: SalespersonBase):
    salesperson_data = salesperson.model_dump(mode="json")
    response = supabase.table("SALESPERSONS").insert(salesperson_data).execute()
    return response.data

async def update_salesperson_db(salesperson: SalespersonBase, salesperson_id: int):
    salesperson_data = salesperson.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("SALESPERSONS").update(salesperson_data).eq("id", salesperson_id).execute()
    return response.data

async def delete_salesperson_db(salesperson_id: int):
    response = supabase.table("SALESPERSONS").delete().eq("id", salesperson_id).execute()
    return response.data

async def delete_salespersons_db():
    response = supabase.table("SALESPERSONS").delete().neq("id", 0).execute()
    return response.data

async def get_new_salespersons_db():
    response = supabase.table("SALESPERSONS").select("*").eq("IS_ACTIVE", False).execute()
    return response.data

async def approve_salesperson_db(salesperson_id: int, unique_code: str):
    response = supabase.table("SALESPERSONS").update({"IS_ACTIVE": True, "UNIQUE_CODE": unique_code}).eq("id", salesperson_id).execute()
    return response.data
