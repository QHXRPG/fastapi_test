import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="demo")

class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None

@app.get('/')
def hello_world():
    return {'hello': 'World'}

@app.get('/city/{city}')
def result(city: str, query_string: Optional[str] = None):
    return {'city':city,
            'query_string': query_string}

@app.put('city/{city}')
def result(city:str, city_info:CityInfo):
    return {'city':city, 'country':city_info.country, 'is_affected':city_info.is_affected}

if __name__ == '__main__':
    uvicorn.run('BaseModel:app', host="127.0.0.1", port=8000)