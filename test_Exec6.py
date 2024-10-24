#Execercicio 6

import unittest
from calculadora import Singleton  # Importe a classe Singleton

class TestSingleton(unittest.TestCase):

    def test_obterInstanciaUnica(self):
        # Obtendo duas instâncias
        instancia1 = Singleton.obterInstanciaUnica()
        instancia2 = Singleton.obterInstanciaUnica()

        # Verificando se ambas as instâncias são a mesma
        self.assertIs(instancia1, instancia2)  # Ambas devem ser a mesma instância (assertSame no Python é assertIs)

if __name__ == '__main__':
    unittest.main()
