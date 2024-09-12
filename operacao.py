import math

class Operacao:
    def __init__(self): #Construtor
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self, num1, num2):
        self.coletar(num1, num2) #Utilizando o método coletar
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1, num2)
        if self.num2 <= 0:
            return "Impossivel dividir."
        else:
            return self.num1 / self.num2

    def tabuada(self, num1):
        resultado = ""
        for i in range(0,11,1):
            resultado += f'\n{num1} * {i} = {num1 * i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num):
        return math.sqrt(num)

class Exercicios:

    def __init__(self):
        self.num = 0

    def coletar(self, num):
        self.num = num

    def exercicio1(self):
        resul = ""
        for i in range(0,11,1):
            resul += f'\n{i}'
        return resul

    def exercicio2(self):
        pares = ""
        for i in range(1,21,1):
            if i % 2 == 0:
                pares += f'\n{i}'
        return pares

    def exercicio3(self):
        soma = sum(range(1, 101))
        return soma

    def exercicio4(self):
        multi = ""
        for i in range(1,51,1):
            if i % 5 == 0:
                multi += f'\n{i}'
        return multi

    def exercicio5(self, num):
        self.coletar(num)
        if num % 2 == 0:
            return f'Este número é par'
        else:
            return f'Este número é ímpar'

    def exercicio6(self, num):
        self.coletar(num)
        if num > 0:
            return f'Este número é positivo'
        elif num < 0:
            return f'Este número é negativo'
        elif num == 0:
            return f'Este número é igual a zero.'

    def exercicio7(self, num):
        self.coletar(num)
        resultado = ""
        for i in range(0,num,1):
            resultado += f'\n{num} * {i} = {num * i}'
        return resultado

    def exercicio8(self, num):
        self.coletar(num)
        resul = ""
        for i in range(1, num, 1):
            resul += f'\n{i}'
        return resul

    def exercicio9(self, num):
        self.coletar(num)
        soma = sum(range(1, num))
        return soma

    def exercicio10(self):
        primos = ""
        for i in range(2,21,1):
            if math.sqrt(i) == 0:
                return f'Sem números primos'
            else:
                primos += f'\n{i}'
        return primos

    def exercicio11(self, num):
        self.coletar(num)
        raiz = math.sqrt(num)
        for i in range(2,num,1):
            if num % i == 0:
                return f'Não é primo'
            else:
                return f'É primo.'

    def exercicio12(self, num):
        self.coletar(num)
        resultado = -1
        for i in range(1,num,1):
            resultado *= i
        return resultado

    def exercicio13(self):
        i = 0
        a = 0
        b = 1
        c = 0
        resultado = f'{a}\n{b}'
        for i in range(1,11,1):
            c = a + b
            resultado += f'\n{c}'
            a = b
            b = c
        return resultado

    def exercicio14(self,num):
        self.coletar(num)
        raiz = int(math.sqrt(num))

        if 5*num*num+4 or 5*num*num-4 == raiz:
            return f'Esse número está presente na sequencia de Fibonacci'
        else:
            return f'Esse número não é de Fibonacci'

    def exercicio15(self):
        num = int(input('Digite um número: '))
        return sum(int(i) for i in num)























