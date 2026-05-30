# app/router.py

from fastapi import APIRouter
# from app.managers import (
    
# )
# from app.schemas import (
    
# )
from uuid import UUID

router = APIRouter()

# Initialize DB Testing

@router.post("/populate", tags=["Testing"])
async def populate():
    pass

@router.delete("/clear", tags=["Testing"])
async def clear():
    pass