s = 0
c = 0
print('{:=^40}'.format(' NÚMEROS MÚLTIPLOS DE 3 '))
for n in range(0, 500+1, 3):
    if n % 2 == 1:
        if n % 3 == 0:
            c = c + 1
            s = s + c
print('A soma de todos os {} números é {}'.format(c, s))


print('FIM')
