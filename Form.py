"""
我们调用 requests.post，如果参数通过 data 传递的话，则相当于提交了一个 form 表单，
那么在 FastAPI 中可以通过 await request.form() 进行获取，
注意：内部同样会先调用 await request.body()。
"""
from fastapi import FastAPI, Form
import uvicorn

app = FastAPI()

@app.post("/user")
async def get_user(username: str = Form(...),
                   password: str = Form(...)):
    return {"username": username, "password": password}

if __name__ == "__main__":
    uvicorn.run("Form:app", host="127.0.0.1", port=8000)
