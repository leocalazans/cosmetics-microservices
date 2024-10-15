from fastapi import FastAPI
from .routes import router
from .database import engine
from .models import Base

app = FastAPI( 
    title="API Carrinho",
    description="api carrinho e checkout",
    version="1.0.0"
    )

Base.metadata.create_all(bind=engine)

app.include_router(router)
