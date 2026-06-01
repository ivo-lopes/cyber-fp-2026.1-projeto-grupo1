from organiza_festa.app.validacoes import validar_texto_obrigatorio, validar_opcao_menu

def cadastrar_evento():
    while True:
        nome = input("Nome do Evento: ").strip()
        if validar_texto_obrigatorio(nome):
            break
            
    while True:
        tipo = input("Tipo do Evento (Aniversário, Casamento, Reunião, etc): ").strip()
        if validar_texto_obrigatorio(tipo):
            break
            
    while True:
        data = input("Data do Evento (DD/MM/AAAA): ").strip()
        # Aqui entrará a função validar_data(data) que o Ivo fará na Fase 2
        if validar_texto_obrigatorio(data): 
            break
            
    while True:
        local = input("Local do Evento: ").strip()
        if validar_texto_obrigatorio(local):
            break
            
    while True:
        orcamento = float(input("Orçamento Inicial (R$): ")).strip()
        # Aqui entrará a função validar_numero_positivo(orcamento) da Renata na Fase 2
        if validar_texto_obrigatorio(orcamento):
            break
            
    while True:
        convidados = int(input("Número de Convidados: ")).strip()
        # Aqui entrará a função validar_inteiro_positivo(convidados) da Renata na Fase 2
        if validar_texto_obrigatorio(convidados):
            break

    novo_evento = {
        "id": "", # O Ivo vai gerar esse ID incremental na Fase 1
        "nome": nome,
        "tipo": tipo,
        "data": data,
        "local": local,
        "orcamento_inicial": orcamento,
        "orcamento_disponivel": orcamento, # Regra de negócio do roadmap
        "num_convidados": convidados,
        "criado_em": "", # O Ivo preenche com a data atual
        "atualizado_em": "" # O Ivo preenche com a data atual
    }
    print(f"\n✔️ Pronto! Os dados de '{nome}' foram validados.")
    return novo_evento

# ESTA LINHA DIZ AO PYTHON PARA EXECUTAR A FUNÇÃO ACIMA:
if __name__ == "__main__":
    cadastrar_evento()
    
