n = str(input('Digite o seu nome: ')).strip()
#frase = 'João Pedro Rasquinha Kunrath'

print('O seu nome em letra maiúsculas fica: {}'.format(n.upper()))
print('O seu nome em letras minúsculas fica: {}'.format(n.lower()))
print('O seu nome tem {} letras! '.format(len(n) - n.count(' ')))
spl = n.split()
print('O seu primeiro nome tem {} letras!'.format(len(spl[0])))










