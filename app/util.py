import os


def limpar_tela():
    # Limpa a tela de acordo com o sistema usado.
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
