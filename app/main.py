# from typing import Union
from fastapi import FastAPI
from .routers import movies
from .database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(movies.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Movie Recommendation API"}
