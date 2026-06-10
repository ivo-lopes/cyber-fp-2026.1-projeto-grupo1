from app.eventos import cadastrar_evento, editar_evento, excluir_evento, listar_eventos, visualizar_evento
from app.sugestoes import exibir_sugestoes_evento
from app.tarefas import cadastrar_tarefa, listar_tarefas_por_evento, editar_tarefa, alterar_status_tarefa, excluir_tarefa
from app.util import limpar_tela, mostrar_aviso, mostrar_titulo
from app.validacoes import pedir_opcao, pedir_texto_cancelavel
from app.gerador_nomes import gerar_nome_evento


def pausar():
    input("\nPressione Enter para continuar...")


def executar_com_pausa(funcao, mensagem_cancelamento):
    try:
        funcao()
        pausar()
    except KeyboardInterrupt:
        mostrar_aviso("\n" + mensagem_cancelamento)


def mostrar_funcionalidade_pendente():
    mostrar_aviso("\nFuncionalidade ainda não implementada.")
    pausar()


def mostrar_menu():
    while True:
        try:
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

            opcao = pedir_opcao("Escolha uma opção: ", ["0", "1", "2", "3", "4", "5"])
            limpar_tela()

            if opcao == "0":
                mostrar_aviso("\nSaindo do Organiza Festa...")
                break
            elif opcao == "1":
                mostrar_menu_eventos()
            elif opcao == "2":
                mostrar_menu_tarefas()
            elif opcao == "3":
                executar_com_pausa(exibir_sugestoes_evento, "operação cancelada. voltando ao menu anterior.")
            elif opcao == "4":
                nome_sugerido = gerar_nome_evento()
                print("Nome sugerido:", nome_sugerido)
                pausar()
            else:
                mostrar_funcionalidade_pendente()
            print()
        except KeyboardInterrupt:
            mostrar_aviso("\nprograma encerrado.")
            break


def mostrar_menu_tarefas():
    while True:
        try:
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

            opcao = pedir_opcao("Escolha uma opção: ", ["0", "1", "2", "3", "4", "5"])
            limpar_tela()

            if opcao == "0":
                break
            elif opcao == "1":
                executar_com_pausa(cadastrar_tarefa, "cadastro cancelado. voltando ao menu anterior.")
            elif opcao == "2":
                evento_id = pedir_texto_cancelavel("ID do evento ou 0 para cancelar: ")

                if evento_id == None:
                    mostrar_aviso("\nConsulta cancelada.")
                else:
                    listar_tarefas_por_evento(evento_id)

                pausar()
            elif opcao == "3":
                executar_com_pausa(editar_tarefa, "edição cancelada. voltando ao menu anterior.")
            elif opcao == "4":
                executar_com_pausa(alterar_status_tarefa, "alteração cancelada. voltando ao menu anterior.")
            elif opcao == "5":
                executar_com_pausa(excluir_tarefa, "exclusão cancelada. voltando ao menu anterior.")
            print()
        except KeyboardInterrupt:
            mostrar_aviso("\noperação cancelada. voltando ao menu anterior.")
            return


def mostrar_menu_eventos():
    while True:
        try:
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

            opcao = pedir_opcao("Escolha uma opção: ", ["0", "1", "2", "3", "4", "5"])
            limpar_tela()

            if opcao == "0":
                break
            elif opcao == "1":
                executar_com_pausa(cadastrar_evento, "cadastro cancelado. voltando ao menu anterior.")
            elif opcao == "2":
                executar_com_pausa(listar_eventos, "operação cancelada. voltando ao menu anterior.")
            elif opcao == "3":
                executar_com_pausa(visualizar_evento, "consulta cancelada. voltando ao menu anterior.")
            elif opcao == "4":
                executar_com_pausa(editar_evento, "edição cancelada. voltando ao menu anterior.")
            elif opcao == "5":
                executar_com_pausa(excluir_evento, "exclusão cancelada. voltando ao menu anterior.")
            print()
        except KeyboardInterrupt:
            mostrar_aviso("\noperação cancelada. voltando ao menu anterior.")
            return
