# app/seed_data.py

from app.db import (
    add_province_db,
    add_city_db,
    add_kecamatan_db,
    add_kelurahan_db,
    add_interest_rate_db,
    add_insurance_db,
    add_branch_db,
    add_cmo_db,
    add_dealer_db,
    add_user_db,
    add_customer_db,
    add_spouse_db,
    add_guarantor_db,
    add_asset_db,
    add_application_db
)
from app.schemas import (
    ProvinceBase,
    CityBase,
    KecamatanBase,
    KelurahanBase,
    InterestRateBase,
    InsuranceBase,
    DealerBase,
    UserBase,
    CustomerBase,
    SpouseBase,
    GuarantorBase,
    AssetBase,
    ApplicationBase
)

async def seed_data():
    await add_province_db(ProvinceBase(NAME="Jakarta"))
    await add_city_db(CityBase(NAME="Jakarta Selatan", PROVINCE_ID=1))