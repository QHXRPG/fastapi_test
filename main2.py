import requests
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/int")
async def index1():
    return 666

@app.get("/str")
async def index2():
    return "古明地觉"

@app.get("/bytes")
async def index3():
    return b"satori"

@app.get("/tuple")
async def index4():
    return ("古明地觉", "古明地恋", "雾雨魔理沙")

@app.get("/list")
async def index5():
    return [{"name": "古明地觉", "age": 17},
            {"name": "古明地恋", "age": 16}]

if __name__ == "__main__":
    uvicorn.run("main2:app", host="127.0.0.1", port=8000)






