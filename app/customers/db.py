# app/customers/db.py

from app.connection import supabase
from app.customers.schemas import (
    CustomerBase,
    SpouseBase,
    GuarantorBase
)
from uuid import UUID

# Customer DB Operations

async def get_customers_db():
    response = supabase.table("CUSTOMERS").select("*").execute()
    return response.data

async def get_customer_db(customer_id: int):
    response = supabase.table("CUSTOMERS").select("*").eq("id", customer_id).execute()
    return response.data

async def add_customer_db(customer: CustomerBase):
    customer_data = customer.model_dump(mode="json")
    response = supabase.table("CUSTOMERS").insert(customer_data).execute()
    return response.data

async def update_customer_db(customer: CustomerBase, customer_id: int):
    customer_data = customer.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("CUSTOMERS").update(customer_data).eq("id", customer_id).execute()
    return response.data

async def delete_customer_db(customer_id: int):
    response = supabase.table("CUSTOMERS").delete().eq("id", customer_id).execute()
    return response.data

async def delete_customers_db():
    response = supabase.table("CUSTOMERS").delete().neq("id", 0).execute()
    return response.data

async def get_customers_by_user_id_db(user_id: int):
    response = supabase.table("CUSTOMERS").select("*").eq("USER_ID", user_id).execute()
    return response.data

# Spouse DB Operations

async def get_spouses_db():
    response = supabase.table("SPOUSES").select("*").execute()
    return response.data

async def get_spouse_db(spouse_id: int):
    response = supabase.table("SPOUSES").select("*").eq("id", spouse_id).execute()
    return response.data

async def add_spouse_db(spouse: SpouseBase):
    spouse_data = spouse.model_dump(mode="json")
    response = supabase.table("SPOUSES").insert(spouse_data).execute()
    return response.data

async def update_spouse_db(spouse: SpouseBase, spouse_id: int):
    spouse_data = spouse.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("SPOUSES").update(spouse_data).eq("id", spouse_id).execute()
    return response.data

async def delete_spouse_db(spouse_id: int):
    response = supabase.table("SPOUSES").delete().eq("id", spouse_id).execute()
    return response.data

async def delete_spouses_db():
    response = supabase.table("SPOUSES").delete().neq("id", 0).execute()
    return response.data

# Guarantor DB Operations

async def get_guarantors_db():
    response = supabase.table("GUARANTORS").select("*").execute()
    return response.data

async def get_guarantor_db(guarantor_id: int):
    response = supabase.table("GUARANTORS").select("*").eq("id", guarantor_id).execute()
    return response.data

async def add_guarantor_db(guarantor: GuarantorBase):
    guarantor_data = guarantor.model_dump(mode="json")
    response = supabase.table("GUARANTORS").insert(guarantor_data).execute()
    return response.data

async def update_guarantor_db(guarantor: GuarantorBase, guarantor_id: int):
    guarantor_data = guarantor.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("GUARANTORS").update(guarantor_data).eq("id", guarantor_id).execute()
    return response.data

async def delete_guarantor_db(guarantor_id: int):
    response = supabase.table("GUARANTORS").delete().eq("id", guarantor_id).execute()
    return response.data

async def delete_guarantors_db():
    response = supabase.table("GUARANTORS").delete().neq("id", 0).execute()
    return response.data