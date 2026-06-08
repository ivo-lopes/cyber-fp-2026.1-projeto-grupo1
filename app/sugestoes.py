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

def buscar_sugestoes(tipo_evento, num_convidados):
    sugestao_generica = None

    try:
        with open(CAMINHO_SUGESTOES, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=";")

            for linha in leitor:
                tipo_csv = linha["tipo_evento"].strip().lower()

                try:
                    minimo = int(linha["min_convidados"])
                    maximo = int(linha["max_convidados"])
                except:
                    continue

                if tipo_csv == "generico":
                    sugestao_generica = linha

                if (
                    tipo_csv == tipo_evento.strip().lower()
                    and minimo <= num_convidados <= maximo
                ):
                    return linha
    except FileNotFoundError:
        print("\nArquivo de sugestões não encontrado.")
        return None

    return sugestao_generica

def exibir_categoria_sugestao(titulo, valor):
    print(f"\n{titulo}:")

    for item in formatar_lista_sugestoes(valor):
        print(f"- {item}")
