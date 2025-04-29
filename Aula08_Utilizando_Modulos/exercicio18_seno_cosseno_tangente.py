import math
n = float(input('Digite o ângulo desejado: '))
n1 = math.sin(math.radians(n))
n2 = math.cos(math.radians(n))
n3 = math.tan(math.radians(n))
print("O seno de {} é {:.2f} \nO cosseno de {} é {:.2f} \nA tangente de {} é {:.2f}".format(n,n1,n,n2,n,n3))