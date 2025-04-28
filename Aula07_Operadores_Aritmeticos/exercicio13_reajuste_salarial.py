s = float(input("Qual o salário do funcionário: R$"))
u = s + (s*15/100)

print("O salário do funcionário, que é atualmente R${:.2f}, com 15% de aumento ficará {:.2f}".format(s,u))