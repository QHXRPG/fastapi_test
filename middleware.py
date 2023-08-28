"""
中间件在 web 开发中可以说是非常常见了，说白了中间件就是一个函数或者一个类。
在请求进入视图函数之前，会先经过中间件（被称为请求中间件），
在里面我们可以对请求进行一些预处理，或者实现一个拦截器等等；
同理当视图函数返回响应之后，也会经过中间件（被称为响应中间件）
"""
from fastapi import FastAPI, Request, Response
import uvicorn
import orjson

#%% 自定义中间件
app = FastAPI()

@app.get("/")
async def view_func(request: Request):
    return {"name": "古明地觉"}

@app.middleware("http")
async def middleware(request: Request, call_next):
    """
    定义一个协程函数，然后使用 @app.middleware("http") 装饰
    即可得到中间件
    """
    # 请求到来时会先经过这里的中间件
    if request.headers.get("ping", "") != "pong":
        response = Response(content=orjson.dumps({"error": "请求头中缺少指定字段"}),
                            media_type="application/json",
                            status_code=404)
        # 当请求头中缺少 "ping": "pong"
        # 在中间件这一步就直接返回了，就不会再往下走了
        # 所以此时相当于实现了一个拦截器
        return response
    # 如果条件满足，则执行await call_next(request)，关键是这里的 call_next
    # 如果该中间件后面还有中间件，那么 call_next 就是下一个中间件；
    # 如果没有，那么 call_next 就是对应的视图函数
    # 这里显然是视图函数，因此执行之后会拿到视图函数返回的 Response 对象
    response: Response = await call_next(request)
    # 我们对 response 做一些润色，比如设置一个响应头
    # 所以我们看到在 FastAPI 中，请求中间件和响应中间件合在一起了
    response.headers["status"] = "success"
    return response

if __name__ == '__main__':
    uvicorn.run('middleware:app', host="127.0.0.1", port=8000)