# Pendências finais

Este relatório foi feito depois da revisão do código, dos CSVs, da documentação e do histórico de commits.

## Partes identificadas no histórico

- Ivo: estrutura inicial, leitura e escrita de CSV, geração de IDs, edição/exclusão de eventos, orçamento, integração dos menus e revisão final.
- Jéssica: eventos, listagem e visualização, contagem regressiva, gerador de nomes e manual do usuário.
- Renata: base de tarefas, cadastro/listagem/edição/status de tarefas, sugestões, testes iniciais e README.

## Pendências de Ivo

- Revisar uma última vez se o orçamento recalcula corretamente depois de cadastrar, editar e excluir tarefas.
- Confirmar se a integração dos menus está funcionando em todos os computadores da equipe.
- Revisar se o código continua simples e sem estruturas avançadas demais.
- Confirmar se o comando `python main.py` funciona no ambiente da apresentação. Neste computador, o comando disponível foi `python3 main.py`.

## Pendências de Jéssica

- Confirmar se cadastro, listagem, visualização, edição e exclusão de eventos estão completos para a apresentação.
- Confirmar se a contagem regressiva aparece corretamente para evento futuro, evento de hoje e evento passado.
- Confirmar se o gerador de nomes está integrado ao cadastro de evento e ao menu principal.
- Confirmar se `data/nomes_eventos.csv` continua com pelo menos 10 opções por coluna.
- Revisar o manual do usuário antes da entrega final.

## Pendências de Renata

- Confirmar se cadastro, listagem, edição, alteração de status e exclusão de tarefas estão completos.
- Confirmar se sugestões personalizadas estão funcionando para tipos específicos quando houver dados no CSV.
- Adicionar ou revisar sugestões específicas em `data/sugestoes.csv`, se a equipe quiser testar além da sugestão genérica.
- Confirmar se o fallback para sugestão genérica está funcionando.
- Revisar os casos de teste e o README antes da entrega final.

## Pendências gerais

- Testar o sistema inteiro pelo terminal antes da apresentação.
- Testar os CSVs depois de criar, editar e excluir registros.
- Revisar o roteiro de apresentação em equipe.
- Validar se todos têm commits relevantes no histórico.
- Conferir se não existe arquivo `__init__.py` rastreado no projeto.
- Conferir se não existe uso de biblioteca externa.
- Fazer merge final para `main` apenas depois dos testes finais.
