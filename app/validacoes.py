from datetime import datetime


def validar_texto_obrigatorio(valor):
    """
    Garante que o campo não seja vazio ou preenchido apenas com espaços.
    Retorna True se for válido, ou False se estiver incorreto.
    """
    if not valor or valor.strip() == "":
        print("❌ Erro: Este campo é obrigatório e não pode ficar em branco. Tente novamente.")
        return False
    return True


def validar_opcao_menu(opcao, opcoes_validas):
    """
    Verifica se a opção digitada pelo usuário está na lista de opções permitidas.
    Retorna True se for válido, ou False se estiver incorreto.
    """
    if opcao not in opcoes_validas:
        print(f"❌ Erro: Opção inválida! Escolha uma opção válida: {', '.join(opcoes_validas)}")
        return False
    return True


def validar_opcao(opcao, opcoes_validas):
    """
    Confere se a opcao digitada esta na lista de opcoes.
    """
    return opcao in opcoes_validas


def validar_data(valor):
    """
    Verifica se a data esta no formato ano-mes-dia.
    """
    try:
        datetime.strptime(valor, "%Y-%m-%d")
        return True
    except:
        return False


def validar_numero_positivo(valor):
    """
    Verifica se o valor é um número positivo.
    Retorna True se for válido, ou False se estiver incorreto.
    """
    try:
        numero = float(valor)
        if numero <= 0:
            print("❌ Erro: O número deve ser positivo. Tente novamente.")
            return False
        return True
    except ValueError:
        print("❌ Erro: Entrada inválida! Por favor, insira um número válido.")
        return False


def formatar_moeda(valor):
    """
    Formata um número como moeda brasileira (R$).
    Exemplo: 1234.56 -> R$ 1.234,56
    """
    try:
        numero = float(valor)
        return f"R$ {numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except ValueError:
        print("❌ Erro: Entrada inválida! Por favor, insira um número válido.")
        return valor
