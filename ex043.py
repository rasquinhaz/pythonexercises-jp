print('    \033[1;36m CÁLCULO DO IMC\033[m   ')
print(':-:' * 20)
cores = {'vermelho': '\033[1;31m',
         'limpa': '\033[m',
         'azul': '\033[1;34',
         'amarelo': '\033[1;33m',
         'branco': '\033[1;97m',
         'preto': '\033[1;30m',
         'verde': '\033[1;32m'}
a = float(input('Qual é a sua altura? '))
p = float(input('Qual é o seu peso (Kg)? '))

imc = p / (a ** 2)
print('=' * 27)
print('O seu IMC é igual a {:.1f}'.format(imc))

if imc < 18.6:
    print(" {}O seu IMC é considerado ABAIXO DO PESO!{}".format(cores['vermelho'], cores['limpa']))
    print('{}Recomendamos que procure um médico nutricionista para avaliar o seu caso em específico!{}'.format(cores['branco'], cores['limpa']))
elif imc > 18.6 and imc < 25.1:
    print('{} O seu IMC é considerado IDEIAL!{}'.format(cores['verde'], cores['limpa']))
    print('{}Continue cuidado da sua saúde! A alimentação é muito importante para ela.{}'.format(cores['branco'], cores['limpa']))
elif imc > 24.9  and imc < 30.1:
    print('O seu IMC é considerado como SOBREPESO!')
    print('Recomendamos que faça uma avaliação com um profissional da saúde.')
elif imc > 30 and imc < 40.1:
    print('O seu IMC é considerado como Obesidade!')
elif imc >= 40:
    print('O seu IMC é considerado como OBESIDADE MÓRBIDA!!!!!')


