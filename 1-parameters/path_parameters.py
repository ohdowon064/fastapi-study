from fastapi import FastAPI

app = FastAPI()

# 1. path parameters with types
#
#
# @app.get("/items/{item_id}")  # 경로에 있는 이름와 동일한 인자가 경로변수가 된다.
# async def read_item(item_id: int):
#     return {"item_id": item_id}
#
#
# @app.get("/users/me")  # 라우트를 위에서부터 찾기 때문에 /users/me 보다 위에 있어야한다.
# async def whoami():
#     return {"user_id": "the current user"}
#
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}


# 2. create an enum class
# from enum import Enum
#
#
# # 정해진 값 중에서만 가능
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
#
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW"}
#
#     if model_name.value == ModelName.lenet:
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}

# 3. path parameters containing paths
# 경로를 포함한 경로변수

# 경로를 포함한 경로변수는 반드시 :path 타입을 명시해야한다. 함수에서는 str로 받는다.
# 루트경로(/)를 포함한 경우에는 // 더블슬래시로 된다.
@app.get("/files/{file_path: path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
