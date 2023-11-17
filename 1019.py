#1019.py
#ainda em depressão
N=int(input(''))
#criando as variáveis
horas = 0
minutos = 0
segundos = 0

if N >= 3600:
    while N >= 3600:
        horas += 1
        N -= 3600

if N >= 60:
    while N >= 60:
        minutos += 1
        N -= 60

segundos = N

print("{}:{}:{}".format(horas,minutos,segundos))