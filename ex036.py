casa = int(input('Qual é o valor da casa: '))
salario = int(input('Qual é o salário do comprador: '))
anos = int(input('Em quantos anos irá pagar: '))

#Calcule o valor da prestação, sabendo que ela não pode ultrapassar 30% do salário ou então o empréstimo será negado.
prestação = casa / (anos * 12)
mínimo = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('O EMPRESTIMO FOI CONCEDIDO ')
else:
    print('O EMPRESTIMO FOI NEGADO')






