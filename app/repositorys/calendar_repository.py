from googleapiclient.discovery import build
from datetime import datetime, timedelta
from app.config import GOOGLE_CREDENTIALS

def listar_eventos_hoje():
    creds = GOOGLE_CREDENTIALS
    service = build('calendar', 'v3', credentials=creds)
    agora = datetime.now(datetime.timezone.utc).isoformat() + 'Z'  # 'Z' indica UTC
    # Define o intervalo de tempo para hoje
    hoje = datetime.now(datetime.timezone.utc).isoformat() + 'Z'  # 'Z' indica UTC
    fim_do_dia = (datetime.now(datetime.timezone.utc) + timedelta(days=1)).isoformat() + 'Z'

    eventos = service.events().list(
        calendarId='primary',
        timeMin=hoje,
        timeMax=fim_do_dia,
        singleEvents=True,
        orderBy='startTime'
    ).execute().get('items', [])
    return eventos