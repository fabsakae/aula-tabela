nome = str(input('Qual o seu nome? ')).strip()
if nome == 'Gustavo':
    print('\033[33mQue nome lindo!'.format(nome))
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bíblico!')
elif nome in 'Ana Claudia jéssica Juliana':
    print('Belo nome Feminino')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {} !'.format(nome))
