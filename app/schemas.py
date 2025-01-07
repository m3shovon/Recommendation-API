from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    genres: str
    director: str
    actors: str
    rating: float

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int

    class Config:
        orm_mode = True
