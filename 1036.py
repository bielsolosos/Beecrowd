#1036 beecrowd
from math import *
N = input('')
#convertendo
N = N.split()
A = float(N[0])
B = float(N[1])
C = float(N[2])

Delta = ((B*B) - (4*A*C))

#calculando as Raízes
if(A != 0 and Delta > -1):
    R1 = ((-B) + sqrt(Delta))/(2*A)
    R2 = ((-B) - sqrt(Delta))/(2*A)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))
else:
    print('Impossivel calcular')