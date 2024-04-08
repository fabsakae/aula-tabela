salario = float(input('Digite o salário para calcular o aumento: R$ '))
basesal = 1250
aumento1 = (salario * 15/100) + salario
aumento2 = (salario * 10/100) + salario
if salario > basesal:
    print('Seu aumento é de 10 por cento e será de R$ {:.2f}'.format(aumento2))
else:
    print('Seu salário aumentou 15 por cento e ficará de R$ {:.2f}'.format(aumento1))
