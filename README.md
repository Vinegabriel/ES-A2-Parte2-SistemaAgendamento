# Relatório de Execução (README)

## 1. Instruções para Execução do Sistema e Testes
- **Linguagem / Versão:** Python 3.15 ou superior, sem dependências de bibliotecas externas.
- **Arquivos Feitos:** `monitoria.py` (contém a lógica de negócio) e `test_agendamento.py` (contém os testes de aceitação).
- **Estrutura dos Arquivos:** Todos os arquivos de código-fonte estão localizados no diretório `codigo/`. Abra o terminal na raiz desta pasta.
- **Comando para execução dos testes automatizados:**
  ```bash
  python -m unittest test_agendamento.py
  ```

## 2. Comparação: Plano vs Realizado
- **16/10 - Análise e Plano:** Feito e entregue em sala. Feito por Vinicius e Felipe.
- **17/10 - Repositório e Histórias de Usuário:** Adiado para o dia 18 para todos os contribuintes participarem do planejamento das histórias de usuário. Feito por Vinicius e Felipe.
- **19/10 - Projeto Inicial, Implementação e Testes:** Elaboração do Projeto Inicial focado na história 2 e desenvolvimento do código-fonte. Devido à dispensa da aula do dia 19, adiantamos o que estava previsto para o dia 20, implementando os testes. Feito por Vinicius e Felipe.
- **21/10 - Relatório e Documentação:** Feito o relatório de execução e compilação da documentação PDF. Feito por Vinicius e Felipe.
- **22/10 - Autoavaliação, Ajustes Finais e Entrega:** O planejamento de autoavaliação final, extração do `.zip` em pasta limpa e entrega oficial no Moodle mantêm-se previstos para o prazo final. Feito por Vinicius e Felipe.
  
## 3. Atrasos e Mudanças em Relação ao Projeto Inicial
- **Atrasos:** Não ocorreu nenhum atraso durante o desenvolvimento da Atividade Avaliativa, na verdade conseguimos adiantar um dia de desenvolvimento. 
- **Mudanças na Arquitetura:** O desenvolvimento seguiu o planejamento inicial. A única adaptação menor ocorreu na construção dos testes de aceitação, onde optamos por fazer a configuração inicial do estado do sistema em um método `setUp()` cadastrando 4 horários base antes de cada teste para evitar a repetição de código em cada critério validado, mantendo as funções limpas e isoladas.
