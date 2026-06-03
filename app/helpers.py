# app/helpers.py

import random
import string
from typing import Optional
import math

def generate_unique_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# async def credit_simulation(
#     OTR: int, 
#     DP: int, 
#     ASSET_YEAR: str, 
#     ASSET_TYPE: str, 
#     TENOR_YEAR: int,
#     TENOR_MONTH: int,
#     INTEREST_RATE: float,
#     INSURANCE_RATE: float,
#     TJH: int,
#     ADMIN: int,
#     PROVISION: int = 0
# ):
#     INSURANCE = OTR * INSURANCE_RATE + TJH
#     PRINCIPAL = OTR - DP + INSURANCE + PROVISION
#     INTEREST = math.ceil((PRINCIPAL * INTEREST_RATE * TENOR_YEAR) / 1000) * 1000
#     MONTHLY_PAYMENT = math.ceil((PRINCIPAL + INTEREST) / TENOR_MONTH / 500.0) * 500
#     ret = {
#         "OTR": OTR,
#         "DP": DP,
#         "INSURANCE": INSURANCE,
#         "PROVISION": PROVISION,
#         "PRINCIPAL": PRINCIPAL,
#         "MONTHLY_PAYMENT": MONTHLY_PAYMENT,
#         "TENOR": TENOR_MONTH - 1,
#         "FLAT_RATE": INTEREST_RATE,
#         "ADMIN_FEE": ADMIN,
#         "FIRST_PAYMENT": DP + MONTHLY_PAYMENT + ADMIN
#     }
#     return ret



