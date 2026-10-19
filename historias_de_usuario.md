História 1
Descrição: Como monitor, eu quero poder marcar meus horários disponiveis para que os alunos possam reservar para mim poder atende-los.

Justificativa: Prioridade Alta, pois esse é a base do sistema, para os alunso poderem reservar precisa cadastrar os horários.

Trecho: "No início do semestre, cada monitor informa os horários em que pode atender, ..."

Critérios:
1. Dado que o monitor quer cadastrar disponibilidade, quando ele acessa o sistema deve escolher um dia da semana, horário de inicio e fim que estará disponivel.
2. Dado que o monitor selecionou os horários, o sistema deve dividir os horários em blocos de 30 minutos para cumprir a ideia de 30 minutos por atendimento.
3. Dado que o monitor acabe esquecendo de colocar horário em alguma semana, deixando em branco, deve exibir um erro de campo obrigatório e impedir o salvamento.

História 2
Descrição: Como aluno, eu quero poder ver os horários de monitoria que batam com o meu cronograma.

Justificativa: Prioridade alta, esse sistema de verificação de horários permite o aluno de se organizar para receber um atendimento exclusivo.

Trecho:"A ideia é que o aluno escolha a disciplina, veja os horários livres ..."

Critérios:
1. Dado que o aluno pesquisa por uma matéria deve aparecer todos os horários disponiveis daquela disciplina.
2. Dado que o aluno pesquise por uma matéria e não tenha nenhum horário disponivel deve aparecer uma mensagem "Sem horário disponivel." 
3. Dado que o aluno visualiza os resultados da busca e selecione uma matéria, o sistema deve exibir todas as informações necessárias, nome do monitor, dia da semana e hora do atendimento.

História 3
Descrição:Como aluno, eu quero poder reservar horário de antendimento com um monitor.

Justificativa: Prioridade alta, para os alunos poderem reservar os horários que os monitores estão disponiveis, resolvendo o grande problema de desencontro.

Trecho:"... e reserve um atendimento."

Critérios:
1. Dado que o aluno poderá visualizar os blocos de disponibilidade de atendimento, quando ele clicar em reservar o horário selecionado deverá passar para "Reservado" e ser vinculado ao aluno.
2. Dado que o aluno já reservou 3 horários na semana em uma certa disciplina o sistema deve bloquear de fazer mais um reserva naquela disciplina naquela semana e avisar sobre o limite.
3. Dado que dois alunos tentem reservar o mesmo horário simultâneamente, quando o sistema processar as solicitações a reserva vai apenas para o primeiro que o sistema processar.

História 4
Descrição:Como monitor, eu quero poder cancelar um horário caso necessário, para evitar confusão de um aluno reservar um horário e eu não estar na sala.

Justificativa: Prioridade média, resolve um problema citado no e-mail, mas não é tão necessário quanto os sistemas de horários e reservas.

Trecho:"...mas às vezes precisa cancelar por causa de prova. Os alunos reclamam que só descobrem o cancelamento quando chegam na sala."

Critérios: 
1. Dado que o monitor tem um horário cadastrados ele poderá selecionar um bloco e remove-lo clicando em "Remover", o horário deve desaparecer da lista de horários disponives.
2. Dado que o monitor precisa remover um bloco e ele já estiver reservado, o monitor poderá clicar em "Cancelar" logo o atendimento será cancelado, com isso avisando o aluno que a reserva foi cancelada.
3. Dado que o monitor precise remover um horário, o mesmo deve desaparecer imediatamente das buscas, sem a necessidade de atualizar manualmente, evitando uma reserva fantasma.

História 5
Descrição:Como professor, eu quero poder ter acesso quais assuntos/tópicos os alunso estão tendo maior dificuldade na minha matéria.

Justificativa: Prioridade baixa, caso muitos alunos estejam tendo dificuldade no mesmo tópico, posso alterar a forma de ensinar em sala, mas o sistema pode funcionar perfeitamente sem esse relatório.

Trecho:"Os professores das disciplinas gostariam de saber quais conteúdos geram mais 
dúvidas, para reforçar em aula."

Critérios:
1. Dado que o professor acesse o sistema, poderá ter acesso aos relatórios, podendo selecionar qual semana ou mês quer ver relatório.
2. Dado que os alunos/monitores não digitem nada no motivo/tema do agendamento, não se deve computar dados vazios para o relatório do professor.
3. Dado que o relatório do professor é gerado, quando o sistema busca as informações, então ele deve exibir apenas os tópicos de dúvidas e nunca exibir as horas ou os pagamentos de bolsa dos monitores.
