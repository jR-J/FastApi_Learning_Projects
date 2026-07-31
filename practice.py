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
