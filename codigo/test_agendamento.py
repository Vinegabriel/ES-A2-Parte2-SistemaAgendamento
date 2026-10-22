import unittest
from datetime import date

from monitoria import SistemaMonitoria


class TestAgendamentoMonitoria(unittest.TestCase):

    def setUp(self):
        """
        Configura um estado inicial limpo do sistema antes de cada teste.
        """
        self.sistema = SistemaMonitoria()
        # Cadastra alguns horários base para os testes
        self.sistema.cadastrar_horario(1, "Cálculo", "Monitor Carlos", "Segunda-feira", "14:00", date(2026, 10, 19))
        self.sistema.cadastrar_horario(2, "Cálculo", "Monitor Carlos", "Segunda-feira", "14:30", date(2026, 10, 19))
        self.sistema.cadastrar_horario(3, "Cálculo", "Monitor Carlos", "Quarta-feira", "10:00", date(2026, 10, 21))
        self.sistema.cadastrar_horario(4, "Física", "Monitora Ana", "Terça-feira", "09:00", date(2026, 10, 20))

    def test_listar_horarios_livres_sucesso(self):
        """
        Critério 1: Garante que a listagem retorne apenas horários livres da disciplina pesquisada.
        """
        # Reserva o horário 1 previamente para garantir que ele seja ignorado na listagem
        self.sistema.reservar_horario(1, "Aluno João", "Cálculo")

        livres_calculo = self.sistema.listar_horarios_livres("Cálculo")

        # Devem restar 2 horários livres para Cálculo (IDs 2 e 3)
        self.assertEqual(len(livres_calculo), 2)
        for h in livres_calculo:
            self.assertEqual(h.status, "Livre")
            self.assertEqual(h.disciplina, "Cálculo")

    def test_reservar_horario_sucesso(self):
        """
        Critério 2: Garante que um horário vago seja reservado com sucesso e vinculado ao aluno.
        """
        resultado = self.sistema.reservar_horario(2, "Aluno Lucas", "Cálculo")
        
        horario_reservado = self.sistema.horarios[1]  # ID 2
        self.assertTrue(resultado)
        self.assertEqual(horario_reservado.status, "Reservado")
        self.assertEqual(horario_reservado.aluno_reservado, "Aluno Lucas")

    def test_reservar_horario_ja_ocupado_falha(self):
        """
        Critério 3: Garante que tentar reservar um horário ocupado lance exceção ValueError.
        """
        # Primeiro aluno reserva o horário 3
        self.sistema.reservar_horario(3, "Aluno Pedro", "Cálculo")

        # Segundo aluno tenta reservar o mesmo horário 3
        with self.assertRaises(ValueError) as contexto:
            self.sistema.reservar_horario(3, "Aluno Maria", "Cálculo")

        self.assertIn("Não é possível reservar um horário com status 'Reservado'", str(contexto.exception))

    def test_limite_maximo_reservas_semanais_falha(self):
        """
        Critério 4: Garante que o sistema impeça a 3ª reserva de um mesmo aluno na mesma disciplina.
        """
        # Aluno faz 2 reservas permitidas em Cálculo
        self.sistema.reservar_horario(1, "Aluno Mateus", "Cálculo")
        self.sistema.reservar_horario(2, "Aluno Mateus", "Cálculo")

        # Aluno tenta fazer a 3ª reserva em Cálculo (ID 3)
        with self.assertRaises(ValueError) as contexto:
            self.sistema.reservar_horario(3, "Aluno Mateus", "Cálculo")

        self.assertIn("Limite máximo de 2 reservas semanais por disciplina atingido", str(contexto.exception))

    def test_limite_semanal_nao_bloqueia_reserva_em_outra_semana(self):
        """
        Garante que reservas de semanas diferentes não sejam somadas para o limite semanal.
        """
        self.sistema.cadastrar_horario(5, "Cálculo", "Monitor Carlos", "Segunda-feira", "14:00", date(2026, 10, 26))
        self.sistema.reservar_horario(1, "Aluno Mateus", "Cálculo")
        self.sistema.reservar_horario(2, "Aluno Mateus", "Cálculo")

        resultado = self.sistema.reservar_horario(5, "Aluno Mateus", "Cálculo")

        self.assertTrue(resultado)
        self.assertEqual(self.sistema.horarios[4].status, "Reservado")
        self.assertEqual(self.sistema.horarios[4].aluno_reservado, "Aluno Mateus")

    def test_reservar_horario_de_outra_disciplina_falha(self):
        """
        Garante que a disciplina informada corresponda à disciplina do horário.
        """
        self.sistema.reservar_horario(1, "Aluno Ana", "Cálculo")
        self.sistema.reservar_horario(2, "Aluno Ana", "Cálculo")

        with self.assertRaisesRegex(ValueError, "não pertence à disciplina informada"):
            self.sistema.reservar_horario(3, "Aluno Ana", "Física")

        with self.assertRaisesRegex(ValueError, "não pertence à disciplina informada"):
            self.sistema.reservar_horario(4, "Aluno Ana", "Cálculo")

        self.assertEqual(self.sistema.horarios[2].status, "Livre")
        self.assertEqual(self.sistema.horarios[3].status, "Livre")


if __name__ == "__main__":
    unittest.main()
