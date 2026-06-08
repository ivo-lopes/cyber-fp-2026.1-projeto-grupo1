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

def exibir_sugestoes_evento():
    tipo_evento = input("Tipo do evento: ").strip()
    convidados = input("Número de convidados: ").strip()

    if tipo_evento == "":
        print("\nTipo do evento é obrigatório.")
        return

    try:
        num_convidados = int(convidados)

        if num_convidados <= 0:
            print("\nNúmero de convidados deve ser maior que zero.")
            return
    except:
        print("\nNúmero de convidados inválido.")
        return

    sugestao = buscar_sugestoes(tipo_evento, num_convidados)

    if sugestao == None:
        print("\nNenhuma sugestão encontrada.")
        return

    print(f"\nSugestões para {tipo_evento} com {num_convidados} convidados:")
    exibir_categoria_sugestao("Fornecedores", sugestao["fornecedores"])
    exibir_categoria_sugestao("Decoração", sugestao["decoracao"])
    exibir_categoria_sugestao("Cardápio", sugestao["cardapio"])
    exibir_categoria_sugestao("Atividades", sugestao["atividades"])

