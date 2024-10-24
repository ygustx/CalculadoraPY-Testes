#Exercicio 4

# test_adicionar_item.py

import unittest
from calculadora import adicionarItem  # Importe o método que adiciona itens

class TestAdicionarItem(unittest.TestCase):

    def test_adicionar_item(self):
        lista = []  # Lista vazia
        item = 'item1'
        adicionarItem(lista, item)  # Adicionando item à lista

        # Verificando se o item foi adicionado
        self.assertTrue(item in lista)  # O item deve estar na lista

if __name__ == '__main__':
    unittest.main()
