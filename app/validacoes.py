from datetime import datetime


def validar_opcao(opcao, opcoes_validas):
    # Confere se a opcao digitada esta na lista de opcoes.
    return opcao in opcoes_validas


def validar_data(valor):
    # Verifica se a data esta no formato ano-mes-dia.
    try:
        datetime.strptime(valor, "%Y-%m-%d")
        return True
    except:
        return False
