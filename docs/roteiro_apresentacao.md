# Roteiro técnico de integração

## 1. Execução do sistema

O sistema começa pelo arquivo `main.py`.

Ele chama `inicializar_arquivos()` para preparar os CSVs e depois chama `mostrar_menu()` para abrir o menu principal.

Comando usado:

```bash
python main.py
```

Neste ambiente também foi testado com:

```bash
python3 main.py
```

## 2. Menu principal

O menu principal fica em `app/menu.py`.

Ele leva para:

- gerenciamento de eventos;
- gerenciamento de tarefas;
- sugestões personalizadas;
- gerador de nomes.

Algumas opções de tarefas ainda ficam como pendentes porque pertencem à parte da Renata.

## 3. Eventos

As funções de eventos ficam em `app/eventos.py`.

O cadastro salva o orçamento inicial e o orçamento disponível com o mesmo valor no começo.

A visualização mostra os dados do evento e a contagem regressiva.

## 4. Tarefas e orçamento

As funções revisadas por Ivo ficam em `app/tarefas.py`.

O total das tarefas é calculado somando o custo das tarefas do mesmo evento.

O orçamento disponível segue a regra:

```text
orcamento_disponivel = orcamento_inicial - soma_dos_custos_das_tarefas
```

Quando uma tarefa é excluída, o sistema chama a atualização do orçamento do evento.

## 5. Contagem regressiva

A função `calcular_dias_restantes()` fica em `app/util.py`.

Ela recebe uma data no formato `AAAA-MM-DD` e retorna:

- número positivo para evento futuro;
- zero para evento de hoje;
- número negativo para evento que já passou.

Se a data vier inválida, a função retorna zero para não quebrar o sistema.

## 6. Sugestões

As sugestões ficam em `app/sugestoes.py` e usam `data/sugestoes.csv`.

O sistema tenta buscar uma sugestão específica pelo tipo do evento e número de convidados.

Se não encontrar, usa uma sugestão genérica.

Se mesmo assim não tiver sugestão, mostra uma mensagem simples para o usuário revisar tudo manualmente.

## 7. Gerador de nomes

O gerador fica em `app/gerador_nomes.py`.

Ele lê `data/nomes_eventos.csv`, sorteia uma parte de cada coluna e monta um nome.

Se o arquivo estiver vazio, retorna `Evento Especial`.

## 8. Testes manuais sugeridos

1. Rodar `python main.py`.
2. Abrir o menu de eventos.
3. Cadastrar ou visualizar um evento.
4. Abrir o menu de tarefas.
5. Testar exclusão de tarefa, se existir tarefa cadastrada.
6. Verificar se o orçamento do evento foi recalculado.
7. Abrir sugestões personalizadas.
8. Gerar um nome automático.
9. Sair pelo menu principal.
