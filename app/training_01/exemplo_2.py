# 01.
print("\n 1. Crie um programa que o usuário digita o seu nome e retorna o número de caracteres. \n")

# Solicitando o nome do usuário
nome = input("Digite seu nome: ")

tamanho = len(nome)

# Usando f-string para formatar e exibir uma mensagem personalizada
print(f"Olá {nome}, o número de caracteres usando seu nome é {tamanho}!")

# 02.

print("\n 2. Crie um programa onde o usuário digite dois valores e apareça a soma. \n")

# Solicitando o primeiro valor ao usuário
valor_1 = input("Digite o seu primeiro valor: ")
valor_1_int = int(valor_1)

# Solicitando o segundo valor ao usuário
valor_2 = input("Digite o seu segundo valor: ")
valor_2_int = int(valor_2)

# Usando f-string para formatar e exibir uma mensagem personalizada
print(f"Olá usuário, a soma dos valores {valor_1_int} e {valor_2_int} é {valor_1_int + valor_2_int}!")


# 03.

#O programa deve começar solicitando ao usuário que insira seu nome.
#Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
#Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
#O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
#Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".

print("\n 3. Escreva um programa em Python que solicita ao usuário para digitar seu nome, \
o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve,\
então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do\
salário em comparação com o bônus recebido. \n")

BONUS = 1000

# Solicitando o nome
nome = input("Olá usuário, digite seu nome: ")

# Solicitando o valor salário mensal
valor_salario = input(f"Certo {nome}, agora digite o valor do seu salário mensal: ")
valor_salario_float = float(valor_salario)

# Solicitando o valor do bônus
valor_bonus = input(f"Baseado no seu salário de R$ {valor_salario}, agora digite o valor em porcentagem de seu bônus que deve receber: ")
valor_bonus_float = float(valor_bonus)

valor_bonus_calculado = BONUS + (valor_salario_float * valor_bonus_float)

# Usando f-string para formatar e exibir uma mensagem personalizada
print(f"Analisando as informações {nome}, utilizando seu salário R$ {valor_salario_float} e {valor_bonus_float}% do seu bônus, \
o seu valor bônus foi de R$ {valor_bonus_calculado:.2f}.")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# Nome: Validar se o nome é texto, se contem caracteres válidos e retirar números.
# Salário: Não pode ser negativo, muito alto, contendo apenas números.
# Bonus: Não pode ser negativo, contendo apenas números.