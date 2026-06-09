import os
from datetime import datetime


def limpar_tela():
    
    if os.name == "nt":
        os.system("cls")
    elif "TERM" in os.environ:
        os.system("clear")
    else:
        print("\n" * 5)


def calcular_dias_restantes(data_evento):
    
    try:
        data_evento = data_evento.strip()

        if data_evento == "":
            return 0

        data = datetime.strptime(data_evento, "%Y-%m-%d").date()
        hoje = datetime.now().date()
        diferenca = data - hoje
        return diferenca.days
    except:
        return 0
