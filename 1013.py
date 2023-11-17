def ehmaior(a,b):
    maior = (((a+b)+(abs(a-b)))/2)
    return maior

numeros = input('digite 3 numeros ')
numeros = numeros.split()
#transforma em lista os números recebidos
Maior1 = ehmaior(int(numeros[0]),int(numeros[1]))
Maior2 = ehmaior(int(numeros[1]),int(numeros[2]))

Maior = int(ehmaior(Maior1,Maior2))
print(Maior,"eh o maior")
