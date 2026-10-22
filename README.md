# Relatório de Execução - Sistema de Agendamento de Monitorias

Este arquivo serve como o Relatório de Execução (Seção 2 da documentação técnica) detalhando as instruções de uso do protótipo, a comparação do planejamento e as justificativas do desenvolvimento.

## 1. Instruções para Execução do Sistema e Testes

*   **Versão do Python:** Python 3.x (recomendado 3.10 ou superior).
*   **Bibliotecas Necessárias:** Não é necessária a instalação de bibliotecas externas. O protótipo utiliza apenas a biblioteca nativa `unittest`.
*   **Arquivos da Aplicação:** `monitoria.py` (contém a lógica de negócio) e `test_agendamentos.py` (contém os testes de aceitação).
*   **Como executar os testes:** Abra o terminal na raiz da pasta `codigo/` e execute o seguinte comando:
    ```bash
    python -m unittest test_agendamentos.py
    ```
    *(O sistema executará a suíte de testes automaticamente e apresentará o resultado no console).*

## 2. Comparação: Plano vs. Realizado

Abaixo encontra-se o registro da execução das tarefas em comparação com o planejamento original (Parte 1):

*   **16/10 (Planejado e Realizado):** Análise do problema, definição da solução e entrega do PDF da Parte 1. *(Realizado por: Vinicius e Felipe)*.
*   **17/10 (Planejado e Realizado):** Criação do repositório no GitHub e escrita das Histórias de Usuário com os respectivos critérios. *(Realizado por: Vinicius e Felipe)*.
*   **19/10 (Realizado com Adiantamento):** Elaboração do Projeto Inicial focando na História 2 *(Realizado por: Vinicius)* e desenvolvimento do código-fonte `monitoria.py` *(Realizado por: Felipe)*. 
    *   **Nota de adiantamento:** Devido à boa fluidez na estruturação do código, adiantamos as tarefas planejadas para os dias 20/10 e 21/10. Implementamos e executamos os testes de aceitação (`test_agendamentos.py`) e redigimos este relatório de execução nesta mesma data. *(Realizado por: Vinicius e Felipe)*.
*   **22/10 (A Realizar):** O planejamento de autoavaliação final, extração do `.zip` em pasta limpa e entrega oficial no Moodle mantêm-se previstos para o prazo final. *(A realizar por: Vinicius e Felipe)*.

## 3. Mudanças, Atrasos e Justificativas

*   **Atrasos:** Não ocorreu nenhum atraso durante o desenvolvimento. Pelo contrário, a dupla conseguiu concluir a implementação, os testes e a documentação antes da data limite estipulada no plano original.
*   **Mudanças no Projeto Inicial:** O desenvolvimento seguiu fielmente a arquitetura desenhada no Projeto Inicial (classes `Horario` e `SistemaMonitoria`). A única adaptação menor ocorreu na construção dos testes de aceitação, onde optamos por consolidar a configuração inicial do estado do sistema em um método `setUp()` (cadastrando 4 horários base antes de cada teste) para evitar a repetição de código em cada critério validado, mantendo as funções limpas e isoladas.