print("\n TypeError, Type Check e Type Conversion \n")

# TypeError
try:
    resultado = len(5)
except TypeError as incorreto:
    print(incorreto)

# TypeCheck
    
numero = 10
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")


# TypeConversion
numero_inteiro = 5
numero_flutuante = 2.5
soma = float(numero_inteiro) + numero_flutuante
print(soma)


print("\n 21. Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, \
utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida. \n")

try:
    valor = float(input("Digite o valor da temperatura em Celsius: "))
    print(f"Olá usuário, o valor {valor} celsius é igual a {(valor * 9/5) + 32} fahrenheit!")
except ValueError:
    print(f"Olá usuário, o valor inserido não é númerico e não pode ser transformado em fahrenheit!")

print("\n 22. Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). \
Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada. \n")

valor = str(input("Digite uma frase ou uma palavra: "))

if isinstance(valor, str):
    valor_reparado = valor.replace(" ", "").strip()
    teste = valor_reparado[::-1]
    if valor_reparado == valor_reparado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

print("\n 23. Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. \
Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada. \n")

valor_1 = float(input("Digite o seu primeiro valor: "))
valor_2 = float(input("Digite o seu segundo valor: "))
operador = input("Digite o seu operador (+ / - *): ").strip()

try:
    if isinstance(valor_1, float) and isinstance(valor_2, float):
        if operador == "+":
            print(f"Olá usuário, a soma dos valores {valor_1} e {valor_2} é {valor_1 + valor_2}!")
        elif operador == "-":
            print(f"Olá usuário, a subtração dos valores {valor_1} e {valor_2} é {valor_1 - valor_2}!")
        elif operador == "*":
            print(f"Olá usuário, a multiplicação dos valores {valor_1} e {valor_2} é {valor_1 * valor_2}!")
        elif operador == "/":
            print(f"Olá usuário, a divisão dos valores {valor_1} e {valor_2} é {valor_1 / valor_2}!")
        else:
            print(f"Olá usuário, você inseriu incorretamente o seu operador!")
except ValueError:
    print(f"Olá usuário, você inseriu incorretamente os seus valores!")
else:
    print(f"Até a próxima!")
finally:
    print("Acabou!")

print("\n 24. Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica \
e utilize if-elif-else para classificar o número como positivo, negativo ou zero. Adicionalmente, identifique se o número é par ou ímpar. \n")

try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

print("\n 25. Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. \
Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, \
imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros. \n")

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")