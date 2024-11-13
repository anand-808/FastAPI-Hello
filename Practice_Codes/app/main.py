from fastapi import FastAPI, HTTPException, Body, Cookie, Form, File, UploadFile
from pydantic import BaseModel, HttpUrl
from typing import Union, Annotated
from typing import List, Set

app = FastAPI()

# Root endpoint (GET)
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Mock items dictionary for error handling in GET request
items = {
    1: {"name": "Item 1", "price": 10.0},
    2: {"name": "Item 2", "price": 20.0},
}

# GET request for items with error handling
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": items[item_id]}

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = set()  # tags as a Set
    images: List[str] = []  # images as a List

# Example POST endpoint with error handling for missing fields
@app.post("/items/")
async def create_item(item: Item):
    if not item.name or not item.price:
        raise HTTPException(status_code=400, detail="Item name and price are required")
    return {"name": item.name, "price": item.price}

# Example PUT endpoint with error handling for missing fields
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    if not item.name or not item.price:
        raise HTTPException(status_code=400, detail="Item name and price are required")
    items[item_id] = {"name": item.name, "price": item.price}
    return {"item_id": item_id, "name": item.name, "price": item.price}

# Define the Cookies model
class Cookies(BaseModel):
    model_config = {"extra": "forbid"}  # Ensures no extra fields are allowed

    session_id: str
    fatebook_tracker: Union[str, None] = None
    googall_tracker: Union[str, None] = None

# GET request to read cookies
@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies

class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}

@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    if not data.username or not data.password:
        raise HTTPException(status_code=400, detail="Username and password are required")
    return data

# Endpoint for receiving file as bytes with error handling
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")
    return {"file_size": len(file)}

# Endpoint for receiving uploaded file and returning filename with error handling
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")
    return {"filename": file.filename}

# Endpoint for receiving two files and a token with error handling
@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    if not file or not fileb:
        raise HTTPException(status_code=400, detail="Both files must be uploaded")
    if not token:
        raise HTTPException(status_code=400, detail="Token is required")
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
