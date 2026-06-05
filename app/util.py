import os
from datetime import datetime


def limpar_tela():
    # Limpa a tela de acordo com o sistema usado.
    if os.name == "nt":
        os.system("cls")
    elif "TERM" in os.environ:
        os.system("clear")
    else:
        print("\n" * 5)


def calcular_dias_restantes(data_evento):
    # Calcula quantos dias faltam para a data do evento.
    try:
        data = datetime.strptime(data_evento, "%Y-%m-%d").date()
        hoje = datetime.now().date()
        diferenca = data - hoje
        return diferenca.days
    except:
        return 0
