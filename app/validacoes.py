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