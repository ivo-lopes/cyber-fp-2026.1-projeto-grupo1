# Casos de teste

## 1. Iniciar o sistema

Passos:
- Rodar `python main.py`.
- Verificar se o menu principal aparece.
- Sair com a opção `0`.

Resultado esperado:
- O sistema abre sem erro e encerra normalmente.

## 2. Cadastrar evento

Passos:
- Entrar em `Gerenciar eventos`.
- Escolher `Cadastrar evento`.
- Informar nome, tipo, data, local, orçamento e convidados.

Resultado esperado:
- O evento é salvo em `data/eventos.csv`.

## 3. Editar evento

Passos:
- Entrar em `Gerenciar eventos`.
- Escolher `Editar evento`.
- Informar o ID do evento.
- Alterar algum campo.

Resultado esperado:
- O evento é atualizado no CSV.

## 4. Excluir evento

Passos:
- Entrar em `Gerenciar eventos`.
- Escolher `Excluir evento`.
- Informar o ID do evento.
- Confirmar a exclusão.

Resultado esperado:
- O evento é removido do CSV.

## 5. Cadastrar tarefa

Passos:
- Entrar em `Gerenciar tarefas de um evento`.
- Escolher `Cadastrar tarefa`.
- Informar o ID do evento e os dados da tarefa.

Resultado esperado:
- A tarefa é salva em `data/tarefas.csv`.

## 6. Excluir tarefa

Passos:
- Entrar em `Gerenciar tarefas de um evento`.
- Escolher `Excluir tarefa`.
- Informar o ID da tarefa.
- Confirmar a exclusão.

Resultado esperado:
- A tarefa é removida e o orçamento do evento é atualizado.

## 7. Verificar orçamento

Passos:
- Criar um evento com orçamento inicial.
- Cadastrar uma tarefa com custo.
- Visualizar o evento.

Resultado esperado:
- O orçamento disponível mostra o orçamento inicial menos o custo das tarefas.

## 8. Testar contagem regressiva

Passos:
- Cadastrar um evento com data futura.
- Visualizar o evento.

Resultado esperado:
- O sistema mostra quantos dias faltam para o evento.

## 9. Testar sugestões

Passos:
- Escolher `Ver sugestões personalizadas`.
- Informar tipo do evento e número de convidados.

Resultado esperado:
- O sistema mostra uma sugestão específica ou a sugestão genérica.

## 10. Testar gerador de nomes

Passos:
- Escolher `Gerar nome automático de evento`.

Resultado esperado:
- O sistema mostra um nome formado com dados de `data/nomes_eventos.csv`.
