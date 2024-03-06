print("\n 1. Inteiros \n")
print("+ - * // %")

print("\n 2. Flutuantes \n")
print("+ - * / **")

print("\n 3. Strings \n")
print("+, *, [], [:], find, replace, split, join, strip, upper, \
lower, title, startswith, endswith, isdigit, isalpha, isspace, islower, isupper")
print("Exemplos práticos:")

# +
concatenado = "GitHub " + "Codespaces!"
print(concatenado)

# *
repetido = "Possivelmente vou repetir várias vezes;" * 3
print(repetido)

# [Indexação]
primeiro_char = "GitHub"[0]
print(primeiro_char)

# Fatia
substring = "Hello, world!"[7:12]
print(substring)

# find()
indice = "Hello, world!".find("world")
print(indice)

# replace()
substituido = "Hi, world!".replace("world", "Python")
print(substituido)

# split()
dividido = "Data, science!".split(", ")
print(dividido)

# join()
juntado = ", ".join(["Data", "Engineer!"])
print(juntado)

# strip()
sem_espacos = "   Architeture, data!   ".strip()
print(sem_espacos)

# upper()
maiuscula = "Excelente trabalho, funcionáriO!".upper()
print(maiuscula)

# lower()
minuscula = "Hello, WORLD!".lower()
print(minuscula)

# title()
titulo = "Tema para TiTuLo!".title()
print(titulo)

# startswith()
comeca_com = "Hello, world!".startswith("Hello")
print(comeca_com)

# endswith()
termina_com = "Hello, world!".endswith("world!")
print(termina_com)

# isdigit()
digitos = "12345".isdigit()
print(digitos)

# isalpha()
alfabetico = "abc".isalpha()
print(alfabetico)

# isspace()
espacos = "   ".isspace()
print(espacos)

# islower()
minusculas = "hello".islower()
print(minusculas)

# isupper()
maiusculas = "HELLO".isupper()
print(maiusculas)


print("\n 4. Booleanos \n")
print("and, or, not, ==, !=, >, <, >=, <=")