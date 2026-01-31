# FastAPI Book API with PostgreSQL

A simple RESTful API for managing books, built with FastAPI and PostgreSQL.

## Features

- 📚 CRUD operations for books
- 🐘 PostgreSQL database with SQLAlchemy ORM
- 🐳 Docker support for easy deployment
- 📖 Auto-generated API documentation (Swagger UI)

## Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **PostgreSQL** - Relational database
- **SQLAlchemy** - Python SQL toolkit and ORM
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server
- **Docker** - Containerization

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (for containerized setup)
- PostgreSQL (for local setup)

### Installation

#### Using Docker (Recommended)

```bash
docker-compose up --build
```

#### Local Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-and-postgresql
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables (create a `.env` file):
```env
DATABASE_URL=postgresql://user:password@localhost:5432/books_db
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/` | Get all books |
| GET | `/books/{book_id}/` | Get a specific book |
| POST | `/books/` | Create a new book |
| PATCH | `/books/{book_id}/` | Update a book (partial) |
| DELETE | `/books/{book_id}/` | Delete a book |

## API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Project Structure

```
fastapi-and-postgresql/
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI application and routes
│   ├── models.py       # SQLAlchemy database models
│   ├── schemas.py      # Pydantic schemas for validation
│   ├── services.py     # Business logic / CRUD operations
│   └── db.py           # Database connection setup
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
├── LICENSE
└── README.md
```

## Example Usage

### Create a Book

```bash
curl -X POST "http://localhost:8000/books/" \
  -H "Content-Type: application/json" \
  -d '{"title": "The Great Gatsby", "description": "A novel by F. Scott Fitzgerald", "author": "F. Scott Fitzgerald", "year": 1925}'
```

### Get All Books

```bash
curl "http://localhost:8000/books/"
```

### Update a Book

```bash
curl -X PATCH "http://localhost:8000/books/1/" \
  -H "Content-Type: application/json" \
  -d '{"year": 1926}'
```

### Delete a Book

```bash
curl -X DELETE "http://localhost:8000/books/1/"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
