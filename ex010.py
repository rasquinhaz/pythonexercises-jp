c = float(input('Digite o valor que você possui na sua carteira R$: '))
d = c/3.27

cores = {'limpa':'\033[m',
         'azul' :'\033[1;34m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'branco': '\033[1;30m'}
print('Este é o quanto de doláres que você pode comprar: {}{:.2f}{}'.format(cores['azul'],d,cores['limpa']))
