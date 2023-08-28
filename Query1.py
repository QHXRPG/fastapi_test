from typing import List
from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


@app.get("/items1")
async def read_items1(a1: str = Query(...), a2: List[str] = Query(...), b: List[str] = Query(...)):
    """
    首先 a2 和 b 都是列表，会获取所有的值，但 a1 只获取了最后一个值。
    """
    return {"a1": a1, "a2": a2, "b": b}


@app.get("/items2")
async def read_items2(
    # item1 必须大于 5
    item1: int = Query(..., gt=5),
    # item2 必须小于等于 7
    item2: int = Query(..., le=7),
    # item3 必须等于 10
    item3: int = Query(..., ge=10, le=10)
):
    return {"item1": item1,
            "item2": item2,
            "item3": item3}


if __name__ == "__main__":
    uvicorn.run("Query1:app", host="127.0.0.1", port=8000)