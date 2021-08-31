from time import sleep
v = int(input('Digite a distancia da viagem em Km: '))
p = (v*0.50)
pl = (v*0.45)
print('Processando dados... ... ... ')
sleep(2)
if v <= 200:
    print('Você deverá pagar o valor de : R${:.2f}'.format(p))
else:
    print('Você deverá pagar o valor de: R${:.2f}'.format(pl))
print(':-:'*23)


