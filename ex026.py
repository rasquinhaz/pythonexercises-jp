f = str(input('Digite uma frase: ')).strip().upper()
print('A letra "a" apareceu {} vezes na frase. '.format(f.count('A')))
print('A primeira letra "a" apareceu na posição {}'.format(f.find('A')+1))
print('A ultima letra "a" apareceu na posição {}'.format(f.rfind('A')+1))


