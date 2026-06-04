# app/dealers/router.py

from fastapi import APIRouter

from app.dealers.schemas import (
    DealerBase,
    SalespersonBase
)

from app.dealers.managers import (
    DealerManager,
    SalespersonManager
)

router = APIRouter(prefix="/dealers", tags=["Dealers & Salespersons"])

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

# Salesperson Routers

@router.get("/salespersons", tags=["Salesperson"])
async def get_salespersons():
    try:
        manager = SalespersonManager(None)
        return await manager.get_salespersons()
    except Exception as e:
        raise e

@router.get("/salespersons/{salesperson_id}", tags=["Salesperson"])
async def get_salesperson(salesperson_id: int):
    try:
        manager = SalespersonManager(None)
        return await manager.get_salesperson(salesperson_id)
    except Exception as e:
        raise e

@router.post("/add_salesperson", tags=["Salesperson"])
async def add_salesperson(salesperson: SalespersonBase, dealer_code: str):
    try:
        manager = SalespersonManager(salesperson)
        return await manager.add_salesperson(dealer_code)
    except Exception as e:
        raise e

@router.put("/update_salesperson/{salesperson_id}", tags=["Salesperson"])
async def update_salesperson(salesperson_id: int, salesperson: SalespersonBase):
    try:
        manager = SalespersonManager(salesperson)
        return await manager.update_salesperson(salesperson_id)
    except Exception as e:
        raise e

@router.delete("/delete_salesperson/{salesperson_id}", tags=["Salesperson"])
async def delete_salesperson(salesperson_id: int):
    try:
        manager = SalespersonManager(None)
        return await manager.delete_salesperson(salesperson_id)
    except Exception as e:
        raise e

@router.delete("/delete_salespersons", tags=["Salesperson"])
async def delete_salespersons():
    try:
        manager = SalespersonManager(None)
        return await manager.delete_salespersons()
    except Exception as e:
        raise e

@router.get("/new_salespersons", tags=["Salesperson"])
async def get_new_salespersons():
    try:
        manager = SalespersonManager(None)
        return await manager.get_new_salespersons()
    except Exception as e:
        raise e

@router.put("/approve_salesperson/{salesperson_id}", tags=["Salesperson"])
async def approve_salesperson(salesperson_id: int):
    try:
        manager = SalespersonManager(None)
        return await manager.approve_salesperson(salesperson_id)
    except Exception as e:
        raise e
