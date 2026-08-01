from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def about_me():
    return {
        "status": "learning",
        "level": "beginner",
        "goal": "Master FastAPI"
    }



@app.get("/greet/{name}")
def greet_person(name: str):
    return {"messae":f"hello {name}"}




@app.get("/double/{number}")
def double_numbers(number: int):
    doubled_number = number*2
    return {"calculate":f"doulbed to {doubled_number}"}


@app.get("/shop")
def online_store(item: str, size: str = "Medium"):
    return {
        "ordered_item": item,
        "selected_size": size,
        "status": "Item added to cart successfully!"
    }



