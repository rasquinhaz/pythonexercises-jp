soma = 0
cont = 0
for n in range(0, 6):
    dig = int(input('Digite um número: '))
    if dig % 2 == 0:
        soma = soma + dig
        cont = cont + 1

print('A soma de todos os {} números pares resultará em {}'.format(cont, soma))

