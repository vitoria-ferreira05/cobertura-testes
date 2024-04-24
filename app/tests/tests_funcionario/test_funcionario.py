from app.funcionario.Funcionario import Funcionario
import pytest


class TestClass:
    def test_quando_idade_recebe_05_06_2000_deve_retornar_24(self):
        # Given-Contexto
        entrada = '05/06/2000'
        esperado = 24

        funcionario_teste = Funcionario('Teste', entrada, 1000)
        resultado = funcionario_teste.idade()  # When-Ação

        assert resultado == esperado  # Then-Desfecho

    def test_quando_sobrenome_recebe_Vitoria_Caroline_deve_retornar_Caroline(self):
        entrada = ' Vitoria Caroline '  # Given
        esperado = 'Caroline'

        lucas = Funcionario(entrada, '05/06/2000', 1000)
        resultado = lucas.sobrenome()  # When

        assert resultado == esperado  # Then
