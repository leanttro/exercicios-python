frase = 'Curso em Vídeo Python'
print(frase[4:13])

frase = 'Curso em Vídeo Python'
print(frase[:13])

frase = 'Curso em Vídeo Python'
print(frase[4:])

frase = 'Curso em Vídeo Python'
print(frase[::2])

n = "Leandro Andrade é um aluno de Ia Também é aluno de programação Tem interesse em Power Bi"
print(n.upper().count("O"))

n = "Leandro Andrade é um aluno de Ia Também é aluno de programação Tem interesse em Power Bi"
print(len(n))
print(n.upper().count("O"))

n = "    Leandro Andrade é um aluno de Ia Também é aluno de programação Tem interesse em Power Bi   "
print(len(n.strip()))

n = "Leandro Andrade é um aluno de Ia Também é aluno de programação Tem interesse em Power Bi"
print(n.replace("Leandro","João"))

print(n)
n = print(n.replace("Leandro Andrade","João"))
print("Curso" in frase)

frase = 'Curso em Vídeo Python'
print(frase.find("Python"))

frase = 'Curso em Vídeo Python'
print(frase.lower().find("python"))

frase = 'Curso em Vídeo Python'
print(frase.split())

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0])

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0][2])