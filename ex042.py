
cores = {'azul': '\033[1;34m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m', 'limpa': '\033[m',
         'branco': '\033[97m',
         'magenta': '\033[1;35m',
         'black': '\033[1;30;107m'}
print('      {}MEDIDAS E CLASSIFICAÇÕES DE TRIANGULOS{}'.format(cores['magenta'], cores['limpa']))
a = float(input('1º Segmento: '))
print('=='*25)
b = float(input('2° Segmento: '))
print('=='*26)
c = float(input('3° Segmento: '))
pformar = a < b+c and b < c+a and c < a+b
nformar = a > b+c and b > (a+c) and c < (a+b)

if pformar and a != b and b != c and c != a:
    print('{}Os segmentos PODEM formar um triângulo!{}'.format(cores['azul'], cores['limpa']))
    print('{}O triangulo é ESCALENO{}!'.format(cores['vermelho'], cores['limpa']))

elif pformar and a == b and b == c and c==a:
    print('Os segmentos PODEM formar um triângulo!')
    print('{}O triangulo é EQUILÁTERO{}'.format(cores['amarelo'], cores['limpa']))

elif pformar and a==b and c != a and c != b:
    print('{}Os segmentos PODEM formar um triângulo!{}'.format(cores['branco'], cores['limpa']))
    print('{}O triangulo é o ISÓSCELES!{}'.format(cores['magenta'], cores['limpa']))

elif pformar and b==c and a != c and a != b:
    print('{}Os segmentos PODEM formar um triângulo!{}'.format(cores['branco'], cores['limpa']))
    print('{}O triangulo é o ISÓSCELES!{}'.format(cores['magenta'], cores['limpa']))

elif pformar and c== a and b != c and b != a:
    print('{}Os segmentos PODEM formar um triângulo!{}'.format(cores['branco'], cores['limpa']))
    print('{}O triangulo é o ISÓSCELES!{}'.format(cores['magenta'], cores['limpa']))
else:
    print('{}Os segmentos NÃO PODEM formar um triângulo!{}'.format(cores['black'], cores['limpa']))






