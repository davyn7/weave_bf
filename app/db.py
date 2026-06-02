from app.connection import supabase
from app.schemas import (
    ProvinceBase,
    CityBase,
    KecamatanBase,
    KelurahanBase,
    InterestRateBase,
    BranchBase,
    CustomerBase,
    SpouseBase,
    GuarantorBase
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

# Interest Rate DB Operations

async def get_interest_rates_db():
    response = supabase.table("INTEREST_RATES").select("*").execute()
    return response.data

async def get_interest_rate_db(interest_rate_id: int):
    response = supabase.table("INTEREST_RATES").select("*").eq("id", interest_rate_id).execute()
    return response.data

async def add_interest_rate_db(interest_rate: InterestRateBase):
    interest_rate_data = interest_rate.model_dump(mode="json")
    response = supabase.table("INTEREST_RATES").insert(interest_rate_data).execute()
    return response.data

async def update_interest_rate_db(interest_rate: InterestRateBase, interest_rate_id: int):
    interest_rate_data = interest_rate.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("INTEREST_RATES").update(interest_rate_data).eq("id", interest_rate_id).execute()
    return response.data

async def delete_interest_rate_db(interest_rate_id: int):
    response = supabase.table("INTEREST_RATES").delete().eq("id", interest_rate_id).execute()
    return response.data

async def delete_interest_rates_db():
    response = supabase.table("INTEREST_RATES").delete().neq("id", 0).execute()
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
