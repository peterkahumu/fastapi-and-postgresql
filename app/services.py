from app.models import Book
from sqlalchemy.orm import Session
from app.schemas import BookCreate, BookUpdate


def create_book(db : Session, data : BookCreate):
    """Add a new book to the Database"""
    book_instance = Book(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)

    return book_instance

def get_books(db: Session):
    """Return all books in the Database"""
    return db.query(Book).all()

def get_book(db : Session, book_id : int):
    """Return a specific book using id (primary key)"""
    return db.query(Book).filter(Book.id == book_id).first()

def update_book_info(book_id, book_data : BookUpdate, db : Session):
    """Partially update the values of a book."""
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        for key, value in book_data.model_dump(exclude_unset=True).items():
            setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book

def delete_book(book_id : int, db : Session):
    """Remove a book from the database"""
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book