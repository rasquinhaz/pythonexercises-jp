d = float(input('Digite o número de dias que foi alguado o carro: '))
km = float(input('Digite o número de km que foi percorrido: '))
tp = 60*d+(km*0.15)
print('Com {} dias alugando o carro e {}km percorridos nele, você devera pagar: R${}'.format(d,km,tp))

