import csv

CAMINHO_SUGESTOES = "data/sugestoes.csv"


def formatar_lista_sugestoes(valor):
    itens = valor.split("|")
    lista_formatada = []

    for item in itens:
        item = item.strip()

        if item != "":
            lista_formatada.append(item)

    return lista_formatada