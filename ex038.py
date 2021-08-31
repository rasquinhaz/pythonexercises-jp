n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
cores = {'vermelho': '\033[1;31m', 'azul':'\033[1;34m', 'amarelo': '\033[1;33m'}

if n1 > n2:
    print('{}O primeiro valor é o maior!'.format(cores['azul']))
elif n2 > n1:
    print('{}O segundo valor é o maior!'.format(cores['vermelho']))
else:
    print('{}Os dois valores são iguais!'.format(cores['amarelo']))
