from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    author: str = "Admin"

class Comment(CommentBase):
    text: str

class CommentOut(CommentBase):
    id: int
    author: str
    created_at: datetime
    likes: int
    images: List[str] = []

    class Config:
        from_attributes = True


