from app.armazenamento import ler_csv


CAMINHO_SUGESTOES = "data/sugestoes.csv"
MENSAGEM_GENERICA = "não encontramos uma sugestão específica para esse evento, mas você pode revisar fornecedores, decoração, cardápio e atividades de forma manual."


def formatar_lista_sugestoes(valor):
    itens = valor.split("|")
    lista_formatada = []

    for item in itens:
        item = item.strip()

        if item != "":
            lista_formatada.append(item)

    return lista_formatada


def convidados_na_faixa(sugestao, num_convidados):
    try:
        minimo = int(sugestao["min_convidados"])
        maximo = int(sugestao["max_convidados"])
        return minimo <= num_convidados <= maximo
    except:
        return True


def buscar_sugestoes(tipo_evento, num_convidados):
    sugestoes = ler_csv(CAMINHO_SUGESTOES)
    sugestao_generica = None

    try:
        convidados = int(num_convidados)
    except:
        convidados = -1

    for sugestao in sugestoes:
        tipo = sugestao["tipo_evento"].strip().lower()

        if tipo == "generico" or tipo == "genérico" or tipo == "geral":
            if sugestao_generica == None:
                sugestao_generica = sugestao

        if tipo == tipo_evento.strip().lower() and convidados_na_faixa(sugestao, convidados):
            return sugestao

    return sugestao_generica


def exibir_sugestoes_evento():
    tipo_evento = input("Tipo do evento: ").strip()
    num_convidados = input("Número de convidados: ").strip()
    sugestao = buscar_sugestoes(tipo_evento, num_convidados)

    if sugestao == None:
        print("\n" + MENSAGEM_GENERICA)
        return

    print("\n========== SUGESTÕES ==========")
    print("Fornecedores:", sugestao["fornecedores"])
    print("Decoração:", sugestao["decoracao"])
    print("Cardápio:", sugestao["cardapio"])
    print("Atividades:", sugestao["atividades"])
