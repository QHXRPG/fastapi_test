"""
假设你的前端运行在 localhost:8080，并且尝试与 localhost:5555 进行通信。
然后浏览器会向后端发送一个 HTTP OPTIONS 请求，后端会返回适当的 headers 来对这个源进行授权。
所以后端必须有一个「允许的源」列表，如果前端对应的源是被允许的，浏览器才会允许前端向后端发请求，否则就会出现跨域失败。
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # 允许跨域的源列表，例如 ["http://localhost:8080"]
    # ["*"] 表示允许任何源
    allow_origins=["*"],
    # 跨域请求是否支持 cookie，默认是 False
    # 如果为 True，allow_origins 必须为具体的源，不可以是 ["*"]
    allow_credentials=False,
    # 允许跨域请求的 HTTP 方法列表，默认是 ["GET"]
    allow_methods=["*"],
    # 允许跨域请求的 HTTP 请求头列表，默认是 []
    # 可以使用 ["*"] 表示允许所有的请求头
    # 当然下面几个请求头总是被允许的
    # Accept、Accept-Language、Content-Language、Content-Type
    allow_headers=["*"],
    # 可以被浏览器访问的响应头, 默认是 []，一般很少指定
    # expose_headers=["*"]
    # 设定浏览器缓存 CORS 响应的最长时间，单位是秒
    # 默认为 600，一般也很少指定
    # max_age=1000
)
