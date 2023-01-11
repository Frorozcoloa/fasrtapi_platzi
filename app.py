from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"
movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get("/", tags=["home"])
def message():
    return HTMLResponse(content="<h1>¡Hola mundo!</h1>", status_code=200)

@app.get("/movies", tags=["movies"])
def get_movies():
    return movies

@app.get("/movie/{movie_id}", tags=["movies"])
def get_movie(movie_id: int):
    movie = list(filter(lambda x: x['id'] == movie_id,movies))
    return movie

@app.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str, year:int):
    movie = list(filter(lambda x: x['category'] == category,movies))
    return movie