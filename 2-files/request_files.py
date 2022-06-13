import json

import uvicorn
from fastapi import FastAPI, File, UploadFile, Depends, Form, HTTPException

# File을 사용하기 위해서는 python-multipart를 설치해야한다.
from pydantic import BaseModel, ValidationError

app = FastAPI()


@app.post("/files")
async def create_file(file: bytes = File()):
    print(file.__dir__())
    print(type(file))
    return {"file_size": len(file)}


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    print(file.__dir__())
    print(type(file))
    return {"filename": file.filename}


class BodyData(BaseModel):
    a: int
    b: int
    c: str

    @classmethod
    def __get_validators__(cls) -> 'CallableGenerator':
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


async def checker(data: str = Form(...)):
    try:
        model = BodyData.parse_raw(data)
    except ValidationError as e:
        raise HTTPException(detail=e.json(), status_code=400)
    return model

# https://stackoverflow.com/questions/65504438/how-to-add-both-file-and-json-body-in-a-fastapi-post-request
# 파일을 포함하지 않는 경우 application/x-www-form-urlencoded로 인코딩된다.
# 파일을 포함한 경우 -> multipart/form-data로 인코딩
# 이 경우 body 데이터는 application/json이 아니므로 form 데이터로 들어온다.
# multipart/form-data에서 File과 Body를 동시에 받는 방법
# 인코딩 함수를 구현(위에 checker 함수) 또는 모델 내부에 구현
# Depends(checker) 방식으로 사용가능
@app.post("/file-body")
async def upload_file_with_body(file: UploadFile, data: BodyData):
    print(data, type(data))
    return {"filename": file.filename, **data.dict()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
