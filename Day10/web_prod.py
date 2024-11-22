from fastapi import FastAPI,HTTPException
from fastapi import status
from logic_prod import Logic

app=FastAPI()

@app.get("/product/{x}")
async def root(x:int,y:int):
    #ans={"message":"input was zero"}
    if(x==0 or y==0):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Both must be positive values."
        )
        #return ans
    
    lo=Logic()
    ans["message"]="Success"
    ans["result"]=lo.prod(int(x), int(y))
    return ans
