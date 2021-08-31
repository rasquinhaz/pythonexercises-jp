n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end=' ')
        total += 1
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end=' ')
print('---> O número {} foi divisível {} vezes.'.format(n, total))
if total ==2:
    print('O número É PRIMO!')
else:
    print('O número NÃO é primo')


