from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base
from app.crud import create_user
from app.schemas import UserCreate

# Garante que todas as tabelas estão criadas
Base.metadata.create_all(bind=engine)

# Sessão de banco de dados
db: Session = SessionLocal()

# Dados do usuário demo
user_data = UserCreate(username="demo_user", email="demo@cosmeticsstore.com", password="password123")

# Verifica se o usuário já existe
user = db.query(User).filter_by(email=user_data.email).first()
if not user:
    # Cria o usuário demo
    create_user(db, user_data)
    print(f"Usuário demo criado com sucesso: {user_data.username}")
else:
    print("Usuário demo já existe.")

# Fechar sessão
db.close()
