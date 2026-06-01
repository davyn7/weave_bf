from app.connection import supabase
from app.schemas import (
    CustomerBase,
    ProvinceBase,
    CityBase,
    KecamatanBase,
    KelurahanBase,
    BranchBase
)
from uuid import UUID

# Location DB Operations

async def add_province_db(province: ProvinceBase):
    province_data = province.model_dump(mode="json")
    response = supabase.table("PROVINCES").insert(province_data).execute()
    return response.data

async def add_city_db(city: CityBase):
    city_data = city.model_dump(mode="json")
    response = supabase.table("CITIES").insert(city_data).execute()
    return response.data

async def add_kecamatan_db(kecamatan: KecamatanBase):
    kecamatan_data = kecamatan.model_dump(mode="json")
    response = supabase.table("KECAMATAN").insert(kecamatan_data).execute()
    return response.data

async def add_kelurahan_db(kelurahan: KelurahanBase):
    kelurahan_data = kelurahan.model_dump(mode="json")
    response = supabase.table("KELURAHAN").insert(kelurahan_data).execute()
    return response.data

# Location Search DB Operations

async def get_cities_db(province_id: int):
    response = supabase.table("CITIES").select("*").eq("PROVINCE_ID", province_id).execute()
    return response.data

async def get_kecamatans_db(city_id: int):
    response = supabase.table("KECAMATAN").select("*").eq("CITY_ID", city_id).execute()
    return response.data

async def get_kelurahans_db(kecamatan_id: int):
    response = supabase.table("KELURAHAN").select("*").eq("KECAMATAN_ID", kecamatan_id).execute()
    return response.data

async def get_postal_code_db(kelurahan_id: int):
    response = supabase.table("KELURAHAN").select("POSTAL_CODE").eq("id", kelurahan_id).execute()
    return response.data

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