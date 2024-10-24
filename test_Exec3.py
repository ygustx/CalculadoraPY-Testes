#Exercicio 3

import unittest
from calculadora import buscarUsuarioPorId, Usuario  # Importe o método e a classe

class TestUsuario(unittest.TestCase):

    def test_buscarUsuarioPorId_encontrado(self):
        # Testando se o usuário é encontrado
        usuario = buscarUsuarioPorId(1)  # ID que existe
        self.assertIsNotNone(usuario)  # O usuário não deve ser nulo
        self.assertEqual(usuario.nome, 'Alice')  # Verificando o nome do usuário

    def test_buscarUsuarioPorId_nao_encontrado(self):
        # Testando se o retorno é None quando o usuário não existe
        usuario = buscarUsuarioPorId(999)  # ID que não existe
        self.assertIsNone(usuario)  # O retorno deve ser nulo

if __name__ == '__main__':
    unittest.main()
