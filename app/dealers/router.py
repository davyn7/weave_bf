# app/dealers/router.py

from fastapi import APIRouter

from app.dealers.schemas import (
    DealerBase,
    UserBase
)

from app.dealers.managers import (
    DealerManager,
    UserManager
)

router = APIRouter(prefix="/dealers", tags=["Dealers & Users"])

# Dealer Routers

@router.get("/dealers", tags=["Dealer"])
async def get_dealers():
    try:
        manager = DealerManager(None)
        return await manager.get_dealers()
    except Exception as e:
        raise e

@router.get("/dealers/{dealer_id}", tags=["Dealer"])
async def get_dealer(dealer_id: int):
    try:
        manager = DealerManager(None)
        return await manager.get_dealer(dealer_id)
    except Exception as e:
        raise e

@router.post("/add_dealer", tags=["Dealer"])
async def add_dealer(dealer: DealerBase):
    try:
        manager = DealerManager(dealer)
        return await manager.add_dealer()
    except Exception as e:
        raise e

@router.put("/update_dealer/{dealer_id}", tags=["Dealer"])
async def update_dealer(dealer_id: int, dealer: DealerBase):
    try:
        manager = DealerManager(dealer)
        return await manager.update_dealer(dealer_id)
    except Exception as e:
        raise e

@router.delete("/delete_dealer/{dealer_id}", tags=["Dealer"])
async def delete_dealer(dealer_id: int):
    try:
        manager = DealerManager(None)
        return await manager.delete_dealer(dealer_id)
    except Exception as e:
        raise e

@router.delete("/delete_dealers", tags=["Dealer"])
async def delete_dealers():
    try:
        manager = DealerManager(None)
        return await manager.delete_dealers()
    except Exception as e:
        raise e

# User Routers

@router.get("/users", tags=["User"])
async def get_users():
    try:
        manager = UserManager(None)
        return await manager.get_users()
    except Exception as e:
        raise e

@router.get("/users/{user_id}", tags=["User"])
async def get_user(user_id: int):
    try:
        manager = UserManager(None)
        return await manager.get_user(user_id)
    except Exception as e:
        raise e

@router.post("/add_user", tags=["User"])
async def add_user(user: UserBase, dealer_code: str):
    try:
        manager = UserManager(user)
        return await manager.add_user(dealer_code)
    except Exception as e:
        raise e

@router.put("/update_user/{user_id}", tags=["User"])
async def update_user(user_id: int, user: UserBase):
    try:
        manager = UserManager(user)
        return await manager.update_user(user_id)
    except Exception as e:
        raise e

@router.delete("/delete_user/{user_id}", tags=["User"])
async def delete_user(user_id: int):
    try:
        manager = UserManager(None)
        return await manager.delete_user(user_id)
    except Exception as e:
        raise e

@router.delete("/delete_users", tags=["User"])
async def delete_users():
    try:
        manager = UserManager(None)
        return await manager.delete_users()
    except Exception as e:
        raise e

@router.get("/new_users", tags=["User"])
async def get_new_users():
    try:
        manager = UserManager(None)
        return await manager.get_new_users()
    except Exception as e:
        raise e

@router.put("/approve_user/{user_id}", tags=["User"])
async def approve_user(user_id: int):
    try:
        manager = UserManager(None)
        return await manager.approve_user(user_id)
    except Exception as e:
        raise e