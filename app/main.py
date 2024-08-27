from fastapi import FastAPI, Query
from typing import Optional
from pydantic import  BaseModel

app = FastAPI()

@app.get('/variety')
async def variety(variety: int):
    return 'endpoint variety='+ {variety}

@app.get('/beers')
async def beers(beers: str,
                variety: Optional[int]= Query(None, ge=1, le=8)):
    return 'endpoint beers='+ {beers}

@app.get('/beers/{beer_id}')
async def beer_id(beer_id: int):
    return 'endpoint beer_)id='+ {beer_id}


class Sreview(BaseModel):
    name_beer: str
    comment: str
    nick: str
    estimation: int


@app.post('/beers/{beer_id}/review')
async def review(beers: str,
                 beer_id: int,
                review: Sreview):
    return 'endpoint review='+ Sreview

