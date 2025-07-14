# app/config.py
from dotenv import load_dotenv
import os

# carrega variáveis do arquivo .env
load_dotenv()

# Configurações do SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///feedback.db")
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False") == "True"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Caminho para as credenciais do Google Calendar (service account JSON)
GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS")

# Pasta onde os relatórios serão salvos
REPORT_STORAGE_PATH = os.getenv("REPORT_STORAGE_PATH", "reports")
