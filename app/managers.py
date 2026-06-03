# app/managers.py

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
from app.db import (
    add_province_db,
    add_city_db,
    add_kecamatan_db,
    add_kelurahan_db,
    get_cities_db,
    get_kecamatans_db,
    get_kelurahans_db,
    get_postal_code_db,
    get_interest_rates_db,
    get_interest_rate_db,
    add_interest_rate_db,
    update_interest_rate_db,
    delete_interest_rate_db,
    delete_interest_rates_db,
    update_interest_rate_field_by_conditions_db,
    get_interest_rate_by_conditions_db,
    get_insurances_db,
    get_insurance_db,
    add_insurance_db,
    update_insurance_db,
    delete_insurance_db,
    delete_insurances_db,
    get_depreciation_rows_by_tenor_db,
    get_insurance_rate_by_fair_value_db,
    get_branches_db,
    get_branch_db,
    add_branch_db,
    update_branch_db,
    delete_branch_db,
    delete_branches_db,
    get_cmos_db,
    get_cmo_db,
    add_cmo_db,
    update_cmo_db,
    delete_cmo_db,
    delete_cmos_db,
    get_dealers_db,
    get_dealer_db,
    add_dealer_db,
    update_dealer_db,
    delete_dealer_db,
    delete_dealers_db,
    get_dealer_by_code_db,
    get_users_db,
    get_user_db,
    add_user_db,
    update_user_db,
    delete_user_db,
    delete_users_db,
    get_new_users_db,
    approve_user_db,
    get_customers_db,
    get_customer_db,
    add_customer_db,
    update_customer_db,
    delete_customer_db,
    delete_customers_db,
    get_customers_by_user_id_db,
    get_spouses_db,
    get_spouse_db,
    add_spouse_db,
    update_spouse_db,
    delete_spouse_db,
    delete_spouses_db,
    get_guarantors_db,
    get_guarantor_db,
    add_guarantor_db,
    update_guarantor_db,
    delete_guarantor_db,
    delete_guarantors_db,
    get_applications_db,
    get_application_db,
    add_application_db,
    update_application_db,
    delete_application_db,
    delete_applications_db,
    get_assets_db,
    get_asset_db,
    add_asset_db,
    update_asset_db,
    delete_asset_db,
    delete_assets_db
)
from uuid import UUID
from typing import Optional
import math
import random
import string

def generate_unique_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

class TestManager:

    def __init__(self):
        pass

    async def test(self):
        return "Hello, World!"

class LocationManager:

    def __init__(self, province: Optional[ProvinceBase] = None, city: Optional[CityBase] = None, kecamatan: Optional[KecamatanBase] = None, kelurahan: Optional[KelurahanBase] = None):
        self.province = province
        self.city = city
        self.kecamatan = kecamatan
        self.kelurahan = kelurahan

    async def add_province(self):
        return await add_province_db(self.province)    

    async def add_city(self):
        return await add_city_db(self.city)

    async def add_kecamatan(self):
        return await add_kecamatan_db(self.kecamatan)

    async def add_kelurahan(self):
        return await add_kelurahan_db(self.kelurahan)

class LocationSearchManager:

    def __init__(self, province_id: Optional[int] = None, city_id: Optional[int] = None, kecamatan_id: Optional[int] = None, kelurahan_id: Optional[int] = None):
        self.province_id = province_id
        self.city_id = city_id
        self.kecamatan_id = kecamatan_id
        self.kelurahan_id = kelurahan_id

    async def get_cities(self):
        return await get_cities_db(self.province_id)

    async def get_kecamatans(self):
        return await get_kecamatans_db(self.city_id)

    async def get_kelurahans(self):
        return await get_kelurahans_db(self.kecamatan_id)

    async def get_postal_code(self):
        return await get_postal_code_db(self.kelurahan_id)

class InterestRateManager:

    def __init__(self, interest_rate: InterestRateBase):
        self.interest_rate = interest_rate

    async def get_interest_rates(self):
        return await get_interest_rates_db()
    
    async def get_interest_rate(self, interest_rate_id: int):
        return await get_interest_rate_db(interest_rate_id)

    async def add_interest_rate(self):
        return await add_interest_rate_db(self.interest_rate)

    async def update_interest_rate(self, interest_rate_id: int):
        return await update_interest_rate_db(self.interest_rate, interest_rate_id)

    async def delete_interest_rate(self, interest_rate_id: int):
        return await delete_interest_rate_db(interest_rate_id)

    async def delete_interest_rates(self):
        return await delete_interest_rates_db()
    
    async def update_interest_rate_field_by_conditions(self, update_data: dict, conditions: dict):
        return await update_interest_rate_field_by_conditions_db(update_data, conditions)

class InsuranceManager:

    def __init__(self, insurance: InsuranceBase):
        self.insurance = insurance

    async def get_insurances(self):
        return await get_insurances_db()
    
    async def get_insurance(self, insurance_id: int):
        return await get_insurance_db(insurance_id)

    async def add_insurance(self):
        return await add_insurance_db(self.insurance)
    
    async def update_insurance(self, insurance_id: int):
        return await update_insurance_db(self.insurance, insurance_id)
    
    async def delete_insurance(self, insurance_id: int):
        return await delete_insurance_db(insurance_id)

    async def delete_insurances(self):
        return await delete_insurances_db()

class BranchManager:

    def __init__(self, branch: BranchBase):
        self.branch = branch

    async def get_branches(self):
        return await get_branches_db()

    async def get_branch(self, branch_id: int):
        return await get_branch_db(branch_id)

    async def add_branch(self):
        return await add_branch_db(self.branch)

    async def update_branch(self, branch_id: int):
        return await update_branch_db(self.branch, branch_id)

    async def delete_branch(self, branch_id: int):
        return await delete_branch_db(branch_id)

    async def delete_branches(self):
        return await delete_branches_db()

class CMOManager:

    def __init__(self, cmo: CMOBase):
        self.cmo = cmo

    async def get_cmos(self):
        return await get_cmos_db()
    
    async def get_cmo(self, cmo_id: int):
        return await get_cmo_db(cmo_id)

    async def add_cmo(self):
        return await add_cmo_db(self.cmo)
    
    async def update_cmo(self, cmo_id: int):
        return await update_cmo_db(self.cmo, cmo_id)
    
    async def delete_cmo(self, cmo_id: int):
        return await delete_cmo_db(cmo_id)
    async def delete_cmos(self):
        return await delete_cmos_db()

class DealerManager:

    def __init__(self, dealer: DealerBase):
        self.dealer = dealer

    async def get_dealers(self):
        return await get_dealers_db()
    
    async def get_dealer(self, dealer_id: int):
        return await get_dealer_db(dealer_id)

    async def add_dealer(self):
        self.dealer.UNIQUE_CODE = generate_unique_code()
        return await add_dealer_db(self.dealer)
    
    async def update_dealer(self, dealer_id: int):
        return await update_dealer_db(self.dealer, dealer_id)
    
    async def delete_dealer(self, dealer_id: int):
        return await delete_dealer_db(dealer_id)

    async def delete_dealers(self):
        return await delete_dealers_db()

class UserManager:

    def __init__(self, user: UserBase):
        self.user = user

    async def get_users(self):
        return await get_users_db()
    
    async def get_user(self, user_id: int):
        return await get_user_db(user_id)

    async def add_user(self, dealer_code: str):
        dealer = await get_dealer_by_code_db(dealer_code)
        self.user.DEALER_ID = dealer["id"]
        return await add_user_db(self.user)
    
    async def update_user(self, user_id: int):
        return await update_user_db(self.user, user_id)
    
    async def delete_user(self, user_id: int):
        return await delete_user_db(user_id)

    async def delete_users(self):
        return await delete_users_db()

    async def get_new_users(self):
        return await get_new_users_db()

    async def approve_user(self, user_id: int):
        unique_code = generate_unique_code()
        return await approve_user_db(user_id, unique_code)

class CustomerManager:

    def __init__(self, customer: CustomerBase):
        self.customer = customer

    async def get_customers(self):
        return await get_customers_db()

    async def get_customer(self, customer_id: int):
        return await get_customer_db(customer_id)

    async def add_customer(self):
        return await add_customer_db(self.customer)
    
    async def update_customer(self, customer_id: int):
        return await update_customer_db(self.customer, customer_id)
    
    async def delete_customer(self, customer_id: int):
        return await delete_customer_db(customer_id)

    async def delete_customers(self):
        return await delete_customers_db()

    async def get_customers_by_user_id(self, user_id: int):
        return await get_customers_by_user_id_db(user_id)

class SpouseManager:

    def __init__(self, spouse: SpouseBase):
        self.spouse = spouse

    async def get_spouses(self):
        return await get_spouses_db()

    async def get_spouse(self, spouse_id: int):
        return await get_spouse_db(spouse_id)

    async def add_spouse(self):
        return await add_spouse_db(self.spouse)

    async def update_spouse(self, spouse_id: int):
        return await update_spouse_db(self.spouse, spouse_id)

    async def delete_spouse(self, spouse_id: int):
        return await delete_spouse_db(spouse_id)

    async def delete_spouses(self):
        return await delete_spouses_db()

class GuarantorManager:

    def __init__(self, guarantor: GuarantorBase):
        self.guarantor = guarantor

    async def get_guarantors(self):
        return await get_guarantors_db()

    async def get_guarantor(self, guarantor_id: int):
        return await get_guarantor_db(guarantor_id)

    async def add_guarantor(self):
        return await add_guarantor_db(self.guarantor)

    async def update_guarantor(self, guarantor_id: int):
        return await update_guarantor_db(self.guarantor, guarantor_id)

    async def delete_guarantor(self, guarantor_id: int):
        return await delete_guarantor_db(guarantor_id)

    async def delete_guarantors(self):
        return await delete_guarantors_db()

class ApplicationManager:

    def __init__(self, application: ApplicationBase):
        self.application = application

    async def application_credit_simulation(self):
        return await credit_simulation(self.application)

    async def get_applications(self):
        return await get_applications_db()

    async def get_application(self, application_id: int):
        return await get_application_db(application_id)

    async def add_application(self):
        return await add_application_db(self.application)

    async def update_application(self, application_id: int):
        return await update_application_db(self.application, application_id)

    async def delete_application(self, application_id: int):
        return await delete_application_db(application_id)

    async def delete_applications(self):
        return await delete_applications_db()

    async def calculate_insurance_rate(self, OTR: float, province_id: int, TENOR_YEAR: int, TYPE: str):
        depreciation_rows = await get_depreciation_rows_by_tenor_db(TENOR_YEAR, TYPE)

        if not depreciation_rows:
            return {
                "CUMULATIVE_RATE": None,
                "message": "No depreciation data found",
            }

        fair_values = []

        for row in depreciation_rows:
            year = row["TENOR_YEAR"]
            depreciation = row["DEPRECIATION"]
            fair_value = OTR * depreciation

            fair_values.append({
                "YEAR": year,
                "VALUE": [
                    fair_value,
                    depreciation,
                ],
            })

        cumulative_rate = 0

        for item in fair_values:
            year = item["YEAR"]
            fair_value = item["VALUE"][0]
            depreciation = item["VALUE"][1]

            insurance_rows = await get_insurance_rate_by_fair_value_db(
                province_id=province_id,
                fair_value=fair_value,
            )

            if not insurance_rows:
                return {
                    "CUMULATIVE_RATE": None,
                    "message": f"No insurance rate found for year {year}",
                    "YEAR": year,
                    "FAIR_VALUE": fair_value,
                }

            base_rate = insurance_rows[0]["RATE"]

            if cumulative_rate == 0:
                cumulative_rate = base_rate
            else:
                cumulative_rate += base_rate * depreciation

        return cumulative_rate
    
    async def test_application_credit_simulation(
        self,
        OTR: int,
        DP: int,
        TENOR_YEAR: int,
        TENOR_MONTH: int,
        TYPE: str,
        PROVINCE_ID: int,
        PROVISION: int = 0
    ):
        interest_rate_object = await get_interest_rate_by_conditions_db({"TYPE": TYPE, "TENOR_YEAR": TENOR_YEAR})
        interest_rate_object = interest_rate_object[0]
        INTEREST_RATE = interest_rate_object["RATE"]
        TJH = interest_rate_object["TJH"]
        ADMIN = interest_rate_object["ADMIN_FEE"] + interest_rate_object["FIDUCIAL_FEE"] + interest_rate_object["INSURANCE_POLICY_FEE"]
        INSURANCE_RATE = await self.calculate_insurance_rate(OTR, PROVINCE_ID, TENOR_YEAR, TYPE)
        INSURANCE = OTR * INSURANCE_RATE + TJH
        PRINCIPAL = OTR - DP + INSURANCE + PROVISION
        INTEREST = math.ceil((PRINCIPAL * INTEREST_RATE * TENOR_YEAR) / 1000) * 1000
        MONTHLY_PAYMENT = math.ceil((PRINCIPAL + INTEREST) / TENOR_MONTH / 500.0) * 500
        ret = {
            "OTR": OTR,
            "DP": DP,
            "INSURANCE": INSURANCE,
            "PROVISION": PROVISION,
            "PRINCIPAL": PRINCIPAL,
            "MONTHLY_PAYMENT": MONTHLY_PAYMENT,
            "TENOR": TENOR_MONTH - 1,
            "FLAT_RATE": INTEREST_RATE,
            "ADMIN_FEE": ADMIN,
            "FIRST_PAYMENT": DP + MONTHLY_PAYMENT + ADMIN
        }
        return ret

    async def application_credit_simulation(
        self,
        PROVISION: int = 0
    ):
        OTR = self.application.OTR
        DP = self.application.DP
        TENOR_YEAR = self.application.TENOR_YEAR
        TENOR_MONTH = self.application.TENOR_MONTH
        dealer = await get_dealer_db(self.application.DEALER_ID)
        dealer = dealer[0]
        asset = await get_asset_db(self.application.ASSET_ID)
        asset = asset[0]
        interest_rate_object = await get_interest_rate_by_conditions_db({"TYPE": asset["CONDITION"], "TENOR_YEAR": TENOR_YEAR})
        interest_rate_object = interest_rate_object[0]
        INTEREST_RATE = interest_rate_object["RATE"]
        TJH = interest_rate_object["TJH"]
        ADMIN = interest_rate_object["ADMIN_FEE"] + interest_rate_object["FIDUCIAL_FEE"] + interest_rate_object["INSURANCE_POLICY_FEE"]
        INSURANCE_RATE = await self.calculate_insurance_rate(OTR, dealer["PROVINCE_ID"], TENOR_YEAR, asset["CONDITION"])
        INSURANCE = OTR * INSURANCE_RATE + TJH
        PRINCIPAL = OTR - DP + INSURANCE + PROVISION
        INTEREST = math.ceil((PRINCIPAL * INTEREST_RATE * TENOR_YEAR) / 1000) * 1000
        MONTHLY_PAYMENT = math.ceil((PRINCIPAL + INTEREST) / TENOR_MONTH / 500.0) * 500
        ret = {
            "OTR": OTR,
            "DP": DP,
            "INSURANCE": INSURANCE,
            "PROVISION": PROVISION,
            "PRINCIPAL": PRINCIPAL,
            "MONTHLY_PAYMENT": MONTHLY_PAYMENT,
            "TENOR": TENOR_MONTH - 1,
            "FLAT_RATE": INTEREST_RATE,
            "ADMIN_FEE": ADMIN,
            "FIRST_PAYMENT": DP + MONTHLY_PAYMENT + ADMIN
        }
        return ret
        
class AssetManager:

    def __init__(self, asset: AssetBase):
        self.asset = asset

    async def get_assets(self):
        return await get_assets_db()
    
    async def get_asset(self, asset_id: int):
        return await get_asset_db(asset_id)

    async def add_asset(self):
        return await add_asset_db(self.asset)
    
    async def update_asset(self, asset_id: int):
        return await update_asset_db(self.asset, asset_id)
    
    async def delete_asset(self, asset_id: int):
        return await delete_asset_db(asset_id)
    
    async def delete_assets(self):
        return await delete_assets_db()