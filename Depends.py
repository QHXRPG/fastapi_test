from typing import Optional
from fastapi import FastAPI, Depends
import uvicorn

app = FastAPI()


async def common_parameters(select: str = "*", skip: int = 0, limit: int = 100):
    return {"select": select, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    # common_parameters 接收三个参数：select、skip、limit
    # 因此会从请求中解析出 select、skip、limit 并传给 common_parameters
    # 然后将 common_parameters 的返回值赋给 commons
    # 但如果解析不到某个参数，那么会判断函数中参数是否有默认值
    # 没有的话就会返回错误
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons


if __name__ == "__main__":
    uvicorn.run("4:app", host="127.0.0.1", port=8000)
