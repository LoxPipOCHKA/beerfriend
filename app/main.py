from fastapi import FastAPI

app = FastAPI()

@app.get('/variety')
async def variety():
    return 'ПРИВЕТ ПИДОРЫ ручка variety'

@app.get('/beers')
async def beers():
    return 'ручка beers GHBDTN PIDOR'

@app.get('/beers/{beer_id}')
async def beer_id():
    return 'ручка beer_id пидор'

@app.post('/beers/{beer_id}/review')
async def review():
    return 'endpoint review pidoras'