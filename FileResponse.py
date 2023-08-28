"""
我们可以返回图片、音频、视频，以字节流的形式
但光有字节流还不够，我们还要告诉 Chrome
拿到这坨字节流之后，应该要如何解析
此时需要通过响应头里面的 Content-Type 指定
Response(
    b"picture | audio | video bytes data",
    # png 图片："image/png"
    # mp3 音频："audio/mp3"
    # mp4 视频："video/mp4"
    media_type="image/png"
)
"""

#通过 Content-Type，Chrome 就知道该如何解析了，至于不同格式的文件会对应哪一种 Content-Type，标准库也提供了一个模块帮我们进行判断。
from mimetypes import guess_type
from fastapi import FastAPI, Response
import uvicorn

# 根据文件后缀进行判断
print(guess_type("1.png")[0])
print(guess_type("1.jpg")[0])
print(guess_type("1.mp3")[0])
print(guess_type("1.mp4")[0])
print(guess_type("1.wav")[0])
print(guess_type("1.flv")[0])
print(guess_type("1.pdf")[0])
"""
image/png
image/jpeg
audio/mpeg
video/mp4
audio/x-wav
video/x-flv
application/pdf
"""

app = FastAPI()

#显示在界面上
@app.get("/file1")
async def get_file1():
    # 读取字节流（任何类型的文件都可以）
    with open("/Users/qiuhaoxuan/Downloads/00004-1998727032.png", "rb") as f:
        data = f.read()
    # 返回的时候通过 Content-Type 告诉 Chrome 文件类型
    # 尽管 Chrome 比较智能，会自动判断，但最好还是指定一下
    return Response(data,
                    # 返回的字节流是 jpg 格式
                    media_type="image/jpeg")
    # Chrome 在拿到字节流时会直接将图片渲染在页面上


# 直接下载
@app.get("/file2")
async def get_file2():
    with open("/Users/qiuhaoxuan/Downloads/00004-1998727032.png", "rb") as f:
        data = f.read()
    # 在响应头中指定 Content-Disposition
    # 意思就是告诉 Chrome，你不要解析了，直接下载下来
    # filename 后面跟的就是文件下载之后的文件名
    return Response(
        data,
        # 既然都下载下来了，也就不需要 Chrome 解析了
        # 将响应类型指定为 application/octet-stream
        # 表示让 Chrome 以二进制格式直接下载
        media_type="application/octet-stream",
        headers={"Content-Disposition": "attachment; filename=img.png"})

if __name__ == "__main__":
    uvicorn.run("FileResponse:app", host="127.0.0.1", port=8000)

