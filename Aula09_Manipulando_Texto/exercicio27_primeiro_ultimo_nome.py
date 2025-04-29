n = str(input('Qual o seu nome completo: ')).strip()
n1 = n.split()
print("Seu nome completo é {} e o primeiro nome é {} e o seu último nome é {}".format(n,n1[0],n1[len(n1)-1]))

n = str(input('Qual o seu nome completo: ')).strip()
n1 = n.split()
print("Seu último nome é {}".format(n1[len(n1)-1]))
