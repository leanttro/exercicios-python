n = int(input("Primeiro valor: "))
n1 = int(input("Segundo valor: "))
n2 = int(input("Terceiro valor: "))

if n > n1 and n > n2:
    maior = n
if n1 > n and n1 > n2:
    maior = n1
if n2 > n and n2 > n1:
    maior = n2
if n < n1 and n < n2:
    menor = n
if n1 < n and n1 < n2:
    menor = n1
if n2 < n and n2 < n1:
    menor = n2
print("O maior número é {}".format(maior))
print("O menor número é {}".format(menor))
