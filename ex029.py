from time import sleep
c = float(input('digite a velocidade do carro em Km/h: '))
print(':-:'*20)
print('Processando dados! ... ... ...  ')
sleep(3)
if c <= 80:
    print('Muito bem continue assim! Esse é o comportamento que queremos no transito...')
    print('Tenha um ótimo dia!')
else:
    print('Você acaba de ser multado! :-|| --, Você deverá pagar ao banco o valor de \n {:.2f}$'.format((c - 80)* 7))
