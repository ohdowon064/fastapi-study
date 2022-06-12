from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str # required
    description: str | None = None # not required
    price: float
    tax: float | None = None

    @property
    def price_with_tax(self):
        if self.tax:
            return self.price + self.tax
        return self.price

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    item_dict["price_with_tax"] = item.price_with_tax
    return item_dict


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@app.put("/items/{item_id}")
async def update_item_with_query(
        item_id: int,
        item: Item,
        q: str | None = None
):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result["q"] = q
    return result

# 라우트 경로에 있는 변수 -> 경로 변수
# 라우트 경로에 없는데 싱글 타입 변수 -> 쿼리 변수
# pydantic 모델 -> body 데이터