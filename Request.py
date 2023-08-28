from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

#任何一个请求都对应一个 Request 对象，请求的所有信息都在这个 Request 对象中，
# FastAPI 也不例外。

@app.get("/girl/{user_id}")
async def read_info(user_id: str,
                    request: Request):
    """
    路径参数必须要体现在函数参数中
    但是查询参数可以不写了
    因为我们定义了 request: Request
    那么请求相关的所有信息都会进入到这个 Request 对象中
    """
    header = request.headers  # 请求头
    method = request.method  # 请求方法
    cookies = request.cookies  # cookies
    query_params = request.query_params  # 查询参数
    return {"name": query_params.get("name"),
            "age": query_params.get("age"),
            "hobby": query_params.getlist("hobby")}


if __name__ == "__main__":
    uvicorn.run("Request:app", host="127.0.0.1", port=8000)
