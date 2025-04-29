l = float(input("Largura da parede(m): "))
a = float(input("Altura da parede(m): "))
m = l * a
t = m * 1/2

print("Sua parede tem a dimensão de {} x {}, a área é de {}. \nPara pintar essa parede, você precisa de {} litros de tinta".format(l,a,m,t))

l = float(input("Largura da parede(m): "))
a = float(input("Altura da parede(m): "))
m = l * a
print("Sua parede tem a dimensão de {:.2f} x {:.2f}, a área é de {:.2f}. \nPara pintar essa parede, você precisa de {:.2f} litros de tinta".format(l,a,m,(l*a) * 1/2))