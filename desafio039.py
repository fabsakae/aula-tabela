from datetime import date
print('ALISTAMENTO MILITAR')
ano = int(input('Qual a ano de seu nascimento? '))
atual = date.today().year #int(input('Qual o ano atual? '))
servico = atual - ano
if servico < 18:
    print('Ainda não é momento para o alistamento militar, falta(m) {} ano(s) !'.format(18 - servico))
elif servico == 18:
    print('Chegou a hora do alistamento militar!')
else:
    print('Já passou {} ano(s) do tempo do alistamento militar !'.format(servico - 18))
