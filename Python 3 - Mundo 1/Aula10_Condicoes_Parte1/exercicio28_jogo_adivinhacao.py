from random import randint
from time import sleep
n = randint(0,5)
print("========================================================================")
print("        Vou pensar em um número de 0 - 5. Tente advinhar qual!:)        ")
print("========================================================================")
n1 = int(input("Qual o número eu pensei: "))
print("PROCESSANDO...")
sleep(1)
if n1 == n:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("Ganhei! Eu pensei no número {} e não no {}!".format(n,n1))