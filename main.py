import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timezone
from typing import List
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://bobyard-frontend.vercel.app",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CommentCreate(BaseModel):
    text: str
    author: str = "Admin"
    images: List[str] = []

class CommentUpdate(BaseModel):
    text: str

@app.get("/comments")
def list_comments():
    res = supabase.table("comments").select("*").order("created_at", desc=True).execute()
    return res.data

@app.post("/comments", status_code=201)
def create_comment(comment: CommentCreate):
    payload = {
        "text": comment.text,
        "author": "Admin",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "likes": 0,
        "images": comment.images,
    }
    res = supabase.table("comments").insert(payload).execute()
    return res.data[0]

@app.patch("/comments/{comment_id}")
def update_comment(comment_id: int, comment: CommentUpdate):
    res = supabase.table("comments").update({"text": comment.text}).eq("id", comment_id).execute()
    if not res.data:
        raise HTTPException(status_code=404, detail="Comment not found")
    return res.data[0]

@app.delete("/comments/{comment_id}", status_code=204)
def delete_comment(comment_id: int):
    res = supabase.table("comments").delete().eq("id", comment_id).execute()
    if not res.data:
        raise HTTPException(status_code=404, detail="Comment not found")
    return None