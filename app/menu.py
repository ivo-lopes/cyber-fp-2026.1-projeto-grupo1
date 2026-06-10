from app.eventos import cadastrar_evento, editar_evento, excluir_evento, listar_eventos, visualizar_evento
from app.sugestoes import exibir_sugestoes_evento
from app.tarefas import cadastrar_tarefa, listar_tarefas_por_evento, editar_tarefa, alterar_status_tarefa, excluir_tarefa
from app.util import limpar_tela, mostrar_aviso, mostrar_erro, mostrar_titulo
from app.validacoes import validar_opcao
from app.gerador_nomes import gerar_nome_evento


def pausar():
    input("\nPressione Enter para continuar...")


def mostrar_funcionalidade_pendente():
    mostrar_aviso("\nFuncionalidade ainda não implementada.")
    pausar()


def mostrar_menu():
    while True:
        limpar_tela()
        mostrar_titulo("ORGANIZA FESTA")
        print()
        print("1. Gerenciar eventos")
        print("2. Gerenciar tarefas de um evento")
        print("3. Ver sugestões personalizadas")
        print("4. Gerar nome automático de evento")
        print("5. Ver resumo geral")
        print("0. Sair")
        print()

        opcao = input("Escolha uma opção: ").strip()
        limpar_tela()

        if not validar_opcao(opcao, ["0", "1", "2", "3", "4", "5"]):
            mostrar_erro("\nOpção inválida.")
            pausar()
        elif opcao == "0":
            mostrar_aviso("\nSaindo do Organiza Festa...")
            break
        elif opcao == "1":
            mostrar_menu_eventos()
        elif opcao == "2":
            mostrar_menu_tarefas()
        elif opcao == "3":
            exibir_sugestoes_evento()
            pausar()
        elif opcao == "4":
            nome_sugerido = gerar_nome_evento()
            print("Nome sugerido:", nome_sugerido)
            pausar()
        else:
            mostrar_funcionalidade_pendente()
        print()


def mostrar_menu_tarefas():
    while True:
        limpar_tela()
        mostrar_titulo("TAREFAS")
        print()
        print("1. Cadastrar tarefa")
        print("2. Listar tarefas de um evento")
        print("3. Editar tarefa")
        print("4. Alterar status da tarefa")
        print("5. Excluir tarefa")
        print("0. Voltar")
        print()

        opcao = input("Escolha uma opção: ").strip()
        limpar_tela()

        if not validar_opcao(opcao, ["0", "1", "2", "3", "4", "5"]):
            mostrar_erro("\nOpção inválida.")
            pausar()
        elif opcao == "0":
            break
        elif opcao == "1":
            cadastrar_tarefa()
            pausar()
        elif opcao == "2":
            evento_id = input("ID do evento: ").strip()
            listar_tarefas_por_evento(evento_id)
            pausar()
        elif opcao == "3":
            editar_tarefa()
            pausar()
        elif opcao == "4":
            alterar_status_tarefa()
            pausar()
        elif opcao == "5":
            excluir_tarefa()
            pausar()
        print()


def mostrar_menu_eventos():
    while True:
        limpar_tela()
        mostrar_titulo("EVENTOS")
        print()
        print("1. Cadastrar evento")
        print("2. Listar eventos")
        print("3. Visualizar evento")
        print("4. Editar evento")
        print("5. Excluir evento")
        print("0. Voltar")
        print()

        opcao = input("Escolha uma opção: ").strip()
        limpar_tela()

        if not validar_opcao(opcao, ["0", "1", "2", "3", "4", "5"]):
            mostrar_erro("\nOpção inválida.")
            pausar()
        elif opcao == "0":
            break
        elif opcao == "1":
            cadastrar_evento()
            pausar()
        elif opcao == "2":
            listar_eventos()
            pausar()
        elif opcao == "3":
            visualizar_evento()
            pausar()
        elif opcao == "4":
            editar_evento()
            pausar()
        elif opcao == "5":
            excluir_evento()
            pausar()
        print()
