from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cassandra.cluster import Cluster

app = FastAPI()

class UserData(BaseModel):
    name: str
    email: str

cluster = Cluster(['cassandra-db'])  # Use the container name
session = cluster.connect()

KEYSPACE = "user_data_keyspace"
TABLE = "users"

session.execute(f"""
    CREATE KEYSPACE IF NOT EXISTS {KEYSPACE} 
    WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}}
""")
session.set_keyspace(KEYSPACE)
session.execute(f"""
    CREATE TABLE IF NOT EXISTS {TABLE} (
        id UUID PRIMARY KEY,
        name text,
        email text
    )
""")

@app.post("/save_user/")
async def save_user(user_data: UserData):
    try:
        query = f"INSERT INTO {TABLE} (id, name, email) VALUES (uuid(), %s, %s)"
        session.execute(query, (user_data.name, user_data.email))
        return {"message": "User data saved successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while saving data.")

@app.get("/users/")
async def get_users():
    try:
        query = f"SELECT id, name, email FROM {TABLE}"
        rows = session.execute(query)
        users = [{"id": str(row.id), "name": row.name, "email": row.email} for row in rows]
        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while fetching user data.")

@app.get("/")
def root():
    return {"message": "FastAPI Cassandra API"}
