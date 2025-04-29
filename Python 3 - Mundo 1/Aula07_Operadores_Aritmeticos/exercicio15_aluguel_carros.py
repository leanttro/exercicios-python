n = int(input("Quantos dias alugados: "))
n1 = float(input("Quantos km percorridos: "))
s = n * 60 + n1 * 0.15
print("O total a pagar é R${:.2f}".format(s))