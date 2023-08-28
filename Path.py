from fastapi import FastAPI, Path

import uvicorn

app = FastAPI()
# 对查询参数进行数据校验使用的是 Query，
# 对路径参数进行数据校验使用的是 Path，两者的使用方式一模一样，没有任何区别。
#%%
@app.get("/items/{item-id}")
async def read_items(
        item_id: int = Path(..., alias="item-id")
):
    return {"item-id": item_id}

#%%
@app.get("/items/{item-id}")
async def read_items(
        q: str,
        item_id: int = Path(..., alias="item-id")
):
    return {"item_id": item_id, "q": q}  # 赋值顺序不可变

#%%
@app.get("/items/{item-id}")
async def read_items(
        *,
        item_id: int = Path(..., alias="item-id"),
        q: str,
):
    return {"item_id": item_id, "q": q}  # 赋值顺序可变


if __name__ == "__main__":
    uvicorn.run("Path:app", host="127.0.0.1", port=8000)