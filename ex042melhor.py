a = float(input('Digite o valor do segmento A: '))
b = float(input('Digite o valor do segmento B: '))
c = float(input('Digite o valor do segmento C: '))
pformar = a < b+c and b < c+a and c < a+b
if pformar:
    print('Os segmentos podem formar um triangulo', end=' ')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos NÃO PODEM formar um triângulo ')


