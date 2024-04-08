#import random
#frase1 = str('Vou pensar em um número entre 0 e 5. Tente adivinhar ...')
#print(frase1)
#frase2 = str(input('Qual número pensei? ')).strip()
#lista = ['0', '1', '2', '3', '4', '5']
#print(random.choice(lista))
#if random.choice == lista:
 #   print('Parabéns você acertou!')
#else:
#   print('Você errou!')
from random import randint
from time import sleep
computador = randint(0, 5)#faz o computador sortear
#print('pensei no número {}'.format(computador)) comoando ara ver se o sorteio funciona
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar ....')
print('-=-' * 20)
jogador = int(input('Qual número eu pensei ? '))#jogador tenta adivinhar
print('PROCESSANDO ...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! voce acertou')
else:
    print('Ganhei! o número foi {} e não {}!'.format(computador, jogador))
