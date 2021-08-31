print('           \033[1;36mMÉDIA DAS NOTAS DOS ALUNOS\033[m')
print(":-:"*20)
notaa = float(input('Digite a sua nota A: '))
notab = float(input('Digite a sua nota B: '))
media = (notaa + notab) / 2
list = [5.1, 6.9]
print('Você tirou {} na nota A e {} na nota B e a média das notas foi de {}'.format(notaa, notab, media))

if media < 5:
    print('Você foi \033[1;31mREPROVADO!\033[m')
elif media >=7:
    print('Você foi \033[1;32mAPROVADO!\033[m ')
    print('\033[1;32mParabéns!\033[31m <3\033[m')
elif media == 5.1 or list:
    print('Você deverá fazer a \033[1;31mRECUPERAÇÃO!\033[m')

