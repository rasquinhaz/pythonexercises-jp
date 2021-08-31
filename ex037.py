numero = int(input('\033[1;33mDigite um número: '))
print('Escolha um das bases para conversão:\033[m ')
print('\033[36m[ 1 ] Para converter para binário\033[m \n\033[1;35m[ 2 ] Para Octal\033[m\n\033[31m[ 3 ] Para Hexadecimal\033[m ')
opção = int(input('Sua opção: '))
cores = {'limpa' : '\033[m ', 'amarelo': '\033[33m', 'vermelho': '\033[31m'}
if opção == 1:
    print('O número {} em binário é igual a {}'.format(cores['vermelho'], numero, bin(numero)[2:]))
elif opção == 2:
    print('O número {} em Octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('O número {}{}{}em Hexadecimal é igual a {}'.format(cores['vermelho'],numero,cores['limpa'], hex(numero)[2:]))
else:
    print('Número digitado inválido!')






