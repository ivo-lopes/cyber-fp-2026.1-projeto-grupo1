from app.armazenamento import ler_csv


CAMINHO_TAREFAS = "data/tarefas.csv"


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
            try:
                total = total + float(tarefa["custo"])
            except:
                pass

    return total


def excluir_tarefa():
    pass
