media = 0
nomevelho = ''
maioridade = 0
cont = 0
for p in range(1, 5):
    print('====== {}ª Pessoa ======='.format(p))
    nome = str(input('Seu nome: ')).strip()
    idade = int(input('Sua idade: '))
    sexo = str(input('Seu sexo [ F/M ]: ')).strip()
    media += idade / 4
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and maioridade < idade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        cont += 1
print('A media de idades das 4 pessoas foram de {}'.format(media))
print('O nome do homem mais velho é {} e sua idade é {} '.format(nomevelho, maioridade))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(cont))











