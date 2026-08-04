from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session 


app = FastAPI()

# Database connection configuration
DATABASE_URL = "sqlite:///./test.db"  # Using SQLite for simplicity
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency to get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# SQLAlchemy model 
class DBProduct(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    item_code = Column(String, unique=True, index=True)
    in_stock = Column(Boolean, default=True)


# Pydantic model for request and response validation
class ProductCreate(BaseModel):

    name: str
    price: float
    item_code: str
    in_stock: bool = True

# Tell sqlalchemy to automatically create the table file when the app starts
Base.metadata.create_all(bind=engine)

# Endpoint
@app.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = DBProduct(
        name=product.name,
        price=product.price,
        item_code=product.item_code,
        in_stock=product.in_stock
    )
    db.add(db_product)      # Stage the product to be added
    db.commit()           # Commit/save the change permanently to the database file
    db.refresh(db_product) # Refresh the object to read its new auto-generated ID
    return {"message": "Saved to database!", "product": {"id": db_product.id, "name": db_product.name, "item_code": db_product.item_code}}

@app.get("/products")
def read_products(db: Session = Depends(get_db)):
    # Query the database to get all records from the products table
    all_products = db.query(DBProduct).all()
    return {"total_in_db": len(all_products), "catalog": all_products}



# Building a DELETE endpoint to delete a product by its ID
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    # 1. Look for the product in the database by its ID
    db_product = db.query(DBProduct).filter(DBProduct.id == product_id).first()
    
    # 2. If it's not found, raise a clean 404 Error
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found in catalog")
    
    # 3. If found, remove it from the session and save the change
    db.delete(db_product)
    db.commit()
    
    return {"message": f"Product '{db_product.name}' was successfully deleted!"}