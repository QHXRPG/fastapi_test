from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn

app = FastAPI()

# 读取指定文件
@app.get("/index")
async def index():
    return StreamingResponse(open("/Users/qiuhaoxuan/Downloads/LICENSE.txt", encoding="utf-8"))

if __name__ == '__main__':
    uvicorn.run('StreamingResponse2:app', host="127.0.0.1", port=8000)
