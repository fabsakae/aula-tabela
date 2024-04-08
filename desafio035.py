reta1 = float(input('Digite o primeiro segmento da reta: '))
reta2 = float(input('Digite o segundo segmento da reta: '))
reta3 = float(input('Digite o terceiro segmento da reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Formam um triangulo')
else:
    print('Não formam um triangulo')
