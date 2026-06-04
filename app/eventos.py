from datetime import datetime

from app.armazenamento import ler_csv, escrever_csv
from app.validacoes import validar_data


CAMINHO_EVENTOS = "data/eventos.csv"
CAMINHO_TAREFAS = "data/tarefas.csv"
CABECALHO_EVENTOS = [
    "id",
    "nome",
    "tipo",
    "data",
    "local",
    "orcamento_inicial",
    "orcamento_disponivel",
    "num_convidados",
    "criado_em",
    "atualizado_em",
]
CABECALHO_TAREFAS = [
    "id",
    "evento_id",
    "descricao",
    "categoria",
    "custo",
    "status",
    "prazo",
    "criado_em",
    "atualizado_em",
]


def cadastrar_evento():
    print("\nFuncionalidade ainda não implementada.")


def listar_eventos():
    print("\nFuncionalidade ainda não implementada.")


def visualizar_evento():
    print("\nFuncionalidade ainda não implementada.")


def buscar_evento_por_id(evento_id):
    # Procura o evento pelo ID informado pelo usuario.
    eventos = ler_csv(CAMINHO_EVENTOS)

    for evento in eventos:
        if evento["id"] == evento_id:
            return evento

    return None


def pedir_texto_opcional(nome_campo, valor_atual):
    novo_valor = input(nome_campo + " [" + valor_atual + "]: ").strip()

    if novo_valor == "":
        return valor_atual

    return novo_valor


def pedir_data_opcional(valor_atual):
    while True:
        nova_data = input("Data [" + valor_atual + "]: ").strip()

        if nova_data == "":
            return valor_atual

        if validar_data(nova_data):
            return nova_data

        print("Data inválida. Use o formato AAAA-MM-DD.")


def pedir_numero_opcional(nome_campo, valor_atual):
    while True:
        novo_valor = input(nome_campo + " [" + valor_atual + "]: ").strip()

        if novo_valor == "":
            return valor_atual

        try:
            numero = float(novo_valor)

            if numero >= 0:
                return novo_valor

            print("Digite um número positivo.")
        except:
            print("Digite um número válido.")


def pedir_inteiro_opcional(nome_campo, valor_atual):
    while True:
        novo_valor = input(nome_campo + " [" + valor_atual + "]: ").strip()

        if novo_valor == "":
            return valor_atual

        try:
            numero = int(novo_valor)

            if numero >= 0:
                return novo_valor

            print("Digite um número inteiro positivo.")
        except:
            print("Digite um número inteiro válido.")


def editar_evento():
    eventos = ler_csv(CAMINHO_EVENTOS)

    if len(eventos) == 0:
        print("\nNenhum evento cadastrado.")
        return

    evento_id = input("ID do evento: ").strip()
    evento_encontrado = None

    for evento in eventos:
        if evento["id"] == evento_id:
            evento_encontrado = evento

    if evento_encontrado == None:
        print("\nEvento não encontrado.")
        return

    print("\nDeixe em branco para manter o valor atual.")

    evento_encontrado["nome"] = pedir_texto_opcional("Nome", evento_encontrado["nome"])
    evento_encontrado["tipo"] = pedir_texto_opcional("Tipo", evento_encontrado["tipo"])
    evento_encontrado["data"] = pedir_data_opcional(evento_encontrado["data"])
    evento_encontrado["local"] = pedir_texto_opcional("Local", evento_encontrado["local"])

    orcamento_antigo = evento_encontrado["orcamento_inicial"]
    novo_orcamento = pedir_numero_opcional("Orçamento inicial", orcamento_antigo)
    evento_encontrado["orcamento_inicial"] = novo_orcamento

    if novo_orcamento != orcamento_antigo:
        evento_encontrado["orcamento_disponivel"] = novo_orcamento

    evento_encontrado["num_convidados"] = pedir_inteiro_opcional(
        "Número de convidados",
        evento_encontrado["num_convidados"],
    )
    evento_encontrado["atualizado_em"] = datetime.now().strftime("%Y-%m-%d")

    escrever_csv(CAMINHO_EVENTOS, CABECALHO_EVENTOS, eventos)
    print("\nEvento atualizado com sucesso.")


def excluir_evento():
    eventos = ler_csv(CAMINHO_EVENTOS)

    if len(eventos) == 0:
        print("\nNenhum evento cadastrado.")
        return

    evento_id = input("ID do evento: ").strip()
    evento_encontrado = buscar_evento_por_id(evento_id)

    if evento_encontrado == None:
        print("\nEvento não encontrado.")
        return

    tarefas = ler_csv(CAMINHO_TAREFAS)
    tarefas_vinculadas = []

    for tarefa in tarefas:
        if tarefa["evento_id"] == evento_id:
            tarefas_vinculadas.append(tarefa)

    if len(tarefas_vinculadas) > 0:
        print("\nEste evento possui tarefas cadastradas.")
        resposta = input("Deseja excluir o evento e todas as tarefas vinculadas? [s/n] ").strip().lower()

        if resposta != "s":
            print("\nExclusão cancelada.")
            return

        novas_tarefas = []

        for tarefa in tarefas:
            if tarefa["evento_id"] != evento_id:
                novas_tarefas.append(tarefa)

        escrever_csv(CAMINHO_TAREFAS, CABECALHO_TAREFAS, novas_tarefas)
    else:
        resposta = input("Deseja excluir este evento? [s/n] ").strip().lower()

        if resposta != "s":
            print("\nExclusão cancelada.")
            return

    novos_eventos = []

    for evento in eventos:
        if evento["id"] != evento_id:
            novos_eventos.append(evento)

    escrever_csv(CAMINHO_EVENTOS, CABECALHO_EVENTOS, novos_eventos)
    print("\nEvento excluído com sucesso.")
