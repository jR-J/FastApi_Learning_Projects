from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Calculator(BaseModel):
    a: float
    b: float
    op: str


@app.post("/calculate")
def calculate(calc: Calculator):
    if calc.op == "add":
        result = calc.a + calc.b
    elif calc.op == "subtract":
        result = calc.a - calc.b
    elif calc.op == "multiply":
        result = calc.a * calc.b
    elif calc.op == "divide":
        if calc.b != 0:
            result = calc.a / calc.b
        else:
            return {"error": "Division by zero is not allowed."}
    else:
        return {"error": "Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."}

    return {
        "operation": calc.op,
        "result": result
    }