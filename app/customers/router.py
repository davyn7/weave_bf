# app/customers/router.py

from fastapi import APIRouter

from app.customers.schemas import (
    CustomerBase,
    SpouseBase,
    GuarantorBase
)

from app.customers.managers import (
    CustomerManager,
    SpouseManager,
    GuarantorManager
)

router = APIRouter(prefix="/customers", tags=["Customers"])

# Customer Routers

@router.get("/customers")
async def get_customers():
    try:
        manager = CustomerManager(None)
        return await manager.get_customers()
    except Exception as e:
        raise e

@router.get("/customers/{customer_id}")
async def get_customer(customer_id: int):
    try:
        manager = CustomerManager(None)
        return await manager.get_customer(customer_id)
    except Exception as e:
        raise e

@router.post("/add_customer")
async def add_customer(customer: CustomerBase):
    try:
        manager = CustomerManager(customer)
        return await manager.add_customer()
    except Exception as e:
        raise e

@router.put("/update_customer/{customer_id}")
async def update_customer(customer_id: int, customer: CustomerBase):
    try:
        manager = CustomerManager(customer)
        return await manager.update_customer(customer_id)
    except Exception as e:
        raise e

@router.delete("/delete_customer/{customer_id}")
async def delete_customer(customer_id: int):
    try:
        manager = CustomerManager(None)
        return await manager.delete_customer(customer_id)
    except Exception as e:
        raise e

@router.delete("/delete_customers")
async def delete_customers():
    try:
        manager = CustomerManager(None)
        return await manager.delete_customers()
    except Exception as e:
        raise e

@router.get("/customers_by_salesperson_id/{salesperson_id}")
async def get_customers_by_salesperson_id(salesperson_id: int):
    try:
        manager = CustomerManager(None)
        return await manager.get_customers_by_salesperson_id(salesperson_id)
    except Exception as e:
        raise e

# Spouse Routers

@router.get("/spouses")
async def get_spouses():
    try:
        manager = SpouseManager(None)
        return await manager.get_spouses()
    except Exception as e:
        raise e

@router.get("/spouses/{spouse_id}")
async def get_spouse(spouse_id: int):
    try:
        manager = SpouseManager(None)
        return await manager.get_spouse(spouse_id)
    except Exception as e:
        raise e

@router.post("/add_spouse")
async def add_spouse(spouse: SpouseBase):
    try:
        manager = SpouseManager(spouse)
        return await manager.add_spouse()
    except Exception as e:
        raise e

@router.put("/update_spouse/{spouse_id}")
async def update_spouse(spouse_id: int, spouse: SpouseBase):
    try:
        manager = SpouseManager(spouse)
        return await manager.update_spouse(spouse_id)
    except Exception as e:
        raise e

@router.delete("/delete_spouse/{spouse_id}")
async def delete_spouse(spouse_id: int):
    try:
        manager = SpouseManager(None)
        return await manager.delete_spouse(spouse_id)
    except Exception as e:
        raise e

@router.delete("/delete_spouses")
async def delete_spouses():
    try:
        manager = SpouseManager(None)
        return await manager.delete_spouses()
    except Exception as e:
        raise e

# Guarantor Routers

@router.get("/guarantors")
async def get_guarantors():
    try:
        manager = GuarantorManager(None)
        return await manager.get_guarantors()
    except Exception as e:
        raise e

@router.get("/guarantors/{guarantor_id}")
async def get_guarantor(guarantor_id: int):
    try:
        manager = GuarantorManager(None)
        return await manager.get_guarantor(guarantor_id)
    except Exception as e:
        raise e

@router.post("/add_guarantor")
async def add_guarantor(guarantor: GuarantorBase): 
    try:
        manager = GuarantorManager(guarantor)
        return await manager.add_guarantor()
    except Exception as e:
        raise e

@router.put("/update_guarantor/{guarantor_id}")
async def update_guarantor(guarantor_id: int, guarantor: GuarantorBase):
    try:
        manager = GuarantorManager(guarantor)
        return await manager.update_guarantor(guarantor_id)
    except Exception as e:
        raise e

@router.delete("/delete_guarantor/{guarantor_id}")
async def delete_guarantor(guarantor_id: int):
    try:
        manager = GuarantorManager(None)
        return await manager.delete_guarantor(guarantor_id)
    except Exception as e:
        raise e

@router.delete("/delete_guarantors")
async def delete_guarantors():
    try:
        manager = GuarantorManager(None)
        return await manager.delete_guarantors()
    except Exception as e:
        raise e