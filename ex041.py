print('            \033[1;34;41mConfederação Nascional de Natação\033[m')
ano = int(input('Insira aqui a sua idade: '))
# Cores: \033[36m
print('::-::-::' * 25)
print('CATEGORIAS')
cores = {'azul': '\033[1;34m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m', 'limpa': '\033[m',
         'branco': '\033[97m',
         'magenta': '\033[1;35m'}
if ano <= 9:
    print('{}Sua categoria é Mirim!{}'.format(cores['amarelo'], cores['limpa']))
elif ano > 9 and ano < 15:
    print('{}Sua Categoria é infantil{}'.format(cores['azul'], cores['limpa']))
elif ano > 14 and ano < 20:
    print('{}Sua categoria é Junior!{}'.format(cores['vermelho'], cores['limpa']))
elif ano > 19 and ano < 26:
    print('{} Sua Categoria é Sênior!{}'.format(cores['branco'], cores['limpa']))
else:
    print('{}A sua Categoria é MASTER!{}'.format(cores['magenta'], cores['limpa']))


'''elif 14 > ano > 9:
    print('\033[36mSua categoria é Infantil\033[m')
elif 15 < ano > 19:
    print('coco')
    print('{}Sua categoria é Junior!{}'.format(cores['vermelho'], cores['limpa']))'''

