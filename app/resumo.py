from datetime import datetime

from app.armazenamento import ler_csv
from app.validacoes import formatar_moeda


CAMINHO_EVENTOS = "data/eventos.csv"
CAMINHO_TAREFAS = "data/tarefas.csv"


def transformar_numero(valor):
    try:
        return float(valor.strip().replace(",", "."))
    except:
        return 0


def buscar_proximo_evento(eventos):
    proximo_evento = None
    menor_data = None
    hoje = datetime.now().date()

    for evento in eventos:
        try:
            data_evento = datetime.strptime(evento["data"], "%Y-%m-%d").date()
        except:
            data_evento = None

        if data_evento != None and data_evento >= hoje:
            if menor_data == None or data_evento < menor_data:
                menor_data = data_evento
                proximo_evento = evento

    return proximo_evento


def exibir_resumo_geral():
    eventos = ler_csv(CAMINHO_EVENTOS)
    tarefas = ler_csv(CAMINHO_TAREFAS)

    total_orcamento_inicial = 0
    total_orcamento_disponivel = 0
    total_custos_tarefas = 0
    tarefas_pendentes = 0
    tarefas_andamento = 0
    tarefas_concluidas = 0

    for evento in eventos:
        total_orcamento_inicial = total_orcamento_inicial + transformar_numero(evento["orcamento_inicial"])
        total_orcamento_disponivel = total_orcamento_disponivel + transformar_numero(evento["orcamento_disponivel"])

    for tarefa in tarefas:
        total_custos_tarefas = total_custos_tarefas + transformar_numero(tarefa["custo"])
        status = tarefa["status"].strip().lower()

        if status == "pendente":
            tarefas_pendentes = tarefas_pendentes + 1
        elif status == "em andamento":
            tarefas_andamento = tarefas_andamento + 1
        elif status == "concluída" or status == "concluida":
            tarefas_concluidas = tarefas_concluidas + 1

    proximo_evento = buscar_proximo_evento(eventos)

    print("========== RESUMO GERAL ==========")
    print()
    print("Eventos cadastrados:", len(eventos))
    print("Tarefas cadastradas:", len(tarefas))
    print("Tarefas pendentes:", tarefas_pendentes)
    print("Tarefas em andamento:", tarefas_andamento)
    print("Tarefas concluídas:", tarefas_concluidas)
    print()
    print("Orçamento inicial total:", formatar_moeda(total_orcamento_inicial))
    print("Orçamento disponível total:", formatar_moeda(total_orcamento_disponivel))
    print("Custo total das tarefas:", formatar_moeda(total_custos_tarefas))
    print()

    if proximo_evento == None:
        print("Próximo evento: nenhum evento futuro cadastrado.")
    else:
        print("Próximo evento:", proximo_evento["nome"])
        print("Data:", proximo_evento["data"])
        print("Local:", proximo_evento["local"])
