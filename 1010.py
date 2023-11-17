r1=(str(input()))
r2=(str(input()))
#faz o split da str em cada elemento de uma lista.  
r1 = r1.split()
r2 = r2.split()

pr1 = float(r1[2])
pr2 = float(r2[2])

r1 = float(r1[1])
r2 = float(r2[1])

pag = ((pr1*r1)+(pr2*r2))
print("VALOR A PAGAR : R$ {:.2f}".format(pag))