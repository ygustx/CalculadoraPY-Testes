#Exercicio 5


import unittest
from calculadora import dividir  # Importe o método que realiza a divisão

class TestDividir(unittest.TestCase):

    def test_dividir_divisor_zero(self):
        # Testando se uma exceção é lançada quando o divisor é zero
        with self.assertRaises(ValueError):  # Verifica se ValueError é levantada
            dividir(10, 0)  # Tentando dividir por zero

if __name__ == '__main__':
    unittest.main()
