n = int(input("Quantos km tem a viagem: "))
if n<200:
    print("Você está prestes a fazer uma viagem de {}km!\nO valor da passagem é R${:.2f}".format(n,n*1/2))
else:
    print("Você está prestes a fazer uma viagem de {}km!\nO valor da passagem é R${:.2f}".format(n,n*0.45))
print("Fim")