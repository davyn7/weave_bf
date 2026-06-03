from app.connection import supabase
from app.schemas import (
    ProvinceBase,
    CityBase,
    KecamatanBase,
    KelurahanBase,
    InterestRateBase,
    InsuranceBase,
    BranchBase,
    CMOBase,
    DealerBase,
    UserBase,
    CustomerBase,
    SpouseBase,
    GuarantorBase,
    ApplicationBase,
    AssetBase
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

async def update_interest_rate_field_by_conditions_db(
    update_data: dict,
    conditions: dict,
):
    query = supabase.table("INTEREST_RATES").update(update_data)

    for column, value in conditions.items():
        query = query.eq(column, value)

    response = query.execute()
    return response.data

async def get_interest_rate_by_conditions_db(conditions: dict):
    query = supabase.table("INTEREST_RATES").select("*")
    for column, value in conditions.items():
        query = query.eq(column, value)
    response = query.execute()
    return response.data

# Insurance DB Operations

async def get_insurances_db():
    response = supabase.table("INSURANCES").select("*").execute()
    return response.data

async def get_insurance_db(insurance_id: int):
    response = supabase.table("INSURANCES").select("*").eq("id", insurance_id).execute()
    return response.data

async def add_insurance_db(insurance: InsuranceBase):
    insurance_data = insurance.model_dump(mode="json")
    response = supabase.table("INSURANCES").insert(insurance_data).execute()
    return response.data

async def update_insurance_db(insurance: InsuranceBase, insurance_id: int):
    insurance_data = insurance.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("INSURANCES").update(insurance_data).eq("id", insurance_id).execute()
    return response.data

async def delete_insurance_db(insurance_id: int):
    response = supabase.table("INSURANCES").delete().eq("id", insurance_id).execute()
    return response.data

async def delete_insurances_db():
    response = supabase.table("INSURANCES").delete().neq("id", 0).execute()
    return response.data

async def get_depreciation_rows_by_tenor_db(tenor_year: int, TYPE: str):
    response = (
        supabase
        .table("INTEREST_RATES")
        .select("TENOR_YEAR, DEPRECIATION")
        .eq("TYPE", TYPE)
        .lte("TENOR_YEAR", tenor_year)
        .order("TENOR_YEAR", desc=False)
        .execute()
    )

    return response.data


async def get_insurance_rate_by_fair_value_db(
    province_id: int,
    fair_value: float,
):
    response = (
        supabase
        .table("INSURANCES")
        .select("RATE, LOWER_LIMIT, UPPER_LIMIT")
        .eq("PROVINCE_ID", province_id)
        .lte("LOWER_LIMIT", fair_value)
        .gte("UPPER_LIMIT", fair_value)
        .limit(1)
        .execute()
    )

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