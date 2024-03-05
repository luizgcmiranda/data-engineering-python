# print()
# Para usar o comando print basta digitar print("Alguma coisa")

print("\n O print() é um comando para imprimir alguma coisa na sua frente, basta digitar print(alguma coisa). \n")
print("Inglês: Good morning")
print("Mandarim: 早上好 (Zǎoshang hǎo)")
print("Hindi: सुप्रभात (Suprabhaat)")
print("Espanhol: Buenos días")
print("Francês: Bonjour")
print("Árabe: صباح الخير (Sabah al-khair)")
print("Bengali: সুপ্রভাত (Suprobhat)")
print("Russo: Доброе утро (Dobroye utro)")
print("Português: Bom dia")
print("Indonésio Selamat pagi")
print("Urdu: صبح بخیر (Subha bakhair)")
print("Alemão: Guten Morgen")
print("Japonês: おはようございます (Ohayō gozaimasu)")
print("Punjabi: ਸਤ ਸ੍ਰੀ ਅਕਾਲ (Sat sri akal)")
print("Italiano: Buongiorno")


# Variáveis

a = 10
b = 5

#O f-string é um recurso do Python para a formatação de strings que permite a incorporação direta de expressões Python dentro de chaves {} em strings prefixadas com f. É uma maneira eficiente e legível de formatar strings.

print("\n Segue exemplos de modelos de operações ariméticas. \n")
print(f"A adição de {a} + {b} é: {a + b}")

# Exemplo de subtração
print(f"A subtração de {a} - {b} é: {a - b}")

# Exemplo de multiplicação
print(f"A multiplicação de {a} * {b} é: {a * b}")

# Exemplo de divisão
print(f"A divisão de {a} / {b} é: {a / b}")

# Exemplo de divisão inteira
print(f"A divisão inteira de {a} // {b} é: {a // b}")

# Exemplo de exponenciação
print(f"{a} elevado a {b} é: {a ** b}")

# Exemplo de módulo (resto da divisão)
print(f"O resto da divisão de {a} por {b} é: {a % b}")

print("\n O comando input() em Python é uma função incorporada usada para capturar dados de entrada do usuário. \n")
# Solicitando o nome do usuário
nome = input("Digite seu nome: ")

# Solicitando a idade do usuário
idade = input("Digite sua idade: ")

# Usando f-string para formatar e exibir uma mensagem personalizada
print(f"Olá {nome}, você tem {idade} anos!")