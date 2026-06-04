from app.validacoes import validar_opcao


def mostrar_titulo():
    print("========== ORGANIZA FESTA ==========")
    print()


def mostrar_opcoes():
    print("1. Gerenciar eventos")
    print("2. Gerenciar tarefas de um evento")
    print("3. Ver sugestões personalizadas")
    print("4. Gerar nome automático de evento")
    print("5. Ver resumo geral")
    print("0. Sair")
    print()


def pausar():
    input("\nPressione Enter para continuar...")


def mostrar_funcionalidade_pendente():
    print("\nFuncionalidade ainda não implementada.")
    pausar()


def mostrar_menu():
    opcoes_validas = ["0", "1", "2", "3", "4", "5"]

    while True:
        mostrar_titulo()
        mostrar_opcoes()

        opcao = input("Escolha uma opção: ").strip()

        if not validar_opcao(opcao, opcoes_validas):
            print("\nOpção inválida.")
            pausar()
        elif opcao == "0":
            print("\nSaindo do Organiza Festa...")
            break
        else:
            mostrar_funcionalidade_pendente()
        print()
