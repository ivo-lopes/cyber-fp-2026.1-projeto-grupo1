from datetime import datetime

from app.armazenamento import ler_csv, escrever_csv


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


def cadastrar_tarefa():
    pass


def listar_tarefas_por_evento(evento_id):
    pass


def editar_tarefa():
    pass


def alterar_status_tarefa():
    pass


def calcular_total_tarefas(evento_id):
    tarefas = ler_csv(CAMINHO_TAREFAS)
    total = 0

    for tarefa in tarefas:
        if tarefa["evento_id"] == str(evento_id):
            custo = tarefa["custo"].strip().replace(",", ".")

            if custo == "":
                custo = "0"

            try:
                total = total + float(custo)
            except:
                pass

    return total


def atualizar_orcamento_evento(evento_id):
    eventos = ler_csv(CAMINHO_EVENTOS)
    encontrou = False

    for evento in eventos:
        if evento["id"] == str(evento_id):
            try:
                orcamento_inicial = float(evento["orcamento_inicial"])
            except:
                orcamento_inicial = 0

            total_tarefas = calcular_total_tarefas(evento_id)
            evento["orcamento_disponivel"] = str(orcamento_inicial - total_tarefas)

            if "atualizado_em" in evento:
                evento["atualizado_em"] = datetime.now().strftime("%Y-%m-%d")

            encontrou = True

    if encontrou:
        escrever_csv(CAMINHO_EVENTOS, CABECALHO_EVENTOS, eventos)


def excluir_tarefa():
    tarefas = ler_csv(CAMINHO_TAREFAS)

    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada.")
        return

    tarefa_id = input("ID da tarefa: ").strip()
    tarefa_encontrada = None

    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa_encontrada = tarefa

    if tarefa_encontrada == None:
        print("\nTarefa não encontrada.")
        return

    resposta = input("Deseja realmente excluir esta tarefa? [s/n] ").strip().lower()

    if resposta != "s":
        print("\nExclusão cancelada.")
        return

    evento_id = tarefa_encontrada["evento_id"]
    novas_tarefas = []

    for tarefa in tarefas:
        if tarefa["id"] != tarefa_id:
            novas_tarefas.append(tarefa)

    escrever_csv(CAMINHO_TAREFAS, CABECALHO_TAREFAS, novas_tarefas)
    atualizar_orcamento_evento(evento_id)
    print("\nTarefa excluída com sucesso.")
