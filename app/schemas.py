from pydantic import BaseModel

class BookBase(BaseModel):
    title : str
    description : str
    author : str
    year : int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title : str | None = None
    description : str | None = None
    author : str | None = None
    year : int | None = None

class Book(BookBase):
    id : int

    class Config:
        # orm_mode = True
        from_attributes = True