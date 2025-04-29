n = int(input("Informe um número: "))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print("Analisando o número: {}".format(n))
print("Milhar: {}".format(m))
print("Dezena: {}".format(c))
print("Centena: {}".format(d))
print("Unidade: {}".format(u))

n = int(input("Informe um número: "))
n = str(n)
print("Analisando o número: {}".format(n))
print("Milhar: {}".format(n[0]))
print("Dezena: {}".format(n[1]))
print("Centena: {}".format(n[2]))
print("Unidade: {}".format(n[3]))
