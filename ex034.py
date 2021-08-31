salario = int(input('Digite o valor do seu salário: '))
superior = (salario * 10)/100
inferior = (salario * 15)/100
if salario <= 1250:
    print('O seu salario com aumento de 15% é de {}'.format(inferior + salario))

if salario > 1250:
    print('O seu salario com aumento de 10% é de {}'.format(superior + salario))
