from math import factorial
print('Digite um número para calcular o seu FATORIAL.')
n = int(input('Seu número: '))
c = n
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end=' ')
    c -= 1


