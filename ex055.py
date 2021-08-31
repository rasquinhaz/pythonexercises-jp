list = []
for contagem in range(1, 6):
    peso = float(input('Insira o {}º peso: '.format(contagem)))
    list += [peso]
    list.sort()
print('The lowest weight is: {}'.format(min(list)))  # Menor item da lista
print('The highest weight is {}'.format(max(list)))  # Maior item da lista

'''media = 0
lista = []
count = 0
contar = 0
for pp in range(1, 5):
    print('======= Peso da {}ª pessoa ======= \n'.format(pp))
    peso = float(input('Insira seu peso aqui: '))
    media += peso/4
    lista += [peso]
    lista.sort()
    if peso <= 50:
        count += 1
    if peso > 51:
        contar += 1



print(" A média dos pesos foi de {}".format(media))
print('O maior peso foi de {}'.format(max(lista)))
print('O menor peso foi de {}'.format(min(lista)))

print('A quantidade de pessoas magras foram: {}'.format(count))
print('A quantidade de pessoas gordas foram: {}'.format(contar))'''










