from datetime import datetime

from app.armazenamento import ler_csv, escrever_csv, obter_proximo_id
from app.validacoes import (
    validar_data,
    formatar_moeda,
    pedir_data_cancelavel,
    pedir_inteiro_positivo_cancelavel,
    pedir_numero_positivo_cancelavel,
    pedir_opcao,
    pedir_texto_cancelavel,
)
from app.gerador_nomes import gerar_nome_evento
from app.util import calcular_dias_restantes


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
    while True:
        resposta = pedir_opcao("Deseja gerar um nome automático para o evento? [s/n] ou 0 para cancelar: ", ["s", "n", "0"])

        if resposta == "0":
            print("\nCadastro cancelado.")
            return

        if resposta == "s":
            while True:
                nome_sugerido = gerar_nome_evento()
                print("Nome sugerido:", nome_sugerido)

                usar_nome = pedir_opcao("Deseja usar esse nome? [s/n] ou 0 para cancelar: ", ["s", "n", "0"])

                if usar_nome == "0":
                    print("\nCadastro cancelado.")
                    return

                if usar_nome == "s":
                    nome = nome_sugerido
                    break

                gerar_outro = pedir_opcao("Deseja gerar outro nome? [s/n] ou 0 para cancelar: ", ["s", "n", "0"])

                if gerar_outro == "0":
                    print("\nCadastro cancelado.")
                    return

                if gerar_outro != "s":
                    nome = pedir_texto_cancelavel("Nome do Evento ou 0 para cancelar: ")

                    if nome == None:
                        print("\nCadastro cancelado.")
                        return

                    break

            break

        elif resposta == "n":
            nome = pedir_texto_cancelavel("Nome do Evento ou 0 para cancelar: ")

            if nome == None:
                print("\nCadastro cancelado.")
                return

            break

    tipo = pedir_texto_cancelavel("Tipo do Evento (Aniversário, Casamento, Reunião, etc) ou 0 para cancelar: ")

    if tipo == None:
        print("\nCadastro cancelado.")
        return

    data = pedir_data_cancelavel("Data do Evento (DD/MM/AAAA) ou 0 para cancelar: ")

    if data == None:
        print("\nCadastro cancelado.")
        return

    local = pedir_texto_cancelavel("Local do Evento ou 0 para cancelar: ")

    if local == None:
        print("\nCadastro cancelado.")
        return

    orcamento = pedir_numero_positivo_cancelavel("Orçamento Inicial (R$) ou 0 para cancelar: ")

    if orcamento == None:
        print("\nCadastro cancelado.")
        return

    convidados = pedir_inteiro_positivo_cancelavel("Número de Convidados ou 0 para cancelar: ")

    if convidados == None:
        print("\nCadastro cancelado.")
        return

    eventos = ler_csv(CAMINHO_EVENTOS)
    data_atual = datetime.now().strftime("%d/%m/%Y")

    novo_evento = {
        "id": str(obter_proximo_id(eventos)),
        "nome": nome,
        "tipo": tipo,
        "data": data,
        "local": local,
        "orcamento_inicial": orcamento,
        "orcamento_disponivel": orcamento,
        "num_convidados": convidados,
        "criado_em": data_atual,
        "atualizado_em": data_atual,
    }

    eventos.append(novo_evento)
    escrever_csv(CAMINHO_EVENTOS, CABECALHO_EVENTOS, eventos)
    print(f"\nPronto! Os dados de '{nome}' foram validados e cadastrados.")
    return novo_evento


def listar_eventos():
    eventos = ler_csv(CAMINHO_EVENTOS)

    if len(eventos) == 0:
        print("\nNenhum evento cadastrado.")
        return

    print("\n========== EVENTOS CADASTRADOS ==========")

    for evento in eventos:
        print("----------------------------------------")
        print("ID:", evento["id"])
        print("Nome:", evento["nome"])
        print("Tipo:", evento["tipo"])
        print("Data:", evento["data"])
        print("Local:", evento["local"])

    print("----------------------------------------")


def visualizar_evento():
    eventos = ler_csv(CAMINHO_EVENTOS)

    if len(eventos) == 0:
        print("\nNenhum evento cadastrado.")
        return

    listar_eventos()

    evento_id = pedir_texto_cancelavel("\nDigite o ID do evento que deseja visualizar ou 0 para cancelar: ")

    if evento_id == None:
        print("\nConsulta cancelada.")
        return

    evento = buscar_evento_por_id(evento_id)

    if evento == None:
        print("\nEvento não encontrado.")
        return

    print("\n========== DETALHES DO EVENTO ==========")
    print("ID:", evento["id"])
    print("Nome:", evento["nome"])
    print("Tipo:", evento["tipo"])
    print("Data:", evento["data"])

    dias_restantes = calcular_dias_restantes(evento["data"])

    if dias_restantes > 0:
        print("Contagem regressiva: Faltam", dias_restantes, "dias para o evento.")
    elif dias_restantes == 0:
        print("Contagem regressiva: O evento acontece hoje.")
    else:
        print("Contagem regressiva: Este evento já aconteceu há", abs(dias_restantes), "dias.")

    print("Local:", evento["local"])
    print("Orçamento inicial:", formatar_moeda(evento["orcamento_inicial"]))
    print("Orçamento disponível:", formatar_moeda(evento["orcamento_disponivel"]))
    print("Número de convidados:", evento["num_convidados"])
    print("Criado em:", evento["criado_em"])
    print("Atualizado em:", evento["atualizado_em"])


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

        print("Data inválida. Use o formato DD/MM/AAAA.")


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

    evento_id = pedir_texto_cancelavel("ID do evento ou 0 para cancelar: ")

    if evento_id == None:
        print("\nEdição cancelada.")
        return

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
    evento_encontrado["atualizado_em"] = datetime.now().strftime("%d/%m/%Y")

    escrever_csv(CAMINHO_EVENTOS, CABECALHO_EVENTOS, eventos)
    from app.tarefas import atualizar_orcamento_evento

    atualizar_orcamento_evento(evento_id)
    print("\nEvento atualizado com sucesso.")


def excluir_evento():
    eventos = ler_csv(CAMINHO_EVENTOS)

    if len(eventos) == 0:
        print("\nNenhum evento cadastrado.")
        return

    evento_id = pedir_texto_cancelavel("ID do evento ou 0 para cancelar: ")

    if evento_id == None:
        print("\nExclusão cancelada.")
        return

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
        resposta = pedir_opcao("Deseja excluir o evento e todas as tarefas vinculadas? [s/n] ou 0 para cancelar: ", ["s", "n", "0"])

        if resposta != "s":
            print("\nExclusão cancelada.")
            return

        novas_tarefas = []

        for tarefa in tarefas:
            if tarefa["evento_id"] != evento_id:
                novas_tarefas.append(tarefa)

        escrever_csv(CAMINHO_TAREFAS, CABECALHO_TAREFAS, novas_tarefas)
    else:
        resposta = pedir_opcao("Deseja excluir este evento? [s/n] ou 0 para cancelar: ", ["s", "n", "0"])

        if resposta != "s":
            print("\nExclusão cancelada.")
            return

    novos_eventos = []

    for evento in eventos:
        if evento["id"] != evento_id:
            novos_eventos.append(evento)

    escrever_csv(CAMINHO_EVENTOS, CABECALHO_EVENTOS, novos_eventos)
    print("\nEvento excluído com sucesso.")
