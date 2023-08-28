"""
如果处理请求的时候需要执行一个耗时任务，那么可以将其放在后台执行
"""
import time
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import Response
import uvicorn
import orjson

app = FastAPI()


def send_email(email: str, message: str = ""):
    """发送邮件，假设耗时三秒"""
    time.sleep(3)
    print(f"三秒之后邮件发送给 {email!r}, "
          f"邮件信息: {message!r}")


@app.get("/user/{email}")
async def order(email: str, bg_tasks: BackgroundTasks):
    """
    这里需要多定义一个参数
    此时任务就被添加到后台，当 Response 对象返回之后触发
    """
    # 可以添加任意多个任务
    bg_tasks.add_task(send_email, email, message="这是一封邮件")
    return Response(orjson.dumps({"message": "邮件发送成功"}))


# 我们在之前介绍 Response 的时候说过，里面有一个参数 background
# 所以我们还可以这么做
"""
bg_tasks = BackgroundTasks() # 不在参数中定义 bg_tasks
bg_tasks.add_task(send_email, email, message="这是一封邮件")
return Response(
    orjson.dumps({"message": "邮件发送成功"}),
    background=bg_tasks
)
"""

if __name__ == "__main__":
    uvicorn.run("BackgroundTasks:app", host="127.0.0.1", port=8000)