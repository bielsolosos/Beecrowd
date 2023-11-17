A=float(input())
B=float(input())
C=float(input())
#Soma dos pesos
med=( ((A*2) + (B*3) + (C*5)) / (2+3+5) )
#concatenação de strs não funciona em todos os casos e o site não aceita fstring
print("MEDIA = {:.1f}".format(med))