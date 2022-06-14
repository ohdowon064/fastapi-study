import json

from fastapi import FastAPI, Form, UploadFile
from pydantic import BaseModel

app = FastAPI()

@app.post("/files")
async def create_files(
        file: UploadFile, token: str = Form()
):
    return {
        "token": token,
        "filename": file.filename
    }

# multipart/form-data에서 File과 Form은 함께 가능
# application/json이 아니므로 File과 Body는 함께 불가능
# Form(str)로 들어온 데이터를 dict로 변환해야함
class BodyData(BaseModel):
    a: int
    b: str

    @classmethod
    def __get_validators__(cls) -> 'CallableGenerator':
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return cls(**value)


@app.post("/filebody")
async def create_files_with_body(files: list[UploadFile], body: BodyData):
    return {"filenames": [file.filename for file in files], **body.dict()}

@app.post("/body")
async def get_body(body: BodyData):
    return body