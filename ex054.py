from datetime import date
maior = date.today().year
totma = 0
totme = 0
for pess in range(0, 7):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '))
    idade = maior - ano
    print('A idade é {}'.format(idade))
    if idade <= 20:
        print('Pessoa de menor!')
        totma += 1
    else:
        print('Pessoa de maioridade!')
        totme += 1
print('Ao todo tivemos {} pessoas de maior e {} de menor!'.format(totma, totme))


'''print('São {} que tem maioridade e {} que não tem maioridade.'.format())'''

