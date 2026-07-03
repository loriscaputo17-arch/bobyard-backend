# Bobyard Comments

Comment system with admin/user roles, built with FastAPI + React.

## Stack
- **Backend**: FastAPI, SQLAlchemy, SQLite
- **Frontend**: React, Vite, Tailwind CSS

## Setup

### Backend
```bash
cd backend
pip install fastapi uvicorn sqlalchemy pydantic
python seed.py
uvicorn main:app --reload
```
API running at `http://localhost:8000`
Docs at `http://localhost:8000/docs`

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/comments` | List all comments |
| POST | `/comments` | Add a comment (Admin) |
| PATCH | `/comments/{id}` | Edit comment text |
| DELETE | `/comments/{id}` | Delete a comment |

## Features
- List, add, edit, delete comments
- Admin / User role switcher
- Images with fullscreen lightbox
- Responsive layout with mobile drawer
- Optimistic UI updates

## What I'd add with more time
- Reply threading (`parent_id` on Comment model)
- Like/unlike toggle endpoint
- Real authentication (JWT)
- Migrate to PostgreSQL

The backend is deployed on a free istance of Render: https://bobyard-backend.onrender.com