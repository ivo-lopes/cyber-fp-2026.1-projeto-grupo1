from app.armazenamento import ler_csv
from app.validacoes import pedir_inteiro_positivo_cancelavel, pedir_texto_cancelavel


CAMINHO_SUGESTOES = "data/sugestoes.csv"


def formatar_lista_sugestoes(valor):
    itens = valor.split("|")
    lista_formatada = []

    for item in itens:
        item = item.strip()

        if item != "":
            lista_formatada.append(item)

    return lista_formatada


def normalizar_tipo_evento(valor):
    valor = valor.strip().lower()
    valor = valor.replace("á", "a").replace("à", "a").replace("ã", "a").replace("â", "a")
    valor = valor.replace("é", "e").replace("ê", "e")
    valor = valor.replace("í", "i")
    valor = valor.replace("ó", "o").replace("ô", "o").replace("õ", "o")
    valor = valor.replace("ú", "u")
    valor = valor.replace("ç", "c")
    return valor


def buscar_sugestoes(tipo_evento, num_convidados):
    sugestoes = ler_csv(CAMINHO_SUGESTOES)
    sugestao_generica = None
    tipo_pesquisado = normalizar_tipo_evento(tipo_evento)

    for sugestao in sugestoes:
        tipo_csv = normalizar_tipo_evento(sugestao["tipo_evento"])

        try:
            minimo = int(sugestao["min_convidados"])
            maximo = int(sugestao["max_convidados"])
        except:
            continue

        if tipo_csv == "generico":
            sugestao_generica = sugestao

        if tipo_csv == tipo_pesquisado and minimo <= num_convidados <= maximo:
            return sugestao

    return sugestao_generica


def exibir_categoria_sugestao(titulo, valor):
    print(f"\n{titulo}:")

    for item in formatar_lista_sugestoes(valor):
        print(f"- {item}")


def exibir_sugestoes_evento():
    tipo_evento = pedir_texto_cancelavel("Tipo do evento ou 0 para cancelar: ")

    if tipo_evento == None:
        print("\nConsulta cancelada.")
        return

    num_convidados = pedir_inteiro_positivo_cancelavel("Número de convidados ou 0 para cancelar: ")

    if num_convidados == None:
        print("\nConsulta cancelada.")
        return

    sugestao = buscar_sugestoes(tipo_evento, num_convidados)

    if sugestao == None:
        print("\nNenhuma sugestão encontrada.")
        return None

    print(f"\nSugestões para {tipo_evento} com {num_convidados} convidados:")
    exibir_categoria_sugestao("Fornecedores", sugestao["fornecedores"])
    exibir_categoria_sugestao("Decoração", sugestao["decoracao"])
    exibir_categoria_sugestao("Cardápio", sugestao["cardapio"])
    exibir_categoria_sugestao("Atividades", sugestao["atividades"])

    return sugestao
