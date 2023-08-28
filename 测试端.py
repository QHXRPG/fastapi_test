import requests

#%%
response1 = requests.post("http://127.0.0.1:8000/girl",
                            json={"name":"qhx", "age":17, "length":155}).json()

#%%
response2 = requests.post("http://127.0.0.1:8000/user",
                          data={"username": "qhx",
                                "password": "asdasd",
                                "not_exists": ""}).json()

#%%
response3 = requests.post("http://127.0.0.1:8000/file1",
                          files={"file":open("/Users/qiuhaoxuan/Downloads/LICENSE.txt","rb")}).json()
response4 = requests.post("http://127.0.0.1:8000/file2",
                          files={"file":open("/Users/qiuhaoxuan/Downloads/tes.txt","rb")}).json()

#%%
response5 = requests.get("http://127.0.0.1:8000/user/qhx@qq.com").json()

#%%
response6 = requests.get("http://127.0.0.1:8000").json()
respon6 = requests.get("http://127.0.0.1:8000")
print(respon6.headers["status"])
response7 = requests.get("http://127.0.0.1:8000", headers={"ping": "pong"}).json()
respon7 = requests.get("http://127.0.0.1:8000", headers={"ping": "pong"})
print(respon7.headers["status"])