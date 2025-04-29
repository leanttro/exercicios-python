n = str(input("Digite uma frase: ")).upper().strip()
print("A letra 'a' apareceu {} vezes".format(n.count("A")))
print("A primeira letra 'a' apareceu na posição {}".format(n.find("A")+1))
print("A última letra 'a' apareceu na posição {}".format(n.rfind("A")+1))