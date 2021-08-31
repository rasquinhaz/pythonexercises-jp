'''from random import randint
from time import sleep
cpu = randint(0, 10)
count = 0
player = int(input("Irei pensar em um número de 0 a 10, tente advinhar: "))
while player != cpu:
    print('Pensando...', end=' ')
    sleep(0.5)
    for c in range(0, 3):
        print('...', end=' ')
        sleep(0.5)
    print('Dados Prontos!')
    player = int(input('Você errou!, tente novamente = '))
    count += 1
print('Pensando...', end=' ')
sleep(0.5)
for c in range(0, 3):
    print('...', end=' ')
    sleep(0.5)
print('Dados já processados!')
print(f'Boa! Na mosca! o número que eu pensei foi {player} e você errou {count} vezes!')
'''

from random import randint
from time import sleep
cpu = randint(0, 10)
count = 0
print('Olá, eu sou o seu computador')
print('Eu pensei em um número de 0 a 10, quero que advinhe em que número eu pensei!')
sleep(1.5)
print('==' * 25)
player = int(input('Qual é a sua jogada? '))
while player != cpu:
    if player > cpu:
        print('Um pouco menos...  ', end=' ')
        player = int(input('Digite novamente:'))
    if player < cpu:
        print('Um pouco mais...', end=' ')
        player = int(input('Digite novamente: '))
    count += 1
print('Parabéns! você acertou  :) ')
print(f'foram necessárias {count} tentativas para descobrir!')





