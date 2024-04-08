print('\033[1;30;43m~**~\033[m' * 10)
casa = float(input('Qual Valor do imóvel? R$ '))
sal = float(input('Qual valor do salário do comprador? R$ '))
ano = float(input('Em quantos anos irá pagar? '))
mes = ano * 12
print('Serão pagos em\033[1;34m {:.0f}\033[m meses'.format(mes))
prestacao = casa / mes
print('Sua prestação mensal será de R$ \033[1;34m{:.2f}\033[m'.format(prestacao))
if prestacao > (sal * 30 / 100):
    print('\033[1;30;41mEmprestimo negado\033[m')
else:
    print('\033[1;30;42mEmpréstimo aceito\033[m')
