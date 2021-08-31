a = float(input('Digite o primeiro valor: '))
b = float(input('Digie o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

if a< b+c and b< a+c and c< b+a:
    print('As somas dos lados podem formar um triangulo!')
else:
    print('As somas dos lados não podem formar um triangulo!')

