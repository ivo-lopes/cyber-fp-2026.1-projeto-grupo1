from app.eventos import cadastrar_evento, editar_evento, excluir_evento, listar_eventos, visualizar_evento
from app.util import limpar_tela
from app.validacoes import validar_opcao
from app.gerador_nomes import gerar_nome_evento


def pausar():
    input("\nPressione Enter para continuar...")


def mostrar_funcionalidade_pendente():
    print("\nFuncionalidade ainda não implementada.")
    pausar()


def mostrar_menu():
    while True:
        limpar_tela()
        print("========== ORGANIZA FESTA ==========")
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
            print("\nOpção inválida.")
            pausar()
        elif opcao == "0":
            print("\nSaindo do Organiza Festa...")
            break
        elif opcao == "1":
            mostrar_menu_eventos()
        elif opcao == "4":
            nome_sugerido = gerar_nome_evento()
            print("Nome sugerido:", nome_sugerido)
            pausar()
        else:
            mostrar_funcionalidade_pendente()
        print()


def mostrar_menu_eventos():
    while True:
        limpar_tela()
        print("========== EVENTOS ==========")
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
            print("\nOpção inválida.")
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
