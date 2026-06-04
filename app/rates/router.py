# app/rates/router.py

from fastapi import APIRouter

from app.rates.schemas import (
    InterestRateBase,
    InsuranceBase,
    InsuranceSpec,
    BatchAddInsurancesRequest
)

from app.rates.managers import (
    InterestRateManager,
    InsuranceManager
)

router = APIRouter(prefix="/rates", tags=["Interest & Insurance"])

# Interest Rate Routers

@router.get("/interest_rates")
async def get_interest_rates():
    try:
        manager = InterestRateManager(None)
        return await manager.get_interest_rates()
    except Exception as e:
        raise e

@router.get("/interest_rates/{interest_rate_id}")
async def get_interest_rate(interest_rate_id: int):
    try:
        manager = InterestRateManager(None)
        return await manager.get_interest_rate(interest_rate_id)
    except Exception as e:
        raise e

@router.post("/add_interest_rate")
async def add_interest_rate(interest_rate: InterestRateBase):
    try:
        manager = InterestRateManager(interest_rate)
        return await manager.add_interest_rate()
    except Exception as e:
        raise e

@router.put("/update_interest_rate/{interest_rate_id}")
async def update_interest_rate(interest_rate_id: int, interest_rate: InterestRateBase):
    try:
        manager = InterestRateManager(interest_rate)
        return await manager.update_interest_rate(interest_rate_id)
    except Exception as e:
        raise e

@router.delete("/delete_interest_rate/{interest_rate_id}")
async def delete_interest_rate(interest_rate_id: int):
    try:
        manager = InterestRateManager(None)
        return await manager.delete_interest_rate(interest_rate_id)
    except Exception as e:
        raise e

@router.delete("/delete_interest_rates")
async def delete_interest_rates():
    try:
        manager = InterestRateManager(None)
        return await manager.delete_interest_rates()
    except Exception as e:
        raise e

@router.put("/update_interest_rate_field_by_conditions")
async def update_interest_rate_field_by_conditions(update_data: dict, conditions: dict):
    try:
        manager = InterestRateManager(None)
        return await manager.update_interest_rate_field_by_conditions(update_data, conditions)
    except Exception as e:
        raise e

# Insurance Routers

@router.get("/insurances")
async def get_insurances():
    try:
        manager = InsuranceManager(None)
        return await manager.get_insurances()
    except Exception as e:
        raise e

@router.get("/insurances/{insurance_id}")
async def get_insurance(insurance_id: int):
    try:
        manager = InsuranceManager(None)
        return await manager.get_insurance(insurance_id)
    except Exception as e:
        raise e

@router.post("/add_insurance")
async def add_insurance(insurance: InsuranceBase):
    try:
        manager = InsuranceManager(insurance)
        return await manager.add_insurance()
    except Exception as e:
        raise e

@router.put("/update_insurance/{insurance_id}")
async def update_insurance(insurance_id: int, insurance: InsuranceBase):
    try:
        manager = InsuranceManager(insurance)
        return await manager.update_insurance(insurance_id)
    except Exception as e:
        raise e

@router.delete("/delete_insurance/{insurance_id}")
async def delete_insurance(insurance_id: int):
    try:
        manager = InsuranceManager(None)
        return await manager.delete_insurance(insurance_id)
    except Exception as e:
        raise e

@router.delete("/delete_insurances")
async def delete_insurances():
    try:
        manager = InsuranceManager(None)
        return await manager.delete_insurances()
    except Exception as e:
        raise e

@router.post("/batch_add_insurances")
async def batch_add_insurances(payload: BatchAddInsurancesRequest):
    try:
        manager = InsuranceManager(None)
        return await manager.batch_add_insurances(payload.provinces, payload.specs)
    except Exception as e:
        raise e