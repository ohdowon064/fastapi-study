from fastapi import FastAPI

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# # 경로 변수가 아닌 인자는 쿼리 변수가 된다.
# @app.get("/items")
# async def read_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]

# Optional patameters
# Optional[str]
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# query string -> 1, True, true, on, yes -> true
# 0, false, False, off, no -> false
# @app.get("/items/{item_id}")
# async def read_item_with_short(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# multiple and required path/query variable
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        *,
        user_id: int,
        item_id: int,
        skip: int = 0,
        limit: int | None = None,
        needy: str,  # default 값이 없으므로 필수 쿼리 변수
):
    return {'user_id': user_id, "item_id": item_id, "skip": skip, "limit": limit, "needy": needy}