from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# name 参数只是起一个名字，FastAPI 内部使用
app.mount("/static",
          StaticFiles(directory=r"/Users/qiuhaoxuan/Downloads"),
          name="static")

if __name__ == "__main__":
    uvicorn.run("返回静态资源:app", host="127.0.0.1", port=8000)
