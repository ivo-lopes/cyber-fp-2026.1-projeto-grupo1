# Organiza Festa

Projeto acadêmico feito em Python para a disciplina de Fundamentos da Programação.

O Organiza Festa é um sistema simples de terminal para ajudar na organização de eventos. Ele permite cadastrar eventos, controlar tarefas, acompanhar orçamento, ver sugestões e gerar nomes automáticos.

## Funcionalidades

- Cadastrar, listar, visualizar, editar e excluir eventos.
- Mostrar contagem regressiva para a data do evento.
- Cadastrar, listar, editar, alterar status e excluir tarefas de um evento.
- Recalcular o orçamento disponível com base no custo das tarefas.
- Ver sugestões personalizadas ou uma sugestão genérica.
- Gerar nomes automáticos para eventos.
- Ver um resumo geral de eventos, tarefas e orçamento.

## Melhorias de uso

- O terminal usa cores simples para títulos, avisos e erros.
- No menu principal, `Ctrl+C` encerra o programa.
- Nos submenus e funções, `Ctrl+C` cancela a operação e volta para o menu anterior.
- Algumas perguntas aceitam `0` para cancelar.
- Entradas inválidas mostram mensagens simples e pedem o valor novamente.

## Como executar

```bash
python main.py
```

Se o comando `python` não estiver disponível no computador, use:

```bash
python3 main.py
```

## Estrutura básica

- `main.py`: inicia o sistema.
- `app/menu.py`: mostra os menus principais.
- `app/eventos.py`: funções de eventos.
- `app/tarefas.py`: funções de tarefas e orçamento.
- `app/sugestoes.py`: busca e mostra sugestões.
- `app/gerador_nomes.py`: monta nomes automáticos.
- `app/resumo.py`: mostra um resumo geral do sistema.
- `app/armazenamento.py`: leitura e escrita simples dos CSVs.
- `app/validacoes.py`: validações básicas.
- `app/util.py`: funções auxiliares.
- `data/`: arquivos CSV usados pelo sistema.
- `docs/`: documentação do projeto.

## Observações sobre os CSVs

Os dados ficam salvos na pasta `data`.

O sistema cria os arquivos se eles não existirem ou estiverem vazios. Quando os arquivos já possuem dados, eles são mantidos.

Os campos são separados por `;`. Dentro de campos com listas, o separador usado é `|`.

## Integrantes e responsabilidades

- Ivo: estrutura do projeto, CSV, orçamento, integração e revisão final.
- Jéssica: eventos, visualização, contagem regressiva e gerador de nomes.
- Renata: tarefas, sugestões, testes e README.
