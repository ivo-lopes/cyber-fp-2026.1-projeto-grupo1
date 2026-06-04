import os


def inicializar_arquivos():
    # Cria a pasta e os arquivos principais do projeto.
    try:
        if not os.path.exists("data"):
            os.mkdir("data")

        arquivos = {
            "data/eventos.csv": "id;nome;tipo;data;local;orcamento_inicial;orcamento_disponivel;num_convidados;criado_em;atualizado_em",
            "data/tarefas.csv": "id;evento_id;descricao;categoria;custo;status;prazo;criado_em;atualizado_em",
            "data/sugestoes.csv": "tipo_evento;min_convidados;max_convidados;fornecedores;decoracao;cardapio;atividades",
            "data/nomes_eventos.csv": "string1;string2;string3",
        }

        for caminho in arquivos:
            if not os.path.exists(caminho):
                arquivo = open(caminho, "w")
                arquivo.write(arquivos[caminho] + "\n")
                arquivo.close()
    except:
        print("Erro ao preparar os arquivos de dados.")


def carregar_dados():
    # Esta funcao vai ser usada depois para carregar os dados.
    return []


def salvar_dados(dados):
    # Esta funcao vai ser usada depois para salvar os dados.
    return dados
