from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.post("/file1")
async def file1(file: bytes = File(...)):
    # 此时会以字节流的形式拿到文件的具体内容
    return {"文件长度": len(file)}

@app.post("/file2")
async def file2(file: UploadFile = File(...)):
    # 会拿到文件句柄
    # 通过 await file.read() 可拿到文件内容
    return {"文件名": file.filename,
            "文件长度": len(await file.read())}

if __name__ == "__main__":
    uvicorn.run("file_upload:app", host="127.0.0.1", port=8000)
