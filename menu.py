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
              '\n22. Exercicio 15' +
              '\n23. Exercicio 16' +
              '\n24. Exercicio 17' +
              '\n25. Exercicio 18' +
              '\n26. Exercicio 19' +
              '\n27. Exercicio 20' +
              '\n28. Exercicio 21' +
              '\n29. Exercicio 22' +
              '\n30. Exercicio 23' +
              '\n31. Exercicio 24' +
              '\n32. Exercicio 25' +
              '\n33. Exercicio 26' +
              '\n34. Exercicio 27' +
              '\n35. Exercicio 28' +
              '\n36. Exercicio 29' +
              '\n37. Exercicio 30' +
              '\n38. Exercicio 31' +
              '\n39. Exercicio 32' +
              '\n40. Exercicio 33' +
              '\n41. Exercicio 34' +
              '\n42. Exercicio 35' +
              '\n43. Exercicio 36'+
              '\n44. Exercicio 37' +
              '\n45. Exercicio 38' +
              '\n46. Exercicio 39' +
              '\n47. Exercicio 40')

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
                print(f'{self.exer.exercicio11()}')
            elif self.opcao == 19:
                num = int(input('Informe um número: '))
                print(f'O fatorial do número digitado é: {self.exer.exercicio12(num)}')
            elif self.opcao == 20:
                print(f'A sequencia de fibonacci até 10 é: {self.exer.exercicio13()}')
            elif self.opcao == 21:
                self.cooletar()
                print(f'{self.exer.exercicio14(self.num)}')
            elif self.opcao == 22:
                print(f'A soma dos digitos é: {self.exer.exercicio15()}')
            elif self.opcao == 23:
                print(f'\n {self.exer.exercicio16()}')
            elif self.opcao == 24:
                print(f'\n {self.exer.exercicio17()}')
            elif self.opcao == 25:
                num = int(input('Informe um número: '))
                print(f'\n {self.exer.exercicio18(num)}')
            elif self.opcao == 26:
                print(f'\n {self.exer.exercicio19()}')
            elif self.opcao == 27:
                print(f'\n {self.exer.exercicio20()}')
            elif self.opcao == 28:
                print(f'\n {self.exer.exercicio21()}')
            elif self.opcao == 29:
                num = int(input('Digite um número: '))
                print(f'\n {self.exer.exercicio22(num)}')
            elif self.opcao == 30:
                print(f'\n As dimensões do retângulo são: {self.exer.exercicio23()}')
            elif self.opcao == 31:
                print(f'\n Sua idade em dias no total é: {self.exer.exercicio24()}')
            elif self.opcao == 32:
                print(f'\n {self.exer.exercicio25()}')
            elif self.opcao == 33:
                print(f'\n {self.exer.exercicio26()}')
            elif self.opcao == 34:
                print(f'\n O custo final é de: {self.exer.exercicio27()}')
            elif self.opcao == 35:
                print(f'A média desse aluno será: {self.exer.exercicio28()}')
            elif self.opcao == 36:
                print(f'O valor total pelas maçãs será de: {self.exer.exercicio29()}')
            elif self.opcao == 37:
                print(f'\n {self.exer.exercicio30()}')
            elif self.opcao == 38:
                print(f'\n O salário total é de: {self.exer.exercicio31()}')
            elif self.opcao == 39:
                print(f'\n {self.exer.exercicio32()}')
            elif self.opcao == 40:
                print(f'\n {self.exer.exercicio33()}')
            elif self.opcao == 41:
                print(f'\n {self.exer.exercicio34()}')
            elif self.opcao == 42:
                print(f'\n {self.exer.exercicio35()}')
            elif self.opcao == 43:
                print(f'\n A soma dos números inferiores a 40 é: {self.exer.exercicio36()}')
            elif self.opcao == 44:
                print(f'\n A média aritmética entre 15 e 100 é: {self.exer.exercicio37()}')
            elif self.opcao == 45:
                print(f'\n {self.exer.exercicio38()}')
            elif self.opcao == 46:
                print(f'\n {self.exer.exercicio39()}')
            elif self.opcao == 47:
                print(f'\n {self.exer.exercicio40()}')



