n = float(input("Qual o preço do produto:R$"))
#n1 = n / 100
#n2 = n1*5
#n3 = n - n2
n4 = n - (n*5 /100)
print("O preço que custava R${:.2f} , na promoção com 5% de desconto, vai custar R${:.2f}".format(n,n4))