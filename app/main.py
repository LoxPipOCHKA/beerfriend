from fastapi import FastAPI, Query
from beers.Review import Review

app = FastAPI()

@app.get('/variety')
async def variety():
    return 'endpoint variety='

@app.get('/beers')
async def beers(
                variety_id: int = Query(ge=1, le=8)):
    return 'endpoint beers, variety_id = ' + str(variety_id)

@app.get('/beers/{beer_id}')
async def beer_id(beer_id: int):
    return 'endpoint beer_id= '+ str(beer_id)

@app.post('/beers/{beer_id}/review')
async def review(
                beer_id: int,
                review: Review):
    return 'endpoint review : ' + 'nick = '+review.nick + ', comment = ' + review.comment + ', estimation = ' + str(review.estimation)