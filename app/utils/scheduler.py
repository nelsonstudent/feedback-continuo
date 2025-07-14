from apscheduler.schedulers.background import BackgroundScheduler
from app.repositories.calendar_repository import listar_eventos_hoje
from app.services.report_service import gerar_relatorio
from datetime import datetime, timedelta

scheduler = BackgroundScheduler()
def checar_e_gerar():
    agora = datetime.now()
    for evt in listar_eventos_hoje():
        fim = datetime.fromisoformat(evt['end']['dateTime'])
        if fim <= agora <= fim + timedelta(minutes=5):
            pass
        try:
            gerar_relatorio(evt['id'])
            print(f"Relatório gerado para o evento {evt['id']}")
        except Exception as e:
             print(f"[Erro ao gerar relatório para o evento] {evt['id']}: {e}")     
    print("Verificação de eventos concluída.")
scheduler.add_job(checar_e_gerar, 'interval', minutes=5)
scheduler.start()