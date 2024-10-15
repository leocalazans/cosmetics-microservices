from fastapi import FastAPI
from app.routes import auth_router
from app.database import Base, engine

app = FastAPI()

# Criação automática das tabelas
Base.metadata.create_all(bind=engine)

# Rotas de autenticação
app.include_router(auth_router)

# Root route
@app.get("/")
def read_root():
    return {"message": "Auth Service is Running"}