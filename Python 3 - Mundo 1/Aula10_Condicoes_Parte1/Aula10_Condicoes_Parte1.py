n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = (n1+n2)/2
print("PARABÉNS" if n3>=6 else "ESTUDE MAIS!")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = (n1+n2)/2
print("A sua média foi {:.2f}".format(n3))
if n3>=6:
    print("Sua média foi boa, parabéns!")
else:
    print("Sua média foi ruim, estude mais!")
print("Fim")

nome = str(input("Digite o seu nome: "))
if nome == "Leandro":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal, {}".format(nome))
print("Bom dia, {}!".format(nome))

nome = str(input("Digite o seu nome: "))
if nome == "Leandro":
    print("Que nome lindo você tem!")
print("Bom dia, {}!".format(nome))
