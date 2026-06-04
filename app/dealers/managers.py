# app/dealers/managers.py

from app.dealers.schemas import (
    DealerBase,
    UserBase
)
from app.dealers.db import (
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
    approve_user_db
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