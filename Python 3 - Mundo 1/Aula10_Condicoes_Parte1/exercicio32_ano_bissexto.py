from datetime import date
n = int(input("Qual ano você quer analisar? Coloque [0] para analisar o ano atual: "))
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("O ano {} é BISSEXTO!".format(n))
else:
    print("O ano {} não é BISSEXTO!".format(n))
