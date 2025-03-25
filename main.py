from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define an empty list to store items
items = []

# ✅ Pydantic model for request body
class Item(BaseModel):
    name: str
    is_done:bool=False

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: Item):
    items.append(item.name)
    return {"message": "Item added", "items": items}

@app.get("/items",response_model=list[Item])
def list_items(limit:int=10):
    return items[0:limit]


@app.get("/items/{item_id}",response_model=Item)
def get_item(item_id: int):
    if 0 <= item_id < len(items):  # ✅ Prevents negative index errors
        return {"item": items[item_id]}
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")  # ✅ Fixed spelling
