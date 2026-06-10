import os
from datetime import datetime


VERDE = "\033[32m"
VERMELHO = "\033[31m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"


def texto_verde(texto):
    return VERDE + texto + RESET


def texto_vermelho(texto):
    return VERMELHO + texto + RESET


def texto_amarelo(texto):
    return AMARELO + texto + RESET


def texto_azul(texto):
    return AZUL + texto + RESET


def mostrar_sucesso(mensagem):
    print(texto_verde(mensagem))


def mostrar_erro(mensagem):
    print(texto_vermelho(mensagem))


def mostrar_aviso(mensagem):
    print(texto_amarelo(mensagem))


def mostrar_titulo(titulo):
    print(texto_azul("===================================="))
    print(texto_azul(titulo.center(36)))
    print(texto_azul("===================================="))


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

        data = datetime.strptime(data_evento, "%d/%m/%Y").date()
        hoje = datetime.now().date()
        diferenca = data - hoje
        return diferenca.days
    except:
        return 0
