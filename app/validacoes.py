from datetime import datetime


def validar_texto_obrigatorio(valor):
    
    if not valor or valor.strip() == "":
        print("Este campo é obrigatório e não pode ficar em branco. Tente novamente.")
        return False
    return True


def validar_opcao_menu(opcao, opcoes_validas):
    
    if opcao not in opcoes_validas:
        print(f"Opção inválida! Escolha uma opção válida: {', '.join(opcoes_validas)}")
        return False
    return True


def validar_opcao(opcao, opcoes_validas):
    
    return opcao in opcoes_validas


def validar_data(valor):
    
    try:
        datetime.strptime(valor, "%Y-%m-%d")
        return True
    except:
        return False


def validar_numero_positivo(valor):
   
    try:
        numero = float(valor)
        if numero <= 0:
            print("O número deve ser positivo. Tente novamente.")
            return False
        return True
    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido.")
        return False


def formatar_moeda(valor):
   
    try:
        numero = float(valor)
        return f"R$ {numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido.")
        return valor
