from fastapi import FastAPI
from .routes import router

app = FastAPI()

app.include_router(router)

# Test root endpoint
@app.get("/")
def root():
    return {"message": "FastAPI Cassandra API"}
