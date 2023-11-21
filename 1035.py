N = input()
Valores = N.split()
#transformando em lista desse jeito podemos chamar os objetos dentro dessa lista
A = int(Valores[0])
B = int(Valores[1])
C = int(Valores[2])
D = int(Valores[3])
#agora temos 4 variáveis com a array dada
Teste1 = False
Teste2 = False
Teste3 = False
Teste4 = False

if B > C:
    Teste1 = True

if D > A:
    Teste2 = True

if (C + D) > (A + B):
    Teste3 =  True

if (C>=0) and (D>=0) and (A%2)== 0:
    Teste4 = True

#print(A,B,C,D)
#print(Teste1,Teste2,Teste3,Teste4)

if Teste1 and Teste2 and Teste3 and Teste4 == True:
    print("Valores aceitos")
else: print("Valores nao aceitos")

