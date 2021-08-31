from time import sleep
a = int(input('Digite um valor: '))  # valor a
b = int(input('Digite um valor: '))  # valor b
sair = 5
menu = ('[ 1 ] Somar\n'  # MENU
        '[ 2 ] multiplicar \n'
        '[ 3 ] maior\n'
        '[ 4 ] Novos números\n'
        '[ 5 ] sair do programa')
usuario = 0
while usuario != sair:
    print('==' * 20)
    print(menu)
    usuario = int(input('Qual será a sua jogada? = '))
    print('==' * 20)
    if usuario == 1:
        somar = a + b
        print(f'{a} + {b} = {somar}')
    elif usuario == 2:
        multiplicar = a * b
        print(f'{a} x {b} = {multiplicar}')
    elif usuario == 3:
        if a > b:
            print(f'entre {a} e {b} o {a} é maior! ')
        else:
            print(f'Entre {a} e {b} o {b} é maior!')
    elif usuario == 4:
        print('Informe os valores novamente:')
        a = int(input('Digite um valor: '))
        b = int(input('Digite um valor: '))
    elif usuario == 5:
        sleep(0.5)
        print('Finalizando...', end='...')
        sleep(0.5)
    else:
        print('Opção inválida, Tente novamente!')
print('OK, até mais!')
