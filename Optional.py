from fastapi import FastAPI
import uvicorn
from typing import Optional

app = FastAPI()


@app.get("/postgres/{schema}/v1/{table}")
async def get_data(schema: str,
                   table: str,
                   select: str = "*",
                   where: Optional[str] = None,
                   limit: Optional[int] = None,
                   offset: Optional[int] = None):
    """
    标准格式是：路径参数按照顺序在前，查询参数在后
    但 FastAPI 对顺序本身是没有什么要求的
    """
    query = f"select {select} from {schema}.{table}"
    if where:
        query += f" where {where}"
    if limit:
        query += f" limit {limit}"
    if offset:
        query += f" offset {offset}"
    return {"query": query}

if __name__ == "__main__":
    uvicorn.run("3:app", host="127.0.0.1", port=8000)
