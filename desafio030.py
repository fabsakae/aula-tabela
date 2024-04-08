num = int(input('digite um número para saber se é PAR ou IMPAR: '))
par = num % 2
if par == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))
