n = float(input("Qual o salário do funcionário:R$ "))
if n <= 1250.00:
    print("Quem ganhava R${:.2f}, passa a ganhar R${:.2f}!".format(n,n+n*15/100))
else:
    print("Quem ganhava R${:.2f}, passa a ganhar R${:.2f}!".format(n,n+n*10/100))
    