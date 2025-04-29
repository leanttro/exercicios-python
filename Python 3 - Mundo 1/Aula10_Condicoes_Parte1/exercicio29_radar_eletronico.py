n = int(input("Qual a velocidade do carro: "))
n1 = (n - 80)*7

if n>80:
    print("MULTADO!V Você excedeu o limite de segurança que é de 80km/h! \nVocê deve pagar uma multa de R${:.2F}.".format(n1))
else:
    print("Tenha um bom dia! Dirija com segurança!")