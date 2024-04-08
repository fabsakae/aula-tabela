num = int(input('Digite um número inteiro para conversão:'))
conv = int(input('Digite\n-> 1 para binário\n-> 2 para octal\n-> 3 para hexadecimal\na opção : '))
if conv == 1:
    print('{} convertido em BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif conv == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif conv == 3:
    print('{} convrtido para HEXADECIMAL é iual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, digite novamente!')
