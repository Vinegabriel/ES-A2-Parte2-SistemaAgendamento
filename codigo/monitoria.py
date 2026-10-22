class Horario:
    """
    Representa um bloco individual de atendimento de 30 minutos.
    """
    def __init__(self, id_horario, disciplina, monitor, dia_semana, hora_inicio):
        self.id_horario = id_horario
        self.disciplina = disciplina
        self.monitor = monitor
        self.dia_semana = dia_semana
        self.hora_inicio = hora_inicio
        self.status = "Livre"  # Estados possíveis: "Livre", "Reservado" ou "Cancelado"
        self.aluno_reservado = None


class SistemaMonitoria:
    """
    Gerencia como organizar os horários de monitoria, cadastra, lista e reserva.
    """
    def __init__(self):
        self.horarios = []

    def cadastrar_horario(self, id_horario, disciplina, monitor, dia_semana, hora_inicio):
        """
        Cadastra um novo bloco de atendimento no sistema.
        """
        horario = Horario(id_horario, disciplina, monitor, dia_semana, hora_inicio)
        self.horarios.append(horario)
        return horario

    def listar_horarios_livres(self, disciplina):
        """
        Retorna apenas os blocos com status "Livre" pertencentes à disciplina pesquisada.
        """
        return [
            h for h in self.horarios 
            if h.disciplina == disciplina and h.status == "Livre"
        ]

    def reservar_horario(self, id_horario, aluno, disciplina):
        """
        Executa a reserva de um horário para o aluno validando as regras de negócio.
        - Lança ValueError se o horário não existir ou não estiver 'Livre'.
        - Lança ValueError se o aluno já tiver 2 reservas ativas na mesma disciplina.
        """
        # Busca o horário informado
        horario_encontrado = None
        for h in self.horarios:
            if h.id_horario == id_horario:
                horario_encontrado = h
                break

        if not horario_encontrado:
            raise ValueError("Horário não encontrado.")

        # Valida se o horário está com status Livre
        if horario_encontrado.status != "Livre":
            raise ValueError(f"Não é possível reservar um horário com status '{horario_encontrado.status}'.")

        # Conta quantas reservas o aluno já possui na mesma disciplina
        reservas_aluno = sum(
            1 for h in self.horarios 
            if h.disciplina == disciplina 
            and h.aluno_reservado == aluno 
            and h.status == "Reservado"
        )

        # Valida o limite de até 2 reservas por disciplina na semana
        if reservas_aluno >= 2:
            raise ValueError("Limite máximo de 2 reservas semanais por disciplina atingido.")

        # Efetua a reserva
        horario_encontrado.status = "Reservado"
        horario_encontrado.aluno_reservado = aluno
        return True
