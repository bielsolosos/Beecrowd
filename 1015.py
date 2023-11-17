from math import *
x = input()
y = input()

x = x.split()
y = y.split()

dist = (sqrt((( ( float(y[0])-float(x[0]) )**2) + (( ( float(y[1])-float(x[1]) ) )**2)) ))
print("{:.4f}".format(dist))