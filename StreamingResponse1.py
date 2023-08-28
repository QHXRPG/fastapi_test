from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn

app = FastAPI()

async def some_video():
    for i in range(5):
        yield f"video {i} bytes ".encode("utf-8")

@app.get("/index")
async def index():
    return StreamingResponse(some_video())

if __name__ == '__main__':
    uvicorn.run('StreamingResponse1:app', host="127.0.0.1", port=8000)