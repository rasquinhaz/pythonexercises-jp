n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número:  '))
#Quem é o menor
me = n1
if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1 and n3 < n2:
    me = n3
#Quem é o maior
ma = n2
if n1 > n2 and n1 > n3:
    ma = n1
if n3 > n2 and n3 > n1:
    ma = n3
print('O maior número é o {}!'.format(ma))

print('O menor número foi o {}!'.format(me))






