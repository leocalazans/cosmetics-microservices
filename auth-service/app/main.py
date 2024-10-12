from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .config import settings
from .schemas import UserCreate, UserOut
from .crud import create_user
from .database import SessionLocal, engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user
