from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    in_stock: bool 



@app.post("/product")
def create_product(new_product: Product):
    total_with_tax = new_product.price*1.18

    return {
        "messega": f"Product {new_product} saved",
        "price_before_tax": new_product.price,
        "total_price_with_tax": total_with_tax
    }

