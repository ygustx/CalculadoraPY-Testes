# calculadora.py

# Código da calculadora interativa
if __name__ == "__main__":
    num1 = 0
    num2 = 0
    result = 0
    op = ''

    while True:
        num1 = float(input('Digite o Primeiro numero: '))
        op = input('Digite a operacao (+, -, *, /): ')
        num2 = float(input('Digite o Segundo numero: '))

        if op == '+':
            result = somar(num1, num2)  # Aqui usamos o método somar
        elif op == '-':
            result = num1 - num2
        elif op == '/':
            if num2 != 0:  # Verifica se o divisor é zero
                result = num1 / num2
            else:
                print('Erro: Divisão por zero!')
                continue
        elif op == '*':
            result = num1 * num2
        else:
            print('Operação não reconhecida!')
            continue

        print('{} {} {} = {}'.format(num1, op, num2, result))

##############################################################################

class Usuario:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

# Simulando um banco de dados com um dicionário
usuarios_db = {
    1: Usuario(1, 'Alice'),
    2: Usuario(2, 'Bob'),
    3: Usuario(3, 'Charlie'),
}

def buscarUsuarioPorId(id: int):
    return usuarios_db.get(id, None)  # Retorna o usuário se encontrado, caso contrário, retorna None

##############################################################################
def somar(a: int, b: int) -> int:
    return a + b


##############################################################################
def ehPar(n: int) -> bool:
    return n % 2 == 0  # Retorna True se n é par, False se n é ímpar

##############################################################################
def adicionarItem(lista, item):
    lista.append(item)  # Adiciona o item à lista

# Código da calculadora interativa (mantido como estava)
if __name__ == "__main__":
    # Seu código existente da calculadora
    pass

##############################################################################
def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisor não pode ser zero")  # Lança exceção se o divisor for zero
    return a / b

##############################################################################
class Singleton:
    _instancia = None

    @staticmethod
    def obterInstanciaUnica():
        if Singleton._instancia is None:
            Singleton._instancia = Singleton()
        return Singleton._instancia