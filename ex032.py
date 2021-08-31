from time import sleep
from datetime import date
a = int(input('Digite um ano aqui ---> (Se quiser o ano atual digite 0! --> '))
if a == 0:
    a = date.today().year
print(':->'*20)
sleep(1)
print('Processando os dados recebidos ... ... ... ...')
sleep(1)
if (a%4) ==0 and a%100!= 0 or a % 400 == 0:
    print('O ano digitado é bissexto!!')
else:
    print('O ano digitado é um ano normal de 365 dias!')
print(':->'*24)
