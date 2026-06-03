def validar_texto_obrigatorio(valor):
    """
    Garante que o campo não seja vazio ou preenchido apenas com espaços.
    Retorna True se for válido, ou False se estiver incorreto.
    """
    # .strip() remove espaços em branco invisíveis do início e do fim do texto
    if not valor or valor.strip() == "":
        print("❌ Erro: Este campo é obrigatório e não pode ficar em branco. Tente novamente.")
        return False
    return True

def validar_opcao_menu(opcao, opcoes_validas):
    """
    Verifica se a opção digitada pelo usuário está na lista de opções permitidas[cite: 215].
    Retorna True se for válido, ou False se estiver incorreto[cite: 215].
    """
    if opcao not in opcoes_validas:
        print(f"❌ Erro: Opção inválida! Escolha uma opção válida: {', '.join(opcoes_validas)}")
        return False
    return True

##Validação de números positivos
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
##Formatação de moeda
def formatar_moeda(valor):
    """
    Formata um número como moeda brasileira (R$).
    Exemplo: 1234.56 -> R$ 1.234,56
    """
    ##O método replace() é utilizado para substituir um ou mais trechos em uma string.
    try:
        numero = float(valor)
        return f"R$ {numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except ValueError:
        print("❌ Erro: Entrada inválida! Por favor, insira um número válido.")
        return valor