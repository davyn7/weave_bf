from app.connection import supabase
from app.rates.schemas import (
    InterestRateBase,
    InsuranceBase
)
from uuid import UUID

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