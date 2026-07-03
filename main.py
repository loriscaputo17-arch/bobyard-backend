from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://bobyard-frontend.vercel.app",],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/comments", response_model=List[schemas.CommentOut])
def get_comments(db: Session = Depends(get_db)):
    return db.query(models.Comment).order_by(models.Comment.created_at.desc()).all()

@app.post("/comments", response_model=schemas.CommentOut, status_code=201)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_comment = models.Comment(
        text=comment.text,
        author=comment.author,
        created_at=datetime.utcnow(),
        likes=0,
        images=[]
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@app.patch("/comments/{comment_id}", response_model=schemas.CommentOut)
def update_comment(comment_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    db_comment.text = comment.text
    db_comment.author = comment.author
    db.commit()
    db.refresh(db_comment)
    return db_comment

@app.delete("/comments/{comment_id}", status_code=204)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    db.delete(db_comment)
    db.commit()
    return None