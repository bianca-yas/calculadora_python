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
        primos = "1\n2\n3\n5"
        for i in range(5,21,1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primos += f'\n{i}'
        return primos

    def exercicio11(self):
        num = int(input('Informe um número: '))
        if num == 2 or num == 3 or num == 5:
            return f'O {num} é primo'
        elif num % 2 != 0 and num % 3 != 0 or num == 5:
            return f'O {num} é primo'
        return f'O {num} não é primo'

    def exercicio12(self,num):
        resultado = 1
        for i in range(1, num+1):
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
        num = int(input('Informe um número: '))
        s = 0
        while num:
            s += num % 10
            num //= 10
        return s

    def exercicio16(self):
        num = int(input('Informe um número: '))
        pares = ""
        impares = ""

        for i in range(1,num,1):
            if i % 2 == 0:
                pares += f'\n{i}'

            if i % 2 != 0:
                impares += f'\n{i}'

        return f'{pares} \n {impares}'

    def exercicio17(self):
        num = int(input('Informe um número: '))
        primos = ""
        if num == 1:
            return "1"
        elif num == 2:
            return f'2'
        elif num == 3:
            return f'2, 3'

        for i in range(1,num,1):
            if i % 2 != 0 and i % 3 != 0 or i == 5:
                primos += f'\n{i}'
        return primos

    def exercicio18(self,num):
        if num % 2 == 0:
            num = num / 2
            return num
        else:
            num = num * 3 + 1
            return num






    def exercicio19(self):
        num = int(input('Informe um número: '))
        pares =0
        impares =0

        for i in range(0,num):
            if i % 2 == 0:
                pares += i
            else:
                impares += i

        return f'{pares}\n{impares}'

    def exercicio20(self):
        num = int(input('Informe um número: '))
        divisores = 0

        for i in range(1, num + 1):
            if num % i == 0:
                divisores += i

        if divisores - num == num:
            return f'{num} é um número perfeito.'
        else:
            return f'{num} não é um número perfeito.'


    def exercicio21(self):
        num1 = 10
        num2 = 20

        aux = num1
        num1 = num2
        num2 = aux

        return f'A = {num1} \n B = {num2}'

    def exercicio22(self,num):
        return num-1

    def exercicio23(self):
        base = int(input('Informe a base do retângulo: '))
        altura = int(input('Informe a altura do retângulo: '))

        if base < 0 and altura < 0:
            return "Digite um número positivo."

        resultado = base * altura
        return resultado

    def exercicio24(self):
        anos = int(input('Informe sua idade em anos: '))
        meses = int(input('Informe sua idade em meses: '))
        dias = int(input('Informe sua idade em dias: '))

        if anos < 0 and meses < 0 and dias < 0:
            return "Informe um número positivo."

        totalDias = (anos*365) + (meses*30) + dias
        return totalDias

    def exercicio25(self):
        eleitores = int(input('Informe o total de eleitores: '))
        brancos = int(input('Informe o total de votos brancos: '))
        nulos = int(input('Informe o total de votos nulos: '))
        validos = int(input('Informe o total de votos válidos: '))

        if eleitores<0 and brancos<0 and nulos<0 and validos<0:
            return "Informe um valor positivo."

        percentual1 = (brancos*100)/eleitores
        percentual2 = (nulos*100)/eleitores
        percentual3 = (validos*100)/eleitores

        return f'Votos brancos: {percentual1} \n Votos nulos: {percentual2} \n Votos válidos: {percentual3}'


    def exercicio26(self):
        salario = int(input('Informe seu salário: '))
        percentual = int(input('Informe o percentual de reajuste: '))

        if salario<0 and percentual<0:
            return "Informe um valor positivo."


        salarioNovo = (salario*percentual)/100
        return salarioNovo

    def exercicio27(self):
        custoFabrica = int(input('Informe o custo de fábrica: '))

        if custoFabrica<0:
            return "Informe um valor positivo: "

        precoFinal = custoFabrica + custoFabrica*0.28 + custoFabrica*0.45
        return precoFinal

    def exercicio28(self):
        nota1 = int(input('Informe a primeira nota: '))
        nota2 = int(input('Informe a segunda nota: '))
        nota3 = int(input('Informe a terceira nota: '))

        if nota1<0 or nota1>10 and nota2<0 or nota2>10 and nota3<0 and nota3>10:
            return "Informe um valor entre 0 e 10."

        media = (nota1+nota2+nota3)/3
        return media

    def exercicio29(self):
        quantidade = int(input('Informe a quantidade de maçãs: '))

        if quantidade < 0 or quantidade > 12:
            return "Informe um número entre 1 e 12."
        elif quantidade == 12:
            total = quantidade*1.00
        elif quantidade < 12:
            total = quantidade*1.30

            return total

    def exercicio30(self):
        lista = []
        for i in range(1,11,1):
            num = int(input('Informe um número: '))
            lista+= f'\n{num}'


        return lista


    def exercicio31(self):
        salario = int(input('Informe seu salário fixo: '))
        vendas = int(input('Informe o valor das vendas efetuadas: '))

        if salario<0 or vendas<0:
            return "Informe um valor positivo."
        elif vendas < 1500 or vendas == 1500:
            comissao = vendas*0.03
            total = salario+comissao

            return total
        elif vendas>1500:
            comissao = vendas*0.05*0.03
            total = salario+comissao

            return total

    def exercicio32(self):
        conta = int(input('Informe o número da conta: '))
        saldo = int(input('Informe o saldo da conta: '))
        credito = int(input('Informe os créditos da conta: '))
        debito = int(input('Informe o débito da conta: '))

        if credito < 0:
            return "Informe um valor positivo"
        elif debito > 0:
            return "Informe um valor negativo"

        saldoA = saldo - debito + credito
        if saldoA < 0 or saldoA == 0:
            return "Saldo atual negativo"
        elif saldoA > 0:
            return "Saldo atual positivo"


    def exercicio33(self):
        resultado = ""
        num = int(input('Informe um valor inteiro: '))

        if num > 10 or num < 0:
            return "Informe um número entre 1 e 10"

        for i in range(0, 11, 1):
            resultado += f'\n{num} * {i} = {num * i}'
        return resultado

    def exercicio34(self):
        lista = ""
        num = int(input('Informe um número: '))
        if num <0:
            return "Informe um valor positivo."

        for i in range(1,num,1):
            lista += f'\n{i}'

        return lista

    def exercicio35(self):
        negativos = ""

        for i in range(0,11,1):
            num = int(input('Informe um número: '))

            if num < 0:
                negativos += f'\n{num}'
        return negativos

    def exercicio36(self):
        soma = 0

        for i in range(1,11,1):
            num = int(input('Informe um número: '))

            if num < 40:
                soma+=num
        return soma

    def exercicio37(self):
        soma = sum(range(15,100))
        return soma/85

    def exercicio38(self):
        quant = int(input('Informe uma quantidade: '))
        maior = 0
        soma = 0

        for i in range(0,quant,1):
            num = int(input('Informe um número: '))
            maior = num

            if num > maior:
                maior = num

            soma += num
            media = soma/quant
        return f'O maior número é: {maior} \n A média dos números digitados é: {media}'

    def exercicio39(self):
        soma = 0
        media = 0
        maiores = ""
        for i in range(1,21,1):
            nota = int(input('Informe a nota do aluno: '))
            if nota > 10 or nota < 0:
                return "Informe uma nota entre 0 e 10."

            soma += nota
            media = soma/20

            if nota > media:
                maiores += f'\n{nota}'
        return f'A média da turma é: {media} \n Notas acima da média: {maiores}'

    def exercicio40(self):
        salario1 = int(input('Informe seu salário: '))
        salario2 = int(input('Informe seu salário: '))
        salario3 = int(input('Informe seu salário: '))

        filhos1 = int(input('Informe a quantidade de filhos: '))
        filhos2 = int(input('Informe a quantidade de filhos: '))
        filhos3 = int(input('Informe a quantidade de filhos: '))

        if salario1<0 or salario2<0 or salario3<0:
            return "Informe valores positivos."

        if filhos1<0 or filhos2<0 or filhos3<0:
            return "Informe valores positivos."

        mediaSalario = (salario1+salario2+salario3)/3
        mediaFilhos = (filhos1+filhos2+filhos3)/3

        maior = 0
        if salario1 > salario2 and salario1 > salario3:
            maior = salario1
        elif salario2 > salario1 and salario2 > salario3:
            maior = salario2
        elif salario3 > salario1 and salario3 > salario2:
            maior = salario3

        return f'Média de salários: {mediaSalario} \n Média de filhos: {mediaFilhos} \n Maior salário: {maior}'











































