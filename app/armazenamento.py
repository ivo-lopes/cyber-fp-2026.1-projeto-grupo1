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
            if not os.path.exists(caminho) or os.path.getsize(caminho) == 0:
                arquivo = open(caminho, "w", encoding="utf-8")
                arquivo.write(arquivos[caminho] + "\n")
                arquivo.close()
    except:
        print("Erro ao preparar os arquivos de dados.")


def ler_csv(caminho):
    # Le o arquivo e transforma cada linha em um dicionario simples.
    registros = []

    try:
        if not os.path.exists(caminho):
            return registros

        arquivo = open(caminho, "r", encoding="utf-8")
        linhas = arquivo.readlines()
        arquivo.close()

        if len(linhas) == 0:
            return registros

        cabecalho = linhas[0].strip().split(";")

        for i in range(1, len(linhas)):
            linha = linhas[i].strip()

            if linha != "":
                valores = linha.split(";")
                registro = {}

                for j in range(len(cabecalho)):
                    if j < len(valores):
                        registro[cabecalho[j]] = valores[j]
                    else:
                        registro[cabecalho[j]] = ""

                registros.append(registro)
    except:
        print("Erro ao ler o arquivo.")

    return registros


def escrever_csv(caminho, cabecalho, registros):
    # Escreve o cabecalho e depois grava os registros no arquivo.
    try:
        arquivo = open(caminho, "w", encoding="utf-8")
        arquivo.write(";".join(cabecalho) + "\n")

        for registro in registros:
            valores = []

            for campo in cabecalho:
                if campo in registro:
                    valores.append(str(registro[campo]))
                else:
                    valores.append("")

            arquivo.write(";".join(valores) + "\n")

        arquivo.close()
    except:
        print("Erro ao escrever no arquivo.")


def obter_proximo_id(registros):
    # Procura o maior id ja usado e soma 1.
    maior_id = 0

    for registro in registros:
        if "id" in registro:
            try:
                id_atual = int(registro["id"])

                if id_atual > maior_id:
                    maior_id = id_atual
            except:
                pass

    return maior_id + 1


def carregar_dados():
    # Esta funcao vai ser usada depois para carregar os dados.
    return []


def salvar_dados(dados):
    # Esta funcao vai ser usada depois para salvar os dados.
    return dados
