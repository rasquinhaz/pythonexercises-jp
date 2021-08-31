from datetime import date
born = int(input('Digite o seu ano de nascimento: '))
print(':-:' * 20)
today = date.today().year
age = today - born
print('A sua idade é de {}'.format(age))
if age < 10:
    print('A sua categoria é mirim!')
elif age < 15 and age > 9:
    print('A sua categoria é infantil!')
elif age < 20 and age > 14:
    print('A sua categoria é Junior!')
elif age < 26 and age > 19:
    print('A sua categoria é Sênior!')
else:
    print('A sua categoria é MESTRE!!!')







