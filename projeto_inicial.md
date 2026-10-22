# Projeto Inicial - Sistema de Agendamento de Monitorias

**História Escolhida para Implementação:** História 2 (Prioridade Alta)  
*Como aluno, eu quero visualizar horários livres e reservar um atendimento de 30 minutos na disciplina desejada para garantir meu suporte nos estudos.*

---

## 1. Mapeamento de Classes e Responsabilidades

Para atender à História 2 sem dependência de entradas manuais (`input`) durante a execução dos testes automatizados, a lógica do sistema será encapsulada nas seguintes classes em Python:

### 1. Classe `Horario`
* **Responsabilidade:** Representar a entidade de um bloco individual de atendimento de 30 minutos e manter o seu estado.
* **Atributos:**
  * `id_horario`: Identificador único da vaga.
  * `disciplina`: Nome da matéria (ex: Cálculo, Física, POO, ED).
  * `monitor`: Nome do monitor responsável pelo atendimento.
  * `dia_semana`: Dia da semana do atendimento (ex: "Segunda-feira").
  * `data_atendimento`: Data do atendimento, usada para identificar a semana da reserva.
  * `hora_inicio`: Horário de início do bloco.
  * `status`: Estado atual do bloco ("Livre", "Reservado" ou "Cancelado").
  * `aluno_reservado`: Nome do aluno que realizou a reserva (inicialmente `None`).

### 2. Classe `SistemaMonitoria`
* **Responsabilidade:** Gerenciar o repositório de horários em memória e aplicar todas as regras de negócio de consulta e reserva.
* **Métodos Principais:**
  * `cadastrar_horario(id_horario, disciplina, monitor, dia_semana, hora_inicio, data_atendimento)`: Adiciona um novo bloco disponível ao sistema.
  * `listar_horarios_livres(disciplina)`: Filtra e retorna apenas os blocos que possuem o status "Livre" para a disciplina pesquisada.
  * `reservar_horario(id_horario, aluno, disciplina)`: Valida as regras de negócio antes de confirmar o agendamento:
    1. Verifica se o bloco informado existe e se o seu status está como "Livre".
    2. Contabiliza quantas reservas o mesmo aluno já possui na mesma disciplina e semana ISO, calculada a partir da data do atendimento.
    3. Se o horário estiver livre e o aluno tiver menos de 2 reservas ativas na disciplina, atualiza o status do bloco para "Reservado" e vincula o nome do aluno.
    4. Caso o horário esteja ocupado/cancelado ou o aluno já tenha atingido o limite máximo de 2 reservas semanais na disciplina, lança uma exceção do tipo `ValueError`.

---

## 2. Planejamento dos Testes de Aceitação (`unittest`)

Os testes automatizados serão implementados no arquivo `test_agendamento.py` com a biblioteca nativa `unittest`. Cada um dos 4 critérios de aceitação da História 2 será coberto por pelo menos um método de teste específico:

* **Critério 1 (Listagem de horários livres):**
  * *Método de Teste:* `test_listar_horarios_livres_sucesso`
  * *Verificação:* Garante que a consulta filtre apenas os blocos com status "Livre" pertencentes à disciplina solicitada, ignorando horários reservados ou de outras matérias.

* **Critério 2 (Reserva de horário vago - Cenário de Sucesso):**
  * *Método de Teste:* `test_reservar_horario_sucesso`
  * *Verificação:* Confirma que, ao solicitar a reserva de um bloco disponível, o atributo `status` do objeto `Horario` passa para "Reservado" e o campo `aluno_reservado` recebe o nome do aluno.

* **Critério 3 (Tentativa de reserva de horário ocupado - Cenário de Exceção/Falha):**
  * *Método de Teste:* `test_reservar_horario_ja_ocupado_falha`
  * *Verificação:* Garante que tentar agendar um bloco que já possui status "Reservado" dispara uma exceção `ValueError` e mantém os dados da reserva original inalterados.

* **Critério 4 (Limite semanal de 2 reservas por disciplina - Cenário de Exceção/Falha):**
  * *Método de Teste:* `test_limite_maximo_reservas_semanais_falha`
  * *Verificação:* Garante que o sistema dispara uma exceção `ValueError` quando um aluno que já possui 2 reservas ativas na mesma disciplina e semana tenta efetuar uma 3ª reserva na mesma matéria.
