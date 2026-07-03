# Bobyard Comments — Backend

RESTful API for a comment system, built with FastAPI + SQLAlchemy.

**Frontend repo:** https://github.com/loriscaputo17-arch/bobyard-frontend
**Live API:** https://bobyard-backend.onrender.com
**API docs:** https://bobyard-backend.onrender.com/docs

## Stack
- FastAPI
- SQLAlchemy
- SQLite

## Setup
```bash
cd backend
pip install -r requirements.txt
python seed.py          # loads comments.json into the database
uvicorn main:app --reload
```
API runs at `http://localhost:8000`
Interactive docs at `http://localhost:8000/docs`

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/comments` | List all comments |
| POST | `/comments` | Add a comment (from Admin, current timestamp) |
| PATCH | `/comments/{id}` | Edit comment text |
| DELETE | `/comments/{id}` | Delete a comment |

## Data model
Each comment has: `id`, `text`, `author`, `created_at`, `likes`, `images`.

## What I'd add with more time
- Reply threading (`parent_id` on the Comment model)
- Like/unlike toggle endpoint
- Authentication (JWT) so only authors edit their own comments
- Migrate from SQLite to PostgreSQL
- Pagination on the list endpoint