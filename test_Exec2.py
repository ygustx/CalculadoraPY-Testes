#Exercicio 2
import unittest
from calculadora import ehPar  # Importe o método 'ehPar' do arquivo da calculadora

class TestEhPar(unittest.TestCase):
    
    def test_ehPar(self):
        # Testando a função ehPar
        self.assertTrue(ehPar(2))    # 2 é par
        self.assertTrue(ehPar(0))    # 0 é par
        self.assertTrue(ehPar(-4))   # -4 é par
        self.assertFalse(ehPar(3))   # 3 é ímpar
        self.assertFalse(ehPar(-1))  # -1 é ímpar

if __name__ == '__main__':
    unittest.main()
