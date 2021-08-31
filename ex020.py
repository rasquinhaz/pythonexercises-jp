from random import shuffle
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
list = [n1, n2, n3, n4]
shuffle(list)
print('A ordem de apresentação sera: \n [{}]'.format(list))

