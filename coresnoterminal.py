print('\033[30;43m-=\033[m' * 10)
print('\033[4;31;47mOlá, mundo!\033[m')
a = 3
b = 5
print('os valores são \033[32m{}\033[m e \033[33m{}\033[m !!'.format(a, b))
nome = 'FABIOLA'
cores = {'limpa': ' \033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'peb': '\033[30m'}
print('Olá, {}{}{}!!!'.format(cores['peb'], nome, cores['limpa']))
soma = 3 * 5 + 4 ** 2
print(soma)
