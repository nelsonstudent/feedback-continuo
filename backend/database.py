from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho para o banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./feedback.db"

# Cria o engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria a sessão com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()
