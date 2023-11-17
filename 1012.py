Valores = input("")
lista = Valores.split()
area_triang = ((float(lista[0])*float(lista[2]))/2)
area_raio = (3.14159 * (float(lista[2])**2)) #aparentemente bateu (tinha q fazer um round...)
area_trapezio = (( (float(lista[0]) + float(lista[1])) * float(lista[2]))/2) #bateu
area_quadrado = (float(lista[1])**2)
area_triangr = ((float(lista[0]) *   float(lista[1])))

print("TRIANGULO: {:.3f}".format(area_triang))
print('CIRCULO: {:.3f}'.format(area_raio))
print('TRAPEZIO: {:.3f}'.format(area_trapezio))
print('QUADRADO: {:.3f}'.format(area_quadrado))
print('RETANGULO: {:.3f}'.format(area_triangr))
