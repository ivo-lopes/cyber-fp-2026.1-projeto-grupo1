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
    tarefas = ler_csv(CAMINHO_TAREFAS)
    eventos = ler_csv(CAMINHO_EVENTOS)

    evento_id = input("ID do evento: ").strip()
    evento_encontrado = False

    for evento in eventos:
        if evento["id"] == evento_id:
            evento_encontrado = True

    if not evento_encontrado:
        print("\nEvento não encontrado. Cadastre a tarefa em um evento existente.")
        return

    descricao = input("Descrição da tarefa: ").strip()
    categoria = input("Categoria da tarefa: ").strip()

    if descricao == "" or categoria == "":
        print("\nDescrição e categoria são obrigatórias.")
        return

    custo_digitado = input("Custo da tarefa: R$ ").strip().replace(",", ".")

    try:
        custo = float(custo_digitado)
        if custo < 0:
            print("\nO custo não pode ser negativo.")
            return
    except:
        print("\nDigite um número válido para o custo.")
        return

    prazo = input("Prazo da tarefa (AAAA-MM-DD): ").strip()

    try:
        datetime.strptime(prazo, "%Y-%m-%d")
    except:
        print("\nData inválida. Use o formato AAAA-MM-DD.")
        return

    maior_id = 0

    for tarefa in tarefas:
        try:
            tarefa_id = int(tarefa["id"])
            if tarefa_id > maior_id:
                maior_id = tarefa_id
        except:
            pass

    agora = datetime.now().strftime("%Y-%m-%d")
    nova_tarefa = {
        "id": str(maior_id + 1),
        "evento_id": str(evento_id),
        "descricao": descricao,
        "categoria": categoria,
        "custo": str(custo),
        "status": "pendente",
        "prazo": prazo,
        "criado_em": agora,
        "atualizado_em": agora,
    }

    tarefas.append(nova_tarefa)
    escrever_csv(CAMINHO_TAREFAS, CABECALHO_TAREFAS, tarefas)
    atualizar_orcamento_evento(evento_id)
    print("\nTarefa cadastrada com sucesso.")




def listar_tarefas_por_evento(evento_id):
    tarefas = ler_csv(CAMINHO_TAREFAS)
    encontrou = False

    print("\n========== TAREFAS DO EVENTO ==========")

    for tarefa in tarefas:
        if tarefa["evento_id"] == str(evento_id):
            encontrou = True
            print(f"ID: {tarefa['id']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Categoria: {tarefa['categoria']}")
            print(f"Custo: R$ {tarefa['custo']}")
            print(f"Status: {tarefa['status']}")
            print(f"Prazo: {tarefa['prazo']}")
            print("---------------------------------------")

    if not encontrou:
        print("Nenhuma tarefa cadastrada para este evento.")


def editar_tarefa():
    tarefas = ler_csv(CAMINHO_TAREFAS)

    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada.")
        return

    tarefa_id = input("ID da tarefa que deseja editar: ").strip()
    tarefa_encontrada = None

    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa_encontrada = tarefa

    if tarefa_encontrada == None:
        print("\nTarefa não encontrada.")
        return

    print("\nDeixe em branco para manter o valor atual.")

    nova_descricao = input(f"Descrição ({tarefa_encontrada['descricao']}): ").strip()
    nova_categoria = input(f"Categoria ({tarefa_encontrada['categoria']}): ").strip()
    novo_custo = input(f"Custo ({tarefa_encontrada['custo']}): R$ ").strip().replace(",", ".")
    novo_prazo = input(f"Prazo ({tarefa_encontrada['prazo']}): ").strip()

    if nova_descricao != "":
        tarefa_encontrada["descricao"] = nova_descricao

    if nova_categoria != "":
        tarefa_encontrada["categoria"] = nova_categoria

    if novo_custo != "":
        try:
            custo = float(novo_custo)
            if custo < 0:
                print("\nO custo não pode ser negativo.")
                return
            tarefa_encontrada["custo"] = str(custo)
        except:
            print("\nDigite um número válido para o custo.")
            return

    if novo_prazo != "":
        try:
            datetime.strptime(novo_prazo, "%Y-%m-%d")
        except:
            print("\nData inválida. Use o formato AAAA-MM-DD.")
            return
        tarefa_encontrada["prazo"] = novo_prazo

    tarefa_encontrada["atualizado_em"] = datetime.now().strftime("%Y-%m-%d")
    escrever_csv(CAMINHO_TAREFAS, CABECALHO_TAREFAS, tarefas)
    atualizar_orcamento_evento(tarefa_encontrada["evento_id"])
    print("\nTarefa editada com sucesso.")


def alterar_status_tarefa():
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

    print("\nStatus disponíveis:")
    print("1. Pendente")
    print("2. Em andamento")
    print("3. Concluída")

    opcao = input("Escolha o novo status: ").strip()

    if opcao == "1":
        novo_status = "pendente"
    elif opcao == "2":
        novo_status = "em andamento"
    elif opcao == "3":
        novo_status = "concluída"
    else:
        print("\nOpção inválida.")
        return

    tarefa_encontrada["status"] = novo_status
    tarefa_encontrada["atualizado_em"] = datetime.now().strftime("%Y-%m-%d")
    escrever_csv(CAMINHO_TAREFAS, CABECALHO_TAREFAS, tarefas)
    print("\nStatus alterado com sucesso.")



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
            orcamento = evento["orcamento_inicial"].strip().replace(",", ".")

            if orcamento == "":
                orcamento = "0"

            try:
                orcamento_inicial = float(orcamento)
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

    if tarefa_id == "":
        print("\nInforme o ID da tarefa.")
        return

    tarefa_encontrada = None

    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa_encontrada = tarefa
            break

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
