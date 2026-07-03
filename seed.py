import json
from database import SessionLocal, engine
from models import Comment, Base  # ← aggiungi Base
from datetime import datetime

def seed():
    Base.metadata.create_all(bind=engine)  # ← aggiungi questa riga
    db = SessionLocal()
    try:
        if db.query(Comment).count() > 0:
            print("Database already seeded.")
            return
        with open('comments.json', 'r') as f:
            data = json.load(f)
        for item in data["comments"]:
            comment = Comment(
                text=item['text'],
                author=item['author'],
                created_at=datetime.fromisoformat(item['date'].replace("Z", "+00:00")),
                likes=item.get('likes', 0),
                images=[item['image']] if item.get('image') else [],
            )
            db.add(comment)
        db.commit()
        print(f"Seeded {len(data['comments'])} comments.")
    except Exception as e:
        print(f"Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed()