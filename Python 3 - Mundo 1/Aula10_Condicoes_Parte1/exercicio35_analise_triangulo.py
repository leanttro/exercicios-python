print("="*30)
print("Analisador de triângulos")
(print("="*30))
n = float(input("Primeiro lado: "))
n1 = float(input("Segundo lado: "))
n2 = float(input("Terceiro lado: "))

if n < n1 + n2 and n1 < n2 + n and n2 < n1 + n:
    print("É possível formar um triângulo!")
else:
    print("Não é possível formar um triângulo!")