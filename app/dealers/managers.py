# app/dealers/managers.py

from app.dealers.schemas import (
    DealerBase,
    SalespersonBase
)
from app.dealers.db import (
    get_dealers_db,
    get_dealer_db,
    add_dealer_db,
    update_dealer_db,
    delete_dealer_db,
    delete_dealers_db,
    get_dealer_by_code_db,
    get_salespersons_db,
    get_salesperson_db,
    add_salesperson_db,
    update_salesperson_db,
    delete_salesperson_db,
    delete_salespersons_db,
    get_new_salespersons_db,
    approve_salesperson_db
)
from uuid import UUID
from typing import Optional
import math
import random
import string

def generate_unique_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

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

class SalespersonManager:

    def __init__(self, salesperson: SalespersonBase):
        self.salesperson = salesperson

    async def get_salespersons(self):
        return await get_salespersons_db()
    
    async def get_salesperson(self, salesperson_id: int):
        return await get_salesperson_db(salesperson_id)

    async def add_salesperson(self, dealer_code: str):
        dealer = await get_dealer_by_code_db(dealer_code)
        self.salesperson.DEALER_ID = dealer["id"]
        return await add_salesperson_db(self.salesperson)
    
    async def update_salesperson(self, salesperson_id: int):
        return await update_salesperson_db(self.salesperson, salesperson_id)
    
    async def delete_salesperson(self, salesperson_id: int):
        return await delete_salesperson_db(salesperson_id)

    async def delete_salespersons(self):
        return await delete_salespersons_db()

    async def get_new_salespersons(self):
        return await get_new_salespersons_db()

    async def approve_salesperson(self, salesperson_id: int):
        unique_code = generate_unique_code()
        return await approve_salesperson_db(salesperson_id, unique_code)
