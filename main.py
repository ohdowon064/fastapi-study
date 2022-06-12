from typing import Optional

from fastapi import FastAPI, Query, Depends, Body, Path, Cookie
from pydantic import BaseModel, Field
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()


class ManyPath(BaseModel):
    path_a: str = Path()
    path_b: int = Path()


class ManyQuery(BaseModel):
    query_a: str = Query()
    query_b: str = Query()
    query_c: str = Query()


class BodyData(BaseModel):
    body_a: str
    body_b: int


class RequestModel(BaseModel):
    path_a: str = Path(...)
    query_a: int = Query(...)
    query_b: str = Query(...)
    path_b: float = Path(...)

    data: BodyData


@app.post("/req/{path_a}/{path_b}")
async def request_with_model(request_model: RequestModel = Depends()):
    return request_model


@app.get("/items")
async def q_test(q: str | None = Query(default=...)):
    return q


class Sample(BaseModel):
    a: str
    b: str

    class Config:
        schema_extra = {
            "a": 123,
            "b": 123,
        }


@app.post("/dict-test")
async def body_test(d: Optional[Sample] = None):
    print(d)
    return d

@app.get('/cookie-test')
async def cookie_test(c: str = Cookie()):
    print(c, type(c))
    return c