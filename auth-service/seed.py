from app.database import SessionLocal
from app.models import User
from app.services import get_password_hash

def create_demo_user():
    db = SessionLocal()
    demo_user = db.query(User).filter(User.username == "demo").first()
    if not demo_user:
        new_user = User(username="demo", email="demo@example.com", hashed_password=get_password_hash("password"))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print("Demo user created:", new_user.username)
    else:
        print("Demo user already exists")

if __name__ == "__main__":
    create_demo_user()
