from fastapi import (
    FastAPI,
    Depends,
    HTTPException
)
from app import (
    models,
    schemas,
    services
)
from app.db import get_db, engine
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/books/", response_model = list[schemas.Book])
async def get_all_books(db : Session = Depends(get_db)):
    return services.get_books()

@app.get("/books/", response_model=schemas.Book)
async def create_new_book(book : schemas.BookCreate, db : Session = Depends(get_db)):
    return services.create_book(db, book)