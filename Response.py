"""
Response 内部接收如下参数：
content：返回的数据；
status_code：状态码；
headers：返回的响应头；
media_type：响应类型（就是响应头里面的 Content-Type，这里单独作为一个参数出现了，其实通过 headers 参数设置也是可以的）；
background：接收一个任务，Response 在返回之后会自动异步执行
"""

#%%
from fastapi import FastAPI, Request, Response
import uvicorn
import orjson

app = FastAPI()


@app.get("/girl/{user_id}")
async def read_info(user_id: str, request: Request):
    # 查询参数
    query_params = request.query_params
    data = {"name": query_params.get("name"),
            "age": query_params.get("age"),
            "hobby": query_params.getlist("hobby")}
    # 实例化一个 Response 对象
    response = Response(orjson.dumps(data), # content，手动转成 json
                        201, # status_code，状态码
                        {"Token": "xxx"}, # headers，响应头
                        # media_type，就是 HTML 中的 Content-Type
                        # content 只是一坨字节流，需要告诉客户端响应类型
                        # 这样客户端才能正确的解析
                        "application/json",
                        )
    # 拿到 response 的时候，还可以单独对响应头和 cookie进行设置
    response.headers["ping"] = "pong"
    # 设置 cookie 的话，通过 response.set_cookie
    response.set_cookie("SessionID", "abc123456")
    # 也可以通过 response.delete_cookie 删除 cookie
    return response

#%%
from fastapi import FastAPI
from fastapi.responses import Response, HTMLResponse
import uvicorn

app = FastAPI()


@app.get("/index")
async def index():
    response1 = HTMLResponse("<h1>你好呀</h1>")
    response2 = Response("<h1>你好呀</h1>",
                         media_type="text/html")
    # 以上两者是等价的，在 HTMLResponse 里面
    # 会自动将 media_type 设置成 text/html
    return response1
