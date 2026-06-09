# Roteiro de apresentação

## 1. Abertura

Apresentar o Organiza Festa como um sistema simples de terminal para organizar eventos.

Explicar que o projeto foi feito em Python para Fundamentos da Programação e usa arquivos CSV para guardar os dados.

## 2. Divisão da equipe

- Ivo: estrutura, CSV, orçamento, integração e revisão final.
- Jéssica: eventos, visualização e gerador de nomes.
- Renata: tarefas, sugestões, testes e README.

## 3. Demonstração do sistema

1. Abrir o sistema com `python main.py`.
2. Mostrar o menu principal.
3. Entrar no menu de eventos.
4. Cadastrar um evento.
5. Listar e visualizar o evento.
6. Mostrar a contagem regressiva.
7. Entrar no menu de tarefas.
8. Cadastrar uma tarefa para o evento.
9. Mostrar o orçamento disponível atualizado.
10. Mostrar sugestões personalizadas.
11. Gerar um nome automático.
12. Sair do sistema.

## 4. Parte técnica

- `main.py` inicia o sistema.
- `app/menu.py` controla os menus.
- `app/eventos.py` trabalha com eventos.
- `app/tarefas.py` trabalha com tarefas e orçamento.
- `app/sugestoes.py` mostra sugestões.
- `app/gerador_nomes.py` gera nomes automáticos.
- `app/armazenamento.py` lê e escreve os CSVs.

## 5. Pontos para comentar

- Os CSVs são criados automaticamente se estiverem vazios ou ausentes.
- Os dados existentes são preservados.
- O orçamento disponível é calculado com base no custo das tarefas.
- A contagem regressiva usa a data do evento.
- A sugestão genérica serve como fallback.

## 6. Fechamento

Encerrar mostrando que o sistema roda pelo terminal, mantém os dados nos CSVs e cobre as funções principais combinadas no roadmap.
