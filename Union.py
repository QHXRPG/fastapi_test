from typing import Union, Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/users/{user_id}")
async def get_user(user_id: Union[int, str],
                   name: Optional[str] = None):
    """
    通过 Union 来声明一个混合类型，int 在前、str 在后
    会先按照 int 解析，解析失败再变成 str
    然后是 name，它表示字符串类型、但默认值为 None（不是字符串）
    那么应该声明为 Optional[str]
    """
    return {"user_id": user_id, "name": name}

if __name__ == "__main__":
    uvicorn.run("Union:app", host="127.0.0.1", port=8000)
