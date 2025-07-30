FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y curl sqlite3

COPY . .

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]