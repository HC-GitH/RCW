from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

@app.get("/")
async def welcome():
    try:
        return {"message": "Hello from server"}
    except Exception as e:
        print('Exception : {e}')
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/test")
async def hello():
    try:
        return {"message": "Hello from test server"}
    except Exception as e:
        print('Exception : {e}')
        raise HTTPException(status_code=500, detail=str(e))