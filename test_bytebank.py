import pytest
from pytest import mark
import sys
sys.path.append(r"C:\Users\jonas\Downloads\Alura\3-Testes unitário e TDD com Python\2622-python-tdd-57de629597dabe71ad125067e9dbedde5babe577")

from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_25(self):
        entrada = '13/03/2000'  # Given
        esperado = 25

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()   # When

        assert resultado == esperado    # Then


    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # Given
        esperado = 90000
        entrada_nome = 'Paulo Bragança'

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()  # When
        resultado = funcionario_teste.salario

        assert resultado == esperado    # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()  # When

        assert resultado == esperado    # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000     # Given
            funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()  # When

            assert resultado    # Then

    '''
    def test_retorno_str(self):
        nome, data_nascimento, salario = ('Teste', '12/03/2000', 1000)  # Given
        esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

        funcionario_teste = Funcionario (nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__()     # When

        assert resultado == esperado  # Then
    '''



