from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    Query
)
from app import (
    models,
    schemas,
    services
)
from app.db import get_db, engine
from sqlalchemy.orm import Session

app = FastAPI(
    title="Book API",
    description="A simple CRUD API for managing books",
    version="1.0.0"
)

@app.get("/books/", response_model = list[schemas.Book])
def get_all_books(db : Session = Depends(get_db)):
    return services.get_books(db)

@app.get("/books/{book_id}/", response_model = schemas.Book)
def get_specific_book(book_id: int , db: Session = Depends(get_db)):
    book = services.get_book(db, book_id)
    
    if not book:
        raise HTTPException(status_code = 404, detail = "Book not found")
    return book

@app.post("/books/", response_model=schemas.Book)
def create_new_book(book : schemas.BookCreate, db : Session = Depends(get_db)):
    return services.create_book(db, book)

@app.patch("/books/{book_id}/", response_model=schemas.Book)
def update_book(book_id : int, book_data : schemas.BookUpdate, db : Session = Depends(get_db)):
    book_update = services.update_book_info(book_id, book_data, db)
    if not book_update:
        raise HTTPException(status_code = 404, detail = "Book not found")
    return book_update

@app.delete("/books/{book_id}/", response_model = schemas.Book)
def delete_book(book_id : int, db : Session = Depends(get_db)):
    book =  services.delete_book(book_id, db)
    if not book:
        raise HTTPException(status_code = 404, detail="Book not found")
    return book