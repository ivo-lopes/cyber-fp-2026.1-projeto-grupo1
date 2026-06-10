# Manual do Usuário - Organiza Festa

## 1. O Que É O Organiza Festa

O Organiza Festa é um sistema em Python executado pelo terminal. Ele foi criado para ajudar no planejamento de eventos, permitindo cadastrar eventos, listar eventos cadastrados, visualizar detalhes, controlar informações básicas e gerar nomes automáticos para eventos.

O sistema usa arquivos CSV para armazenar os dados, ou seja, as informações continuam salvas mesmo depois que o programa é encerrado.

## 2. Como Executar O Sistema

Para executar o sistema, abra o terminal na pasta do projeto e digite:

```bash
python main.py
```

Ao iniciar, o sistema prepara automaticamente os arquivos necessários dentro da pasta `data`.

## 3. Menu Principal

Ao executar o programa, o usuário verá o menu principal:

```text
========== ORGANIZA FESTA ==========

1. Gerenciar eventos
2. Gerenciar tarefas de um evento
3. Ver sugestões personalizadas
4. Gerar nome automático de evento
5. Ver resumo geral
0. Sair
```

Digite o número da opção desejada e pressione Enter.

O sistema usa cores simples no terminal para destacar títulos, avisos e mensagens de erro.

Se pressionar `Ctrl+C` no menu principal, o programa será encerrado. Se pressionar `Ctrl+C` dentro de um submenu ou de uma função, a operação será cancelada e o sistema voltará para o menu anterior.

Em algumas perguntas, como ID de evento, ID de tarefa ou confirmação de exclusão, é possível digitar `0` para cancelar.

## 4. Gerenciar Eventos

Ao escolher a opção `1. Gerenciar eventos`, o sistema abre o menu de eventos:

```text
========== EVENTOS ==========

1. Cadastrar evento
2. Listar eventos
3. Visualizar evento
4. Editar evento
5. Excluir evento
0. Voltar
```

Esse menu permite cadastrar, listar, visualizar, editar e excluir eventos.

## 5. Cadastrar Evento

Para cadastrar um evento, escolha a opção `1. Cadastrar evento`.

O sistema perguntará se você deseja gerar um nome automático para o evento:

```text
Deseja gerar um nome automático para o evento? [s/n]
```

Se responder `s`, o sistema mostrará uma sugestão de nome, por exemplo:

```text
Nome sugerido: Festa Memorável de Bons Momentos
```

Depois, será perguntado se você deseja usar esse nome:

```text
Deseja usar esse nome? [s/n]
```

Se responder `s`, o nome sugerido será usado no cadastro.

Se responder `n`, o sistema perguntará se deseja gerar outro nome:

```text
Deseja gerar outro nome? [s/n]
```

Caso não queira gerar outro, você poderá digitar o nome manualmente.

Depois do nome, o sistema solicitará:

- Tipo do evento;
- Data do evento no formato `DD/MM/AAAA`;
- Local do evento;
- Orçamento inicial;
- Número de convidados.

Ao final, o evento será salvo no arquivo `data/eventos.csv`.

## 6. Listar Eventos

Para listar eventos, escolha a opção `2. Listar eventos`.

O sistema exibirá os eventos cadastrados com as principais informações:

- ID;
- Nome;
- Tipo;
- Data;
- Local.

Exemplo:

```text
========== EVENTOS CADASTRADOS ==========
----------------------------------------
ID: 1
Nome: Festa Memorável de Bons Momentos
Tipo: Aniversário
Data: 20/06/2026
Local: Salão Central
----------------------------------------
```

O ID é importante porque será usado para visualizar, editar ou excluir um evento específico.

## 7. Visualizar Evento

Para visualizar os detalhes de um evento, escolha a opção `3. Visualizar evento`.

O sistema mostrará a lista de eventos e pedirá o ID:

```text
Digite o ID do evento que deseja visualizar:
```

Depois disso, serão exibidos os dados completos:

- ID;
- Nome;
- Tipo;
- Data;
- Contagem regressiva;
- Local;
- Orçamento inicial;
- Orçamento disponível;
- Número de convidados;
- Data de criação;
- Data de atualização.

A contagem regressiva pode aparecer de três formas:

```text
Contagem regressiva: Faltam 12 dias para o evento.
```

```text
Contagem regressiva: O evento acontece hoje.
```

```text
Contagem regressiva: Este evento já aconteceu há 3 dias.
```

## 8. Editar Evento

Para editar um evento, escolha a opção `4. Editar evento`.

O sistema pedirá o ID do evento. Depois, mostrará os campos atuais e permitirá alterar as informações.

Se quiser manter um valor, basta deixar o campo em branco e pressionar Enter.

## 9. Excluir Evento

Para excluir um evento, escolha a opção `5. Excluir evento`.

O sistema pedirá o ID do evento e solicitará confirmação antes de excluir.

Se o evento tiver tarefas vinculadas, o sistema avisará e perguntará se deseja excluir também as tarefas relacionadas.

## 10. Gerador Automático De Nomes

O gerador automático de nomes é a funcionalidade extra do projeto.

Ele usa o arquivo `data/nomes_eventos.csv`, que possui três colunas:

```csv
string1;string2;string3
```

O sistema escolhe uma opção de cada coluna e monta o nome final.

Exemplo:

```text
Festa + Memorável + de Bons Momentos

Festa Memorável de Bons Momentos
```

A estrutura escolhida foi:

```text
Substantivo genérico + adjetivo positivo + complemento abstrato
```

Essa regra ajuda a garantir que as combinações façam sentido.

## 11. Gerenciar Tarefas

Para usar tarefas, escolha no menu principal:

```text
2. Gerenciar tarefas de um evento
```

O sistema abre o menu de tarefas:

```text
1. Cadastrar tarefa
2. Listar tarefas de um evento
3. Editar tarefa
4. Alterar status da tarefa
5. Excluir tarefa
0. Voltar
```

As tarefas sempre ficam ligadas a um evento pelo ID do evento.

Ao cadastrar uma tarefa, o sistema pede descrição, categoria, custo e prazo. Depois disso, o orçamento disponível do evento é recalculado.

Ao editar ou excluir uma tarefa, o orçamento também é atualizado.

## 12. Sugestões Personalizadas

Para ver sugestões, escolha no menu principal:

```text
3. Ver sugestões personalizadas
```

O sistema pede o tipo do evento e o número de convidados.

Se encontrar uma sugestão específica no arquivo `data/sugestoes.csv`, ela será exibida. Se não encontrar, o sistema usa a sugestão genérica cadastrada no arquivo.

## 13. Resumo Geral

Para ver o resumo, escolha no menu principal:

```text
5. Ver resumo geral
```

O sistema mostra:

- quantidade de eventos;
- quantidade de tarefas;
- tarefas por status;
- orçamento inicial total;
- orçamento disponível total;
- custo total das tarefas;
- próximo evento futuro, se existir.

## 14. Validações

O sistema possui validações para evitar erros durante o uso.

Alguns exemplos:

- Campos obrigatórios não podem ficar vazios;
- Datas devem seguir o formato `DD/MM/AAAA`;
- Opções de menu precisam existir;
- Orçamento e número de convidados devem ser positivos.

Se o usuário digitar uma informação inválida, o sistema mostra uma mensagem de erro e pede o dado novamente.

## 15. Arquivos De Dados

O sistema usa arquivos CSV dentro da pasta `data`.

Principais arquivos:

- `eventos.csv`: armazena os eventos cadastrados;
- `tarefas.csv`: armazena tarefas vinculadas aos eventos;
- `nomes_eventos.csv`: armazena as partes usadas no gerador de nomes;
- `sugestoes.csv`: armazena sugestões personalizadas por tipo de evento.

## 16. Restrições Conhecidas

- O arquivo de sugestões possui tipos específicos e também uma sugestão genérica para fallback.
- O projeto usa CSV simples com `;` e não usa a biblioteca `csv`.
- O sistema foi feito para ser usado pelo terminal.

## 17. Encerrando O Sistema

Para sair do sistema, volte ao menu principal e escolha:

```text 
0. Sair
```

O programa será encerrado, e os dados continuarão salvos nos arquivos CSV.
