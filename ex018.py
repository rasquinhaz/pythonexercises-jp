'''from math import (cos, sin, tan)
n = int(input('Digite aqui um valor para angulo:  '))
c = cos(n)
s = sin(n)
tg = tan(n)
print('O angulo de {}° tem resultado de \n COS - {:.2f}  \n SENO - {:.2f} \n TG - {:.2f} \n'.format(n,c,s,tg))'''
from math import sin,cos,tan,radians
an = float(input('Digite o valor do angulo: '))
c = cos(radians(an))
s = sin(radians(an))
tg = tan(radians(an))
print('O angulo de {}° tem resultado de \n COS - {:.3f}  \n SENO - {:.3f} \n TG - {:.3f} \n'.format(an, c, s, tg))






