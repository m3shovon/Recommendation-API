from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database
from ..recommendation import recommend_movies

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/", response_model=list[schemas.MovieResponse])
def get_movies(skip: int = 0, limit: int = 10, db: Session = Depends(database.SessionLocal)):
    return db.query(models.Movie).offset(skip).limit(limit).all()

@router.post("/", response_model=schemas.MovieResponse)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(database.SessionLocal)):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.post("/recommend")
def recommend_movies_endpoint(user_preferences: dict, db: Session = Depends(database.SessionLocal)):
    # Load movie data
    movies = db.query(models.Movie).all()
    movie_data = [movie.genres for movie in movies]  # Example feature
    # Get recommendations
    recommendations = recommend_movies(user_preferences, movie_data)
    return [movies[i].title for i in recommendations]