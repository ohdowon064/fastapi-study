# return 값이 없는 의존성이 존재한다.
# Depends로 파라미터를 선언하지 않고, 의존성 리스트를 추가하는 방식이 존재

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: str = Header()):
    if x_token != "super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token Header Invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key Header Invalid")
    return x_key


# verify_token -> verity_key 순서
@app.get("/items", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    # print(x_key) -> 리턴값 사용 불가
    return [{"item": "Foo"}, {"item": "Bar"}]
