# FastAPI app 전역에 의존성 주입하기
from fastapi import Depends, FastAPI, Header, HTTPException


async def verify_token(x_token: str = Header()):
    if x_token != "sst":
        raise HTTPException(status_code=400, detail="invalid x-token")


async def verify_key(x_key: str = Header()):
    if x_key != "ssk":
        raise HTTPException(status_code=400, detail="invalid x-key")
    return x_key


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
