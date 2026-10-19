# Histórias de Usuário - Sistema de Agendamento de Monitorias

## História 1
**Descrição:** Como monitor, eu quero cadastrar meus horários disponíveis para que os alunos possam reservar atendimentos.
**Justificativa:** Prioridade Alta. É a funcionalidade base do sistema; sem a oferta de horários pelos monitores, não há como realizar agendamentos.
**Trecho do E-mail:** "No início do semestre, cada monitor informa os horários em que pode atender..."

**Critérios de Aceitação:**
1. Dado que o monitor acessa o cadastro, quando ele seleciona um dia e horário de início/fim, o sistema deve registrar a disponibilidade.
2. Dado que o monitor selecionou os horários, o sistema deve dividi-los automaticamente em blocos de 30 minutos.
3. Dado que o monitor tente salvar uma disponibilidade sem preencher os campos obrigatórios, o sistema deve exibir uma mensagem de erro e impedir o salvamento.

---

## História 2 (HISTÓRIA ESCOLHIDA PARA IMPLEMENTAÇÃO)
**Descrição:** Como aluno, eu quero visualizar horários livres e reservar um atendimento de 30 minutos na disciplina desejada para garantir meu suporte nos estudos.
**Justificativa:** Prioridade Alta. Esta é a funcionalidade principal do sistema indicada pela coordenação ("Se a reserva de horários funcionar, já ajuda muito").
**Trecho do E-mail:** "A ideia é que o aluno escolha a disciplina, veja os horários livres e reserve um atendimento."

**Critérios de Aceitação:**
1. Dado que o aluno pesquisa por uma disciplina, o sistema deve listar apenas os horários com status livre.
2. Dado que o aluno seleciona um horário vago e confirma a reserva, o sistema deve alterar o status do horário para "Reservado" e vinculá-lo ao aluno.
3. Dado que o aluno tenta reservar um horário que já foi ocupado por outro usuário, o sistema deve recusar o agendamento e lançar uma exceção/mensagem de erro.
4. Dado que o aluno tenta reservar mais de 2 horários na mesma disciplina na mesma semana, o sistema deve bloquear a operação e informar que o limite semanal foi atingido.

---

## História 3
**Descrição:** Como monitor, eu quero poder cancelar um horário de atendimento previamente cadastrado para evitar que alunos compareçam presencialmente sem que eu esteja disponível.
**Justificativa:** Prioridade Média. Resolve o problema de desencontro citado no e-mail, mas depende da existência prévia do cadastro e reserva de horários.
**Trecho do E-mail:** "...mas às vezes precisa cancelar por causa de prova. Os alunos reclamam que só descobrem o cancelamento quando chegam na sala."

**Critérios de Aceitação:**
1. Dado que o monitor possui horários livres cadastrados, ao selecionar um bloco e confirmar a remoção, o horário deve desaparecer da lista pública de buscas.
2. Dado que o monitor cancela um horário que já possui reserva de um aluno, o sistema deve alterar o status para "Cancelado" e disparar a notificação/aviso ao aluno.
3. Dado que um horário é cancelado pelo monitor, qualquer tentativa de reserva posterior por parte de um aluno deve ser bloqueada.

---

## História 4
**Descrição:** Como coordenação, eu quero gerar um relatório mensal restrito com o total de horas atendidas por cada monitor para realizar o pagamento correto das bolsas.
**Justificativa:** Prioridade Média. É essencial para a gestão financeira do curso, porém depende do registro dos atendimentos realizados no sistema.
**Trecho do E-mail:** "A coordenação precisa de um relatório mensal com as horas atendidas por cada monitor, porque isso conta para o pagamento da bolsa. Essas informações de bolsa não podem ficar visíveis para todo mundo."

**Critérios de Aceitação:**
1. Dado que o usuário da coordenação solicita o relatório mensal, o sistema deve somar todas as horas de atendimentos concluídos por cada monitor no mês.
2. Dado que um usuário comum (aluno ou monitor) tente acessar o relatório de bolsas, o sistema deve negar o acesso e exibir mensagem de permissão negada.
3. Dado que o relatório mensal é gerado, ele deve listar o nome do monitor, disciplina e o total de horas contabilizadas.

---

## História 5
**Descrição:** Como professor, eu quero visualizar relatórios dos tópicos e conteúdos que geram mais dúvidas para reforçar esses pontos em sala de aula.
**Justificativa:** Prioridade Baixa. É um recurso analítico útil para o ensino, mas não impede o funcionamento operacional do agendamento de monitorias.
**Trecho do E-mail:** "Os professores das disciplinas gostariam de saber quais conteúdos geram mais dúvidas, para reforçar em aula."

**Critérios de Aceitação:**
1. Dado que o professor acessa a área de relatórios, ele pode filtrar os tópicos de dúvidas cadastrados por disciplina e período.
2. Dado que existam agendamentos sem especificação de tema/dúvida, o sistema não deve computar dados vazios no relatório.
3. Dado que o relatório de conteúdos do professor é exibido, ele não deve conter nenhuma informação sobre valores de bolsa ou horas para pagamento da coordenação.
