from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from db import retrieve_users_data, add_user_data

app = FastAPI()


@app.get("/")
def get_users_data():
    try:
        result = retrieve_users_data()
        return JSONResponse(status_code=200, content=result)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)


@app.post("/")
def add_users_data(data: dict):
    try:
        result = add_user_data(data)
        return JSONResponse(status_code=200, content=result)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)
