print("\n Inteiros (int) \n")
#

print("\n 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário. \n")

valor_1 = int(input("Digite o seu primeiro valor: "))
valor_2 = int(input("Digite o seu segundo valor: "))
print(f"Olá usuário, a soma dos valores {valor_1} e {valor_2} é {valor_1 + valor_2}!")
#

print("\n 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5. \n")

valor_1 = int(input("Digite um número: "))
valor_2 = (valor_1 % 5)
print(f"Olá usuário, o número digitado foi {valor_1} e o resto da divisão desse número por 5 é {valor_2}!")
#

print("\n 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado. \n")

valor_1 = int(input("Digite o seu primeiro valor: "))
valor_2 = int(input("Digite o seu segundo valor: "))
print(f"Olá usuário, a multiplicação dos valores {valor_1} e {valor_2} é {valor_1 * valor_2}!")
#

print("\n 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo. \n")

valor_1 = int(input("Digite o seu primeiro valor: "))
valor_2 = int(input("Digite o seu segundo valor: "))
print(f"Olá usuário, a divisão dos valores {valor_1} e {valor_2} é {valor_1 // valor_2}!")


print("\n 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário. \n")

valor_1 = int(input("Digite um número: "))
valor_2 = (valor_1 ** 2)
print(f"Olá usuário, o número digitado foi {valor_1} e o quadrado desse número é {valor_2}!")

print("\n Flutuante (float) \n")
#

print("\n 6.  Escreva um programa que receba dois números flutuantes e realize sua adição. \n")

valor_1 = float(input("Digite o seu primeiro valor: "))
valor_2 = float(input("Digite o seu segundo valor: "))
print(f"Olá usuário, a soma dos valores {valor_1} e {valor_2} é {valor_1 + valor_2}!")

print("\n 7.  Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário. \n")

valor_1 = float(input("Digite o seu primeiro valor: "))
valor_2 = float(input("Digite o seu segundo valor: "))
print(f"Olá usuário, a média dos valores {valor_1} e {valor_2} é {(valor_1 + valor_2) / 2}!")

print("\n 8.  Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário). \n")

valor_1 = float(input("Digite um valor: "))
valor_2 = float(input("Digite um valor da sua potência/expoente: "))
print(f"Olá usuário, a potência do seu número {valor_1} é {valor_1 ** valor_2}!")

print("\n 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit. \n")

valor_1 = float(input("Digite um valor celsius: "))
print(f"Olá usuário, o valor {valor_1} celsius é igual a {(valor_1 * 9/5) + 32} fahrenheit!")


print("\n 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada. \n")

valor_1 = float(input("Digite um valor de raio: "))
print(f"Olá usuário, baseado no valor {valor_1} de raio, a área calculada é igual a {3.14159 * valor_1 ** 2}!")

print("\n Strings (string) \n")

print("\n 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas. \n")

valor_1 = str(input("Olá, digite um valor: ")).upper()
print(f"Olá usuário, você digitou {valor_1}!")

print("\n 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas. \n")

valor_1 = str(input("Olá, digite o seu nome completo: ")).lower()
print(f"Olá usuário, você digitou {valor_1}.")

print("\n 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final. \n")

valor_1 = str(input("Olá, digite uma frase: ")).strip()
print(f"Olá usuário, você digitou {valor_1}.")

print("\n 14. Faça um programa que peça ao usuário para digitar uma data no formato dd/mm/aaaa e, em seguida, imprima o dia, o mês e o ano separadamente. \n")

valor_1, valor_2, valor_3 = str(input("Olá, digite uma data no formato dd/mm/aaaa: ")).split('/')
print(f"Olá usuário, você digitou dia {valor_1}, mês {valor_2} e ano de {valor_3}.")

print("\n 15. Escreva um programa que concatene duas strings fornecidas pelo usuário. \n")

valor_1 = str(input("Digite o seu primeiro valor: "))
valor_2 = str(input("Digite o seu segundo valor: "))
print(f"Olá usuário, a concatenação dos valores {valor_1} e {valor_2} é {valor_1 + valor_2}!")

print("\n Booleanos (bool) \n")

print("\n 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas. \n")

valor_1 = True
valor_2 = False
print(f"Olá usuário, a expressão booleana dos valores {valor_1} e {valor_2} é {valor_1 and valor_2}!")


print("\n 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR. \n")

valor_1 = True
valor_2 = False
print(f"Olá usuário, a expressão booleana dos valores {valor_1} e {valor_2} é {valor_1 or valor_2}!")


print("\n 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor. \n")

valor_1 = input("Digite o seu primeiro valor booleano: ")
valor_2 = not valor_1
print(f"Olá usuário, a expressão booleana do valor inserido é {valor_1} e o inverso é {valor_2}!")


print("\n 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais. \n")

valor_1 = int(input("Digite o seu primeiro valor: "))
valor_2 = int(input("Digite o seu segundo valor: "))
print(f"Olá usuário, os valores digitados foram {valor_1} e {valor_2} e a comparação deles serem iguais é {valor_1 == valor_2}!")


print("\n 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes. \n")

valor_1 = int(input("Digite o seu primeiro valor: "))
valor_2 = int(input("Digite o seu segundo valor: "))
print(f"Olá usuário, os valores digitados foram {valor_1} e {valor_2} e a comparação deles serem diferentes é {valor_1 != valor_2}!")