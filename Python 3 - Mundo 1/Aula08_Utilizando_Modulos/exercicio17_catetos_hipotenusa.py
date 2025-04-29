import math
n = float(input('Comprimento do cateto oposto: '))
n1 = float(input('Comprimento do cateto adjacente: '))
n2 = math.hypot(n,n1)
print("A hipotenusa do cateto oposto {} e do cateto adjacente {} é {:.2f}".format(n,n1,n2))
