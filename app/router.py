# app/router.py

from fastapi import APIRouter
from app.managers import (
    TestManager,
    LocationManager,
    LocationSearchManager,
    InterestRateManager,
    InsuranceManager,
    BranchManager,
    CMOManager,
    DealerManager,
    UserManager,
    CustomerManager,
    SpouseManager,
    GuarantorManager,
    ApplicationManager,
    AssetManager
)
from app.schemas import (
    ProvinceBase,
    CityBase,
    KecamatanBase,
    KelurahanBase,
    InterestRateBase,
    InsuranceBase,
    BranchBase,
    CMOBase,
    DealerBase,
    UserBase,
    CustomerBase,
    SpouseBase,
    GuarantorBase,
    ApplicationBase,
    AssetBase
)
from pydantic import BaseModel
from uuid import UUID

router = APIRouter()

# Initialize DB Testing

@router.post("/populate", tags=["Testing"])
async def populate():
    pass

@router.delete("/clear", tags=["Testing"])
async def clear():
    pass

# Location Routers

@router.post("/add_province", tags=["Location"])
async def add_province(province: ProvinceBase):
    try:
        manager = LocationManager(province=province)
        return await manager.add_province()
    except Exception as e:
        raise e

@router.post("/add_city", tags=["Location"])
async def add_city(city: CityBase):
    try:
        manager = LocationManager(city=city)
        return await manager.add_city()
    except Exception as e:
        raise e

@router.post("/add_kecamatan", tags=["Location"])
async def add_kecamatan(kecamatan: KecamatanBase):
    try:
        manager = LocationManager(kecamatan=kecamatan)
        return await manager.add_kecamatan()
    except Exception as e:
        raise e

@router.post("/add_kelurahan", tags=["Location"])
async def add_kelurahan(kelurahan: KelurahanBase):
    try:
        manager = LocationManager(kelurahan=kelurahan)
        return await manager.add_kelurahan()
    except Exception as e:
        raise e

# Location Search Routers

@router.get("/cities/{province_id}", tags=["Location Search"])
async def get_cities(province_id: int):
    try:
        manager = LocationSearchManager(province_id=province_id)
        return await manager.get_cities()
    except Exception as e:
        raise e

@router.get("/kecamatans/{city_id}", tags=["Location Search"])
async def get_kecamatans(city_id: int):
    try:
        manager = LocationSearchManager(city_id=city_id)
        return await manager.get_kecamatans()
    except Exception as e:
        raise e

@router.get("/kelurahans/{kecamatan_id}", tags=["Location Search"])
async def get_kelurahans(kecamatan_id: int):
    try:
        manager = LocationSearchManager(kecamatan_id=kecamatan_id)
        return await manager.get_kelurahans()
    except Exception as e:
        raise e

@router.get("/postal_code/{kelurahan_id}", tags=["Location Search"])
async def get_postal_code(kelurahan_id: int):
    try:
        manager = LocationSearchManager(kelurahan_id=kelurahan_id)
        return await manager.get_postal_code()
    except Exception as e:
        raise e

# Interest Rate Routers

@router.get("/interest_rates", tags=["Interest Rate"])
async def get_interest_rates():
    try:
        manager = InterestRateManager(None)
        return await manager.get_interest_rates()
    except Exception as e:
        raise e

@router.get("/interest_rates/{interest_rate_id}", tags=["Interest Rate"])
async def get_interest_rate(interest_rate_id: int):
    try:
        manager = InterestRateManager(None)
        return await manager.get_interest_rate(interest_rate_id)
    except Exception as e:
        raise e

@router.post("/add_interest_rate", tags=["Interest Rate"])
async def add_interest_rate(interest_rate: InterestRateBase):
    try:
        manager = InterestRateManager(interest_rate)
        return await manager.add_interest_rate()
    except Exception as e:
        raise e

@router.put("/update_interest_rate/{interest_rate_id}", tags=["Interest Rate"])
async def update_interest_rate(interest_rate_id: int, interest_rate: InterestRateBase):
    try:
        manager = InterestRateManager(interest_rate)
        return await manager.update_interest_rate(interest_rate_id)
    except Exception as e:
        raise e

@router.delete("/delete_interest_rate/{interest_rate_id}", tags=["Interest Rate"])
async def delete_interest_rate(interest_rate_id: int):
    try:
        manager = InterestRateManager(None)
        return await manager.delete_interest_rate(interest_rate_id)
    except Exception as e:
        raise e

@router.delete("/delete_interest_rates", tags=["Interest Rate"])
async def delete_interest_rates():
    try:
        manager = InterestRateManager(None)
        return await manager.delete_interest_rates()
    except Exception as e:
        raise e

@router.put("/update_interest_rate_field_by_conditions", tags=["Interest Rate"])
async def update_interest_rate_field_by_conditions(update_data: dict, conditions: dict):
    try:
        manager = InterestRateManager(None)
        return await manager.update_interest_rate_field_by_conditions(update_data, conditions)
    except Exception as e:
        raise e

# Insurance Routers

@router.get("/insurances", tags=["Insurance"])
async def get_insurances():
    try:
        manager = InsuranceManager(None)
        return await manager.get_insurances()
    except Exception as e:
        raise e

@router.get("/insurances/{insurance_id}", tags=["Insurance"])
async def get_insurance(insurance_id: int):
    try:
        manager = InsuranceManager(None)
        return await manager.get_insurance(insurance_id)
    except Exception as e:
        raise e

@router.post("/add_insurance", tags=["Insurance"])
async def add_insurance(insurance: InsuranceBase):
    try:
        manager = InsuranceManager(insurance)
        return await manager.add_insurance()
    except Exception as e:
        raise e

@router.put("/update_insurance/{insurance_id}", tags=["Insurance"])
async def update_insurance(insurance_id: int, insurance: InsuranceBase):
    try:
        manager = InsuranceManager(insurance)
        return await manager.update_insurance(insurance_id)
    except Exception as e:
        raise e

@router.delete("/delete_insurance/{insurance_id}", tags=["Insurance"])
async def delete_insurance(insurance_id: int):
    try:
        manager = InsuranceManager(None)
        return await manager.delete_insurance(insurance_id)
    except Exception as e:
        raise e

@router.delete("/delete_insurances", tags=["Insurance"])
async def delete_insurances():
    try:
        manager = InsuranceManager(None)
        return await manager.delete_insurances()
    except Exception as e:
        raise e

# Branch Routers

@router.get("/branches", tags=["Branch"])
async def get_branches():
    try:
        manager = BranchManager(None)
        return await manager.get_branches()
    except Exception as e:
        raise e

@router.get("/branches/{branch_id}", tags=["Branch"])
async def get_branch(branch_id: int):
    try:
        manager = BranchManager(None)
        return await manager.get_branch(branch_id)
    except Exception as e:
        raise e

@router.post("/add_branch", tags=["Branch"])
async def add_branch(branch: BranchBase):
    try:
        manager = BranchManager(branch)
        return await manager.add_branch()
    except Exception as e:
        raise e

@router.put("/update_branch/{branch_id}", tags=["Branch"])
async def update_branch(branch_id: int, branch: BranchBase):
    try:
        manager = BranchManager(branch)
        return await manager.update_branch(branch_id)
    except Exception as e:
        raise e

@router.delete("/delete_branch/{branch_id}", tags=["Branch"])
async def delete_branch(branch_id: int):
    try:
        manager = BranchManager(None)
        return await manager.delete_branch(branch_id)
    except Exception as e:
        raise e

@router.delete("/delete_branches", tags=["Branch"])
async def delete_branches():
    try:
        manager = BranchManager(None)
        return await manager.delete_branches()
    except Exception as e:
        raise e

# CMO Routers

@router.get("/cmos", tags=["CMO"])
async def get_cmos():
    try:
        manager = CMOManager(None)
        return await manager.get_cmos()
    except Exception as e:
        raise e

@router.get("/cmos/{cmo_id}", tags=["CMO"])
async def get_cmo(cmo_id: int):
    try:
        manager = CMOManager(None)
        return await manager.get_cmo(cmo_id)
    except Exception as e:
        raise e

@router.post("/add_cmo", tags=["CMO"])
async def add_cmo(cmo: CMOBase):
    try:
        manager = CMOManager(cmo)
        return await manager.add_cmo()
    except Exception as e:
        raise e

@router.put("/update_cmo/{cmo_id}", tags=["CMO"])
async def update_cmo(cmo_id: int, cmo: CMOBase):
    try:
        manager = CMOManager(cmo)
        return await manager.update_cmo(cmo_id)
    except Exception as e:
        raise e

@router.delete("/delete_cmo/{cmo_id}", tags=["CMO"])
async def delete_cmo(cmo_id: int):
    try:
        manager = CMOManager(None)
        return await manager.delete_cmo(cmo_id)
    except Exception as e:
        raise e

@router.delete("/delete_cmos", tags=["CMO"])
async def delete_cmos():
    try:
        manager = CMOManager(None)
        return await manager.delete_cmos()
    except Exception as e:
        raise e

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

# Customer Routers

@router.get("/customers", tags=["Customers"])
async def get_customers():
    try:
        manager = CustomerManager(None)
        return await manager.get_customers()
    except Exception as e:
        raise e

@router.get("/customers/{customer_id}", tags=["Customers"])
async def get_customer(customer_id: int):
    try:
        manager = CustomerManager(None)
        return await manager.get_customer(customer_id)
    except Exception as e:
        raise e

@router.post("/add_customer", tags=["Customers"])
async def add_customer(customer: CustomerBase):
    try:
        manager = CustomerManager(customer)
        return await manager.add_customer()
    except Exception as e:
        raise e

@router.put("/update_customer/{customer_id}", tags=["Customers"])
async def update_customer(customer_id: int, customer: CustomerBase):
    try:
        manager = CustomerManager(customer)
        return await manager.update_customer(customer_id)
    except Exception as e:
        raise e

@router.delete("/delete_customer/{customer_id}", tags=["Customers"])
async def delete_customer(customer_id: int):
    try:
        manager = CustomerManager(None)
        return await manager.delete_customer(customer_id)
    except Exception as e:
        raise e

@router.delete("/delete_customers", tags=["Customers"])
async def delete_customers():
    try:
        manager = CustomerManager(None)
        return await manager.delete_customers()
    except Exception as e:
        raise e

@router.get("/customers_by_user_id/{user_id}", tags=["Customers"])
async def get_customers_by_user_id(user_id: int):
    try:
        manager = CustomerManager(None)
        return await manager.get_customers_by_user_id(user_id)
    except Exception as e:
        raise e

# Spouse Routers

@router.get("/spouses", tags=["Spouses"])
async def get_spouses():
    try:
        manager = SpouseManager(None)
        return await manager.get_spouses()
    except Exception as e:
        raise e

@router.get("/spouses/{spouse_id}", tags=["Spouses"])
async def get_spouse(spouse_id: int):
    try:
        manager = SpouseManager(None)
        return await manager.get_spouse(spouse_id)
    except Exception as e:
        raise e

@router.post("/add_spouse", tags=["Spouses"])
async def add_spouse(spouse: SpouseBase):
    try:
        manager = SpouseManager(spouse)
        return await manager.add_spouse()
    except Exception as e:
        raise e

@router.put("/update_spouse/{spouse_id}", tags=["Spouses"])
async def update_spouse(spouse_id: int, spouse: SpouseBase):
    try:
        manager = SpouseManager(spouse)
        return await manager.update_spouse(spouse_id)
    except Exception as e:
        raise e

@router.delete("/delete_spouse/{spouse_id}", tags=["Spouses"])
async def delete_spouse(spouse_id: int):
    try:
        manager = SpouseManager(None)
        return await manager.delete_spouse(spouse_id)
    except Exception as e:
        raise e

@router.delete("/delete_spouses", tags=["Spouses"])
async def delete_spouses():
    try:
        manager = SpouseManager(None)
        return await manager.delete_spouses()
    except Exception as e:
        raise e

# Guarantor Routers

@router.get("/guarantors", tags=["Guarantors"])
async def get_guarantors():
    try:
        manager = GuarantorManager(None)
        return await manager.get_guarantors()
    except Exception as e:
        raise e

@router.get("/guarantors/{guarantor_id}", tags=["Guarantors"])
async def get_guarantor(guarantor_id: int):
    try:
        manager = GuarantorManager(None)
        return await manager.get_guarantor(guarantor_id)
    except Exception as e:
        raise e

@router.post("/add_guarantor", tags=["Guarantors"])
async def add_guarantor(guarantor: GuarantorBase): 
    try:
        manager = GuarantorManager(guarantor)
        return await manager.add_guarantor()
    except Exception as e:
        raise e

@router.put("/update_guarantor/{guarantor_id}", tags=["Guarantors"])
async def update_guarantor(guarantor_id: int, guarantor: GuarantorBase):
    try:
        manager = GuarantorManager(guarantor)
        return await manager.update_guarantor(guarantor_id)
    except Exception as e:
        raise e

@router.delete("/delete_guarantor/{guarantor_id}", tags=["Guarantors"])
async def delete_guarantor(guarantor_id: int):
    try:
        manager = GuarantorManager(None)
        return await manager.delete_guarantor(guarantor_id)
    except Exception as e:
        raise e

@router.delete("/delete_guarantors", tags=["Guarantors"])
async def delete_guarantors():
    try:
        manager = GuarantorManager(None)
        return await manager.delete_guarantors()
    except Exception as e:
        raise e

# Application Routers

@router.get("/applications", tags=["Applications"])
async def get_applications():
    try:
        manager = ApplicationManager(None)
        return await manager.get_applications()
    except Exception as e:
        raise e

@router.get("/applications/{application_id}", tags=["Applications"])
async def get_application(application_id: int):
    try:
        manager = ApplicationManager(None)
        return await manager.get_application(application_id)
    except Exception as e:
        raise e

@router.post("/add_application", tags=["Applications"])
async def add_application(application: ApplicationBase):
    try:
        manager = ApplicationManager(application)
        return await manager.add_application()
    except Exception as e:
        raise e

@router.put("/update_application/{application_id}", tags=["Applications"])
async def update_application(application_id: int, application: ApplicationBase):
    try:
        manager = ApplicationManager(application)
        return await manager.update_application(application_id)
    except Exception as e:
        raise e

@router.delete("/delete_application/{application_id}", tags=["Applications"])
async def delete_application(application_id: int):
    try:
        manager = ApplicationManager(None)
        return await manager.delete_application(application_id)
    except Exception as e:
        raise e

@router.delete("/delete_applications", tags=["Applications"])
async def delete_applications():
    try:
        manager = ApplicationManager(None)
        return await manager.delete_applications()
    except Exception as e:
        raise e

# @router.get("/calculate_insurance_rate", tags=["Applications"])
# async def calculate_insurance_rate(
#     otr: int,
#     province_id: int,
#     tenor_year: int,
#     TYPE: str
# ):
#     try:
#         manager = ApplicationManager(None)
#         return await manager.calculate_insurance_rate(
#             otr=otr,
#             province_id=province_id,
#             tenor_year=tenor_year,
#             TYPE=TYPE,
#         )
#     except Exception as e:
#         raise e

@router.get("/application_credit_simulation", tags=["Applications"])
async def application_credit_simulation(application_id: int, PROVISION: int = 0):
    try:
        manager = ApplicationManager(None)
        application_dict = await manager.get_application(application_id)
        application_dict = application_dict[0]
        application = ApplicationBase(**application_dict)
        new_manager = ApplicationManager(application)
        return await new_manager.application_credit_simulation(PROVISION=PROVISION)
    except Exception as e:
        raise e

class CreditSimulationRequest(BaseModel):
    OTR: int
    DP: int
    TENOR_YEAR: int
    TENOR_MONTH: int
    TYPE: str
    PROVINCE_ID: int

@router.post("/test_application_credit_simulation", tags=["Applications"])
async def test_application_credit_simulation(payload: CreditSimulationRequest):
    try:
        manager = ApplicationManager(None)
        return await manager.test_application_credit_simulation(OTR=payload.OTR, DP=payload.DP, TENOR_YEAR=payload.TENOR_YEAR, TENOR_MONTH=payload.TENOR_MONTH, TYPE=payload.TYPE, PROVINCE_ID=payload.PROVINCE_ID)
    except Exception as e:
        raise e

# @router.put("/add_application_credit_simulation", tags=["Applications"])
# async def add_application_credit_simulation(application: ApplicationBase):
#     try:
#         manager = ApplicationManager(application)
#         return await manager.add_application_credit_simulation()
#     except Exception as e:
#         raise e

# Asset Routers

@router.get("/assets", tags=["Assets"])
async def get_assets():
    try:
        manager = AssetManager(None)
        return await manager.get_assets()
    except Exception as e:
        raise e
        
@router.get("/assets/{asset_id}", tags=["Assets"])
async def get_asset(asset_id: int):
    try:
        manager = AssetManager(None)
        return await manager.get_asset(asset_id)
    except Exception as e:
        raise e
        
@router.post("/add_asset", tags=["Assets"])
async def add_asset(asset: AssetBase):
    try:
        manager = AssetManager(asset)
        return await manager.add_asset()
    except Exception as e:
        raise e

@router.put("/update_asset/{asset_id}", tags=["Assets"])
async def update_asset(asset_id: int, asset: AssetBase):
    try:
        manager = AssetManager(asset)
        return await manager.update_asset(asset_id)
    except Exception as e:
        raise e
        
@router.delete("/delete_asset/{asset_id}", tags=["Assets"])
async def delete_asset(asset_id: int):
    try:
        manager = AssetManager(None)
        return await manager.delete_asset(asset_id)
    except Exception as e:
        raise e
        
@router.delete("/delete_assets", tags=["Assets"])
async def delete_assets():
    try:
        manager = AssetManager(None)
        return await manager.delete_assets()
    except Exception as e:
        raise e