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

## 10. Testar resumo geral

Passos:
- Escolher `Ver resumo geral`.

Resultado esperado:
- O sistema mostra quantidade de eventos, tarefas, orçamento total e próximo evento.

## 11. Testar gerador de nomes

Passos:
- Escolher `Gerar nome automático de evento`.

Resultado esperado:
- O sistema mostra um nome formado com dados de `data/nomes_eventos.csv`.

## 11. Testar entradas inválidas

Passos:
- Digitar letras em campos numéricos.
- Deixar campos obrigatórios vazios.
- Digitar data fora do formato `DD/MM/AAAA`.

Resultado esperado:
- O sistema mostra uma mensagem simples e pede o valor novamente.

## 12. Testar cancelamento

Passos:
- Entrar em um submenu e escolher uma função de cadastro, edição ou exclusão.
- Digitar `0` quando a pergunta permitir cancelar.
- Pressionar `Ctrl+C` dentro de um submenu.
- Pressionar `Ctrl+C` no menu principal.

Resultado esperado:
- O `0` cancela a operação quando estiver disponível.
- `Ctrl+C` em submenu volta para o menu principal.
- `Ctrl+C` no menu principal encerra o programa.

## 13. Testar resumo geral

Passos:
- Escolher `Ver resumo geral`.

Resultado esperado:
- O sistema mostra totais de eventos, tarefas, orçamento e próximo evento quando existir.
