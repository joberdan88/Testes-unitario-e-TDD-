import sys
sys.path.append(r"C:\Users\jonas\Downloads\Alura\3-Testes unitário e TDD com Python\2622-python-tdd-57de629597dabe71ad125067e9dbedde5babe577")

from codigo.bytebank import Funcionario
ana = Funcionario('Ana', '12/03/1997', 100000)

print(ana.calcular_bonus())


