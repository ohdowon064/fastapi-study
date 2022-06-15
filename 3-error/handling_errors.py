# 수행 권한 없음, 리소스 접근 권한, 존재하지 않는 곳에 접근 등
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        # return이 아닌 raise
        raise HTTPException(status_code=404, detail="Item Not Found")
    return {"item": items[item_id]}


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


# 특정 예외를 발생시켰을 때 행동정의
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."}
    )


@app.get("/unicorn/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)  # 예외 발생 -> 설정된 예외 핸들러 동작
    return {"unicorn_name": name}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body})
    )


class Item(BaseModel):
    title: str
    size: int


@app.post("/items")
async def create_item(item: Item):
    return item
