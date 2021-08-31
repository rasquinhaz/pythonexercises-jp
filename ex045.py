from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Opções de Jogada
[ 0 ] = Pedra
[ 1 ] = Papel 
[ 2 ] = Tesoura''')
player = int(input('Qual será a sua jogada? '))
sleep(1)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[player]))
if computador == 0: # O computador Jogou Pedra
    if player == 0:
        print('Empate!')
    elif player == 1:
        print('Jogador vence!')
    elif player == 2:
        print('Computador vence!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # O computador Jogou Papel
    if player == 1:
        print('EMPATE!')
    elif player == 0:
        print('Computador vence!')
    elif player == 2:
        print('Jogador Ganha!')
    else:
        print('Jogada inválida')
elif computador == 2: # O computador jogou tesoura
    if player == 2:
        print('EMPATE!')
    elif player == 1:
        print('Computador vence!')
    elif player == 0:
        print('Jogador vence!')
    else:
        print('JOGADA INVÁLIDA')








