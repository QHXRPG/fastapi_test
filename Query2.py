from typing import Optional
from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

#%%
@app.get("/user")
async def check_length(
        # 默认值为 None，应该声明为 Optional[str]，当然声明 str 也是可以的
        # 只不过声明为 str，那么默认值应该也是 str
        # 所以如果允许一个类型的值为空，那么更规范的做法应该是声明为 Optional[类型]
        password: Optional[str] = Query(None, min_length=6, max_length=15)
):
    return {"password": password}

#%%
@app.get("/user")
async def check_length(
    password: str = Query("satori", min_length=6,
                          max_length=15, regex=r"^satori")
):
    """
    此时 password 的默认值为 'satori'，并且传递的时候也必须要以 'satori' 开头
    但值得注意的是 password 后面的类型注解是 str，不再是 Optional[str]
    因为默认值不是 None 了，当然这里即使写成 Optional[str] 也是没有什么影响的
    """
    return {"password": password}

#%%
@app.get("/user")
async def check_length(
    password: str = Query(..., min_length=6,
                          max_length=15)
):
    # 我们知道 Query 的第一个参数是 password 的默认值
    # 但如果将 Query 的第一个参数换成 ...
    # 那么 FastAPI 就不会再将它当成是默认值了
    # 而是对 password 起一个限定作用，表示它是必传参数
    return {"password": password}


if __name__ == "__main__":
    uvicorn.run("Query2:app", host="127.0.0.1", port=8000)