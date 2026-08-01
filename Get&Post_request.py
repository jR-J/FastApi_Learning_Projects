from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    is_offer:bool = None

#GET route(read data)
@app.get("/")
def read_root():
    return {"message": "welcome to my first FastApi"}


#GET route with a path parameter
@app.get("/items/{item_id}")
def read_item(item_id:int, q: str = None):
    return {"item_id":item_id, "query_param":q}

#POST route(creat data) using item model
@app.post("/items/")
def creat_item(item: Item):
    return {"message":f"item" "{item.name} created successfully", "data":item}