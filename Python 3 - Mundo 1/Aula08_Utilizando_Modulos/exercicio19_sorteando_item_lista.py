from random import choice 
n = input('Primeiro aluno: ')
n1 = input('Segundo aluno: ')
n2 = input('Terceiro aluno: ')
n3 = input('Quarto alunio: ')
l = [n, n1, n2, n3]
n4 = choice(l)

print('O aluno escolhido foi {}'.format(n4))
