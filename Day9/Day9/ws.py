from fastapi import FastAPI
from logic import Logic

app=FastAPI()

@app.get('/')
async def root():
    return {"message":"Hello World"}

@app.get("/s")
async def func():
    li=Logic()
    return li.rs()

@app.get("/next")
async def wp(n):
    li=Logic()
    b=li.nextnumber(int(n))
    return{"Result":b}
