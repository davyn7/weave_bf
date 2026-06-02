# app/managers.py

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
    get_branches_db,
    get_branch_db,
    add_branch_db,
    update_branch_db,
    delete_branch_db,
    delete_branches_db,
    get_customers_db,
    get_customer_db,
    add_customer_db,
    update_customer_db,
    delete_customer_db,
    delete_customers_db,
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
    delete_guarantors_db
)
from app.helpers import generate_unique_code
from uuid import UUID
from typing import Optional

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