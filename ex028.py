from random import randint
from time import sleep
import colorsys

cpu = randint(0, 5)
print(':-:'*20)
print('Irei pensar em um número de 1 a 5... Tente adivinhar!')
print(':-:'*20)
print('pensando... AGUARDE 3 SEGUNDOS!')
sleep(3)
player = int(input('Em que número eu pensei?? ---> '))
print('Processando...')
sleep(2)
if player == cpu:
    print('Parabénss!! Você acertou na mosca! ')
else:
    print('Ganhei! Eu pensei no número {} e não no {}! '.format(cpu, player))



