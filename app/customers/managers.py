# app/customers/managers.py

from app.customers.schemas import (
    CustomerBase,
    SpouseBase,
    GuarantorBase
)
from app.customers.db import (
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
    delete_guarantors_db
)
from uuid import UUID
from typing import Optional
import math
import random
import string

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