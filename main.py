from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define an empty list to store items
items = []

# Pydantic model for request body
class Item(BaseModel):
    name: str

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: Item):
    items.append(item.name)
    return {"message": "Item added", "items": items}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    
    return {"item": items[item_id]}
