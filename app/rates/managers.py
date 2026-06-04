# app/rates/managers.py

from app.rates.schemas import (
    InterestRateBase,
    InsuranceBase,
    InsuranceSpec,
    BatchAddInsurancesRequest
)
from app.rates.db import (
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
    get_insurance_rate_by_fair_value_db
)
from uuid import UUID
from typing import Optional
import math
import random
import string

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

    async def batch_add_insurances(self, provinces: list[int], specs: list[InsuranceSpec]):
        for province_id in provinces:
            for spec in specs:
                insurance = InsuranceBase(
                    PROVINCE_ID=province_id,
                    UPPER_LIMIT=spec.UPPER_LIMIT,
                    LOWER_LIMIT=spec.LOWER_LIMIT,
                    RATE=spec.RATE,
                )
                await add_insurance_db(insurance)