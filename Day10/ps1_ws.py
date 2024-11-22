from fastapi import FastAPI,status, HTTPException
from pydantic import BaseModel
from typing import List
from ps1_logic import Logic


# Create a Pydantic model for the input (Rectangle)
class Product(BaseModel):
    id:int
    name:str
    price:float

# Initialize FastAPI app
app = FastAPI()
l1=Logic()

@app.post("/addproduct",status_code=status.HTTP_201_CREATED)
async def add_product(new_product: Product):
    add=l1.add_product(new_product)
    id add is False:
        raise HTTPException (status_code=status.HTTP_400_BAD_REQUEST,
            detail="Length and breadth must be positive values."
        )
    return add
 
@app.put("/updateproduct/{productid}")
async def update_product(updated_product: Product):
    update = l1.update_product(updated_product)
    return update
 
@app.get("/viewproducts")
async def list_products():
    view = l1.view_all_products()
    return view

@app.put("/applyDiscount")
async def applyDiscount(discAmount: float):
    result = l1.apply_discount(discAmount)
    return  result



