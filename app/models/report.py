# app/models/report.py
from datetime import datetime
from app import db

class Report(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)
    aula_id = db.Column(db.String, nullable=False, unique=True)
    url = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
