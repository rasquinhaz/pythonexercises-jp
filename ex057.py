sex = str(input('Digite o seu sexo: ')).strip().upper()[0]
while sex not in 'FfMm':
    sex = str(input('Inválido, Digite novamente = ')).strip().upper()[0]
print('Seus dados foram salvos com sucesso!, seu sexo é o {}'.format(sex))



