from operacao import Operacao
from operacao import Exercicios

class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer = Exercicios()
        self.opera = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):
        print('\n----- MENU -----\n\n' +
              'Escolha uma das opções abaixo: ' +
              '\n0. Sair' +
              '\n1. Somar' +
              '\n2. Subtrair' +
              '\n3. Dividir' +
              '\n4. Multiplicar' +
              '\n5. Potência' +
              '\n6. Raiz' +
              '\n7. Tabuada' +
              '\n8. Exercicio 01' +
              '\n9. Exercicio 02' +
              '\n10. Exercicio 03' +
              '\n11. Exercicio 04' +
              '\n12. Exercicio 05' +
              '\n13. Exercicio 06' +
              '\n14. Exercicio 07' +
              '\n15. Exercicio 08' +
              '\n16. Exercicio 09' +
              '\n17. Exercicio 10' +
              '\n18. Exercicio 11' +
              '\n19. Exercicio 12' +
              '\n20. Exercicio 13' +
              '\n21. Exercicio 14' +
              '\n22. Exercicio 15')

    def coletar(self):
        self.num1 = int(input('Informe o primeiro número: '))
        self.num2 = int(input('Informe o segundo número: '))

    def cooletar(self):
        self.num = int(input('Informe um número: '))

    def operacaoo(self):
        while self.opcao != 0:
            self.mostrarMenu()  # Chamando as opções
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 0:
                print('Obrigado!!')
            if self.opcao == 1:
                self.coletar() #Chamando o input por meio do coletar
                print(f'A soma dos números é {self.opera.somar(self.num1, self.num2)}')
            elif self.opcao == 2:
                self.coletar()
                print(f'A subtração dos números coletados é: {self.opera.subtrair(self.num1, self.num2)}')
            elif self.opcao == 3:
                self.coletar()
                print(f'A divisão dos números coletados é: {self.opera.dividir(self.num1, self.num2)}')
            elif self.opcao == 4:
                self.coletar()
                print(f'A multiplicação dos números coletados é: {self.opera.multiplicar(self.num1, self.num2)}')
            elif self.opcao == 5:
                self.coletar()
                print(f'A potência dos números digitados é: {self.opera.potencia(self.num1, self.num2)}')
            elif self.opcao == 6:
                self.coletar()
                print(f'A raiz de {self.num1} é: {self.opera.raiz(self.num1)}')
                print(f'A raiz de {self.num2} é: {self.opera.raiz(self.num2)}')
            elif self.opcao == 7:
                print(f'A tabuada de {self.num1} é: {self.opera.tabuada(self.num1)}')
                print(f'A tabuada de {self.num2} é: {self.opera.tabuada(self.num2)}')
            elif self.opcao == 8:
                self.coletar()
                print(f'\n {self.exer.exercicio1()}')
            elif self.opcao == 9:
                print(f'\n {self.exer.exercicio2()}')
            elif self.opcao == 10:
                print(f'A soma dos números de 1 até 100 é: {self.exer.exercicio3()}')
            elif self.opcao == 11:
                print(f'Os múltiplos de 5 de 1 até 50 são: {self.exer.exercicio4()}')
            elif self.opcao == 12:
                self.cooletar()
                print(f'\n {self.exer.exercicio5(self.num)}')
            elif self.opcao == 13:
                self.cooletar()
                print(f'\n {self.exer.exercicio6(self.num)}')
            elif self.opcao == 14:
                self.cooletar()
                print(f'A tabuada do número digitado é: {self.exer.exercicio7(self.num)}')
            elif self.opcao == 15:
                self.cooletar()
                print(f'\n {self.exer.exercicio8(self.num)}')
            elif self.opcao == 16:
                self.cooletar()
                print(f'A soma de 1 até o número digitado é: {self.exer.exercicio9(self.num)}')
            elif self.opcao == 17:
                print(f'Os números primos de 1 a 20 são: {self.exer.exercicio10()}')
            elif self.opcao == 18:
                self.cooletar()
                print(f'O número digitado é: {self.exer.exercicio11(self.num)}')
            elif self.opcao == 19:
                self.cooletar()
                print(f'O fatorial do número digitado é: {self.exer.exercicio12(self.num)}')
            elif self.opcao == 20:
                print(f'A sequencia de fibonacci até 10 é: {self.exer.exercicio13()}')
            elif self.opcao == 21:
                self.cooletar()
                print(f'{self.exer.exercicio14(self.num)}')
            elif self.opcao == 22:
                print(f'A soma dos digitos é: {self.exer.exercicio15()}')



