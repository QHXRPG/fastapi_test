"""
在 FastAPI 中，请求体可以看成是 Model 对象
"""

from typing import Optional
from fastapi import FastAPI, Response
from pydantic import BaseModel
import orjson
import uvicorn

app = FastAPI()


class Girl(BaseModel):
    """
    数据验证是通过 pydantic 实现的
    我们需要从中导入 BaseModel，然后继承它
    """
    name: str
    age: Optional[str] = None
    length: float


@app.post("/girl")
async def read_info(girl: Girl):
    # girl 就是我们接收的请求体，它需要通过 json 来传递
    # 并且这个 json 要有上面的三个字段（age 可以没有）
    # 通过 girl.xxx 的方式我们可以获取和修改内部的所有属性
    data = {"姓名": girl.name, "年龄": girl.age, "身高": girl.length}
    return Response(orjson.dumps(data), media_type="application/json")


if __name__ == "__main__":
    uvicorn.run("Model:app", host="127.0.0.1", port=8000)


