from fastapi import APIRouter, HTTPException
from .models import UserData
from .database import session

router = APIRouter()

# GET API to retrieve all users
@router.get("/users/")
async def get_users():
    try:
        query = f"SELECT id, name, email FROM users"
        rows = session.execute(query)
        users = [{"id": str(row.id), "name": row.name, "email": row.email} for row in rows]
        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while fetching user data.")
