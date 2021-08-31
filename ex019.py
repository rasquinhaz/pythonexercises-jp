from random import choice
a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))
a4 = str(input('Nome do aluno 4: '))
list = [a1,a2,a3,a4]
r = choice(list)
print('O aluno escolhido é:{} '.format(r))





