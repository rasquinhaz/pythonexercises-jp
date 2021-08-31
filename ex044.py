print('============ LOJA DE COMPRAS ================')
valor = float(input('Valor das compras: R$ - '))
print('FORMAS DE PAGAMENTO\n [ 1 ] À vista/cheque\n [ 2 ] À vista no cartão\n [ 3 ] 2x no cartão\n [ 4 ] 3x ou mais no cartão')
forma = int(input('Qual é a sua forma de pagamento? '))
desconto = valor - (valor * 10) /100
desconto2 = valor - (valor * 5) /100


if forma == 1:
    print('O valor das compras á vista/cheque fica R$ - {:.2f}'.format(desconto))
elif forma ==2:
    print('O valor das compras à vista no cartão fica R$ = {:.2f}'.format(desconto2))
elif forma == 3:
    print('O valor das compras em até 2x no cartão fica R$ = {:.2f}'.format(valor))
elif forma == 4:
    par = int(input('Em quantas parcelas? '))
    juros = valor + (valor * 20/100)
    parcela = juros / par
    tt = print('A sua compra sera parcelada {}x de R${:.2f} '.format(par, parcela))
    print('A sua compra de {} ficará {:.2f} como juros aplicado.'.format(valor, juros))






