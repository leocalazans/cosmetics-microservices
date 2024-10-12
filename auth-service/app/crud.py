from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate
from .services import get_password_hash

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
