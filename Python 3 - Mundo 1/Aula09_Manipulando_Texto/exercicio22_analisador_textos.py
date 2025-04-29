n = str(input("Digite seu nome completo: ")).strip()
print("{} \n{} \n{} \n{} letras".format(n,n.upper(),n.lower(), len(n)-n.count(" ")))
s = n.split()
print("Seu nome completo é {} e o primeiro nome é {} e tem {} letras".format(n,s[0],len(s[0])))
print("Seu primeiro nome tem {} letras".format(n.find(" ")))





