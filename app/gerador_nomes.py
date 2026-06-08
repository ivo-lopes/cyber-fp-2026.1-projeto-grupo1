import random

from app.armazenamento import ler_csv


CAMINHO_NOMES = "data/nomes_eventos.csv"


def carregar_partes_nomes():
    registros = ler_csv(CAMINHO_NOMES)
    partes = {
        "string1": [],
        "string2": [],
        "string3": [],
    }

    for registro in registros:
        if registro["string1"].strip() != "":
            partes["string1"].append(registro["string1"])

        if registro["string2"].strip() != "":
            partes["string2"].append(registro["string2"])

        if registro["string3"].strip() != "":
            partes["string3"].append(registro["string3"])

    return partes


def escolher_item_aleatorio(lista):
    if len(lista) == 0:
        return ""

    return random.choice(lista)


def gerar_nome_evento():
    partes = carregar_partes_nomes()

    primeira = escolher_item_aleatorio(partes["string1"])
    segunda = escolher_item_aleatorio(partes["string2"])
    terceira = escolher_item_aleatorio(partes["string3"])

    if primeira == "" or segunda == "" or terceira == "":
        return "Evento Especial"

    return primeira + " " + segunda + " " + terceira
