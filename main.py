from fastapi import FastAPI
import uvicorn

# 类似于 app = Flask(__name__)
app = FastAPI()


# 绑定路由和视图函数
@app.get("/")
async def index():
    return {"name": "古明地觉"}


# 在 Windows 中必须加上 if __name__ == "__main__"
# 否则会抛出 RuntimeError: This event loop is already running
if __name__ == "__main__":
    # 启动服务，因为我们这个文件叫做 main.py
    # 所以需要启动 main.py 里面的 app
    # 第一个参数 "main:app" 就表示这个含义
    # 然后是 host 和 port 表示监听的 ip 和端口
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
