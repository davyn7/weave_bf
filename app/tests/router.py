# app/tests/router.py

from fastapi import APIRouter
# from app.tests.managers import (

# )
# from app.tests.schemas import (

# )
from pydantic import BaseModel
from typing import List
from uuid import UUID

router = APIRouter(prefix="/tests", tags=["Tests"])

# Initialize DB Testing

@router.post("/populate")
async def populate():
    pass

@router.delete("/clear")
async def clear():
    pass