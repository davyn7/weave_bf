# app/managers.py

from app.schemas import (
    BranchBase,
    CMOBase,
    ApplicationBase,
    AssetBase
)
from app.db import (
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
    delete_cmos_db
)

# For Assets
from app.db import (
    get_assets_db,
    get_asset_db,
    add_asset_db,
    update_asset_db,
    delete_asset_db,
    delete_assets_db
)

# For Applications
from app.rates.db import (
    get_depreciation_rows_by_tenor_db,
    get_insurance_rate_by_fair_value_db
)
from app.db import (
    get_applications_db,
    get_application_db,
    add_application_db,
    update_application_db,
    delete_application_db,
    delete_applications_db,
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