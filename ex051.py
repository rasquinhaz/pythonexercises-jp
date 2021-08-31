print('{:.^70}'.format('PROGREÇÃO ARITMÉTICA'))
p = int(input('Digite um valor: '))
r = int(input('Razão: '))
décimo = p + (10 - 1) * r
for p in range(p, décimo + r, r):
    print(p, end=(' → '))
print('Acabou!')


