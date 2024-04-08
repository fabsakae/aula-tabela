km = float(input('Digite quantos KM percorridos: '))
valor = km * 0.50
valor2 = km * 0.45
if km <= 200:
    print('voce percorreu {} km e o valor a ser pago será de: R$ {:.2f}'.format(km, valor))
else:
    print('voce pecorreu {} km e o valor a ser pago será de: R$ {:.2f}'.format(km, valor2))
