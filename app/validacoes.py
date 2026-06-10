from datetime import datetime


def validar_texto_obrigatorio(valor):
    
    if not valor or valor.strip() == "":
        print("Erro: este campo é obrigatório e não pode ficar em branco.")
        return False
    return True


def validar_opcao_menu(opcao, opcoes_validas):
    
    if opcao not in opcoes_validas:
        print("Erro: opção inválida. Escolha uma opção válida:", ", ".join(opcoes_validas))
        return False
    return True


def validar_opcao(opcao, opcoes_validas):
    
    return opcao in opcoes_validas


def validar_data(valor):
    
    try:
        datetime.strptime(valor, "%d/%m/%Y")
        return True
    except:
        return False


def validar_numero_positivo(valor):
   
    try:
        numero = float(valor)
        if numero <= 0:
            print("Erro: o número deve ser positivo.")
            return False
        return True
    except ValueError:
        print("Erro: digite um número válido.")
        return False


def formatar_moeda(valor):
   
    try:
        numero = float(valor)
        return f"R$ {numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except ValueError:
        print("Erro: digite um número válido.")
        return valor


def pedir_opcao(mensagem, opcoes_validas):
    while True:
        valor = input(mensagem).strip().lower()

        if valor in opcoes_validas:
            return valor

        print("Opção inválida. Tente novamente.")


def pedir_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor != "":
            return valor

        print("Este campo não pode ficar em branco.")


def pedir_texto_cancelavel(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor == "0":
            return None

        if valor != "":
            return valor

        print("Este campo não pode ficar em branco.")


def pedir_numero_positivo(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")

        try:
            numero = float(valor)

            if numero > 0:
                return valor

            print("Digite um número maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número.")


def pedir_numero_zero_ou_positivo(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")

        try:
            numero = float(valor)

            if numero >= 0:
                return valor

            print("Digite um número positivo.")
        except ValueError:
            print("Valor inválido. Digite um número.")


def pedir_inteiro_positivo(mensagem):
    while True:
        valor = input(mensagem).strip()

        try:
            numero = int(valor)

            if numero > 0:
                return valor

            print("Digite um número maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def pedir_data(mensagem):
    while True:
        valor = input(mensagem).strip()

        if validar_data(valor):
            return valor

        print("Data inválida. Use o formato DD/MM/AAAA.")


def pedir_data_cancelavel(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor == "0":
            return None

        if validar_data(valor):
            return valor

        print("Data inválida. Use o formato DD/MM/AAAA.")


def pedir_numero_positivo_cancelavel(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")

        if valor == "0":
            return None

        try:
            numero = float(valor)

            if numero > 0:
                return valor

            print("Digite um número maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número.")


def pedir_inteiro_positivo_cancelavel(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor == "0":
            return None

        try:
            numero = int(valor)

            if numero > 0:
                return valor

            print("Digite um número maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
