from typing import Optional

from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory=".")


@app.get("/")
async def hello(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/files/{file_path}")
async def root(file_path: str):
    return {"file_path": file_path}


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
