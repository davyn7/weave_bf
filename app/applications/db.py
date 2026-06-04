# app/applications/db.py

from app.connection import supabase
from app.applications.schemas import (
    ApplicationBase
)
from uuid import UUID

# Application DB Operations

async def get_applications_db():
    response = supabase.table("APPLICATIONS").select("*").execute()
    return response.data

async def get_application_db(application_id: int):
    response = supabase.table("APPLICATIONS").select("*").eq("id", application_id).execute()
    return response.data

async def add_application_db(application: ApplicationBase):
    application_data = application.model_dump(mode="json")
    response = supabase.table("APPLICATIONS").insert(application_data).execute()
    return response.data

async def update_application_db(application: ApplicationBase, application_id: int):
    application_data = application.model_dump(exclude_unset=True, mode="json")
    response = supabase.table("APPLICATIONS").update(application_data).eq("id", application_id).execute()
    return response.data

async def delete_application_db(application_id: int):
    response = supabase.table("APPLICATIONS").delete().eq("id", application_id).execute()
    return response.data

async def delete_applications_db():
    response = supabase.table("APPLICATIONS").delete().neq("id", 0).execute()
    return response.data