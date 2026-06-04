# app/users/router.py

from fastapi import APIRouter
# TODO
# from app.users.managers import (
    
# )
# from app.buana.schemas import (

# )
from pydantic import BaseModel
from typing import List
from uuid import UUID

router = APIRouter(prefix="/users", tags=["Users"])

# TODO: Add routers for Users

@router.get("/users")
async def get_users():
    return {"message": "Hello, World!"}