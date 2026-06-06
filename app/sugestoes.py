import csv

def formatar_lista_sugestoes(valor):
    return valor.split("|")

## Procura uma sugestão no arquivo sugestoes.csv de acordo com o tipo do evento e a quantidade de convidados

def buscar_sugestoes(tipo_evento, num_convidados):

    ## Abre o arquivo CSV para leitura
    ##encoding="utf-8"=>isso serve para dizer ao Python como ler os caracteres do arquivo.
    with open("data/sugestoes.csv", "r", encoding="utf-8") as arquivo:

        ## delimiter=";" => Lê o arquivo considerando ";" como separador
        leitor = csv.DictReader(arquivo, delimiter=";")

        ## Percorre cada linha do arquivo
        for linha in leitor:

            ## Verifica se:
            ## 1. O tipo do evento é o mesmo informado pelo usuário
            ## 2. A quantidade de convidados está dentro da faixa permitida
            if (
                linha["tipo_evento"].lower() == tipo_evento.lower()
                and int(linha["min_convidados"]) <= num_convidados <= int(linha["max_convidados"])
            ):

                ## Retorna a linha encontrada
                return linha

    ## Caso nenhuma sugestão seja encontrada
    return None