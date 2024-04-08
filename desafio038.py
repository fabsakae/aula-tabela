num1 = int(input('digite o primeiro número: '))
num2 = int(input('Digite o segundo n´mero: '))
if num1 > num2:
    print('o primeiro número {} é maior que o segundo número {}'.format(num1, num2))
elif num2 > num1:
    print('O segundo número {} é maior que o primeiro número {}'.format(num2, num1))
else:
    print('Não existe valor maior, os dois são iguais!')
