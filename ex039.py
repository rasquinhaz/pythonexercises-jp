from datetime import date
genero = str(input('Informe aqui o seu gênero entre (feminino) e (masculino): ')).upper()
if genero == 'FEMININO':
    print('Voce não necessita fazer o alistamento!')
    print(exit())
elif genero == 'MASCULINO':
    print('Seu alistamento é obrigatório.')
print('Agora siga os passos abaixo!')
nas = int(input('Informe o seu ano de nascimento: '))
print(':-0:' * 20)
hoje = date.today().year
idade = hoje - nas
print('Quem nasceu em {} tem {} anos em {}'.format(nas,idade, hoje))
if idade == 18:
    print('Você de se alistar assim que POSSÍVEL!!!')
elif idade > 18:
    saldo = idade - 18
    alistamento = hoje - saldo
    print('O seu tempo de alistamento passou faz {} anos!'.format(saldo))
    print('O ano do seu alistamento foi no ano de {}'.format(alistamento))
elif idade < 18:
    saldo = 18 - idade
    alistamento = nas + 18
    print('Você deve se alistar daqui a {} ano(s)!'.format(saldo))
    print('O seu ano de alistamento sera no ano de {}'.format(alistamento))










