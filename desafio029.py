velocidade = float(input('qual velocidade voce está? '))
multa = (velocidade - 80) * 7
if multa > 80:
    print('Excedeu a velocidade permitida, sua multa será de {:.2f}'.format(multa))
else:
    print('Velocidade Permitida!')
