# Exercício 1

import unittest
from calculadora import somar  # Importe o método 'somar' do arquivo da calculadora

class TestCalculadora(unittest.TestCase):
    
    def test_somar(self):
        # Testando a função somar com vários casos
        self.assertEqual(somar(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(somar(-1, 1), 0)  # -1 + 1 = 0
        self.assertEqual(somar(0, 0), 0)  # 0 + 0 = 0
        self.assertEqual(somar(-5, -3), -8)  # -5 + (-3) = -8
        self.assertEqual(somar(1000, 2000), 3000)  # 1000 + 2000 = 3000

if __name__ == '__main__':
    unittest.main()

    unittest.main()
