import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# num_1 = int(input("Digite um número inteiro: "))
# num_2 = int(input("Digite outro número inteiro: "))
# soma = num_1 + num_2
# print(f"A soma dos números {num_1} e {num_2} é {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da 
# divisão desse número por 5.

# CONSTANTE_DIVISAO = 5 
# num_1 = int(input("Digite um número: "))
# resto_divisao = num_1 % CONSTANTE_DIVISAO
# print(f"O resto da divisão de {num_1} por {CONSTANTE_DIVISAO} é {resto_divisao}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e 
# mostre o resultado.

# num_1 = int(input("Digite um número inteiro: "))
# num_2 = int(input("Digite outro número inteiro: "))
# multiplicacao = num_1 * num_2
# print(f"A multiplicação dos números {num_1} e {num_2} é {multiplicacao}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# num_1 = int(input("Digite um número inteiro: "))
# num_2 = int(input("Digite outro número inteiro: "))
# divisao = num_1 // num_2
# print(f"A divisão inteira dos números {num_1} e {num_2} é {divisao}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# num_1 = int(input("Digite um número: "))
# quadrado = num_1  ** 2
# print(f"O quadrado de {num_1} é {quadrado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# num_1 = float(input("Digite um número: "))
# num_2 = float(input("Digite outro número: "))
# soma = num_1 + num_2
# print(f"A soma dos números {num_1} e {num_2} é {soma}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# num_1 = float(input("Digite um número: "))
# num_2 = float(input("Digite outro número: "))
# media = (num_1 + num_2) / 2 
# print(f"A média dos números {num_1} e {num_2} é {media}")

# 8. Desenvolva um programa que calcule a potência de um número 
# (base e expoente fornecidos pelo usuário).

# num_1 = float(input("Digite um número: "))
# num_2 = float(input("Digite um número expoente: "))
# potencia = num_1 ** num_2
# print(f"O número {num_1} elevado a {num_2} é {potencia}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# temp_celsius = float(input("Digite uma temperatura em Celsius: "))
# temp_fahrenheit = temp_celsius * 1.8 + 32
# temp_fahrenheit_arredondada = round(temp_fahrenheit,2)
# print(f"A temperatura {temp_celsius} graus Celsius é igual a {temp_fahrenheit_arredondada} graus Fahreinheit.")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio = float(input("Digite um valor para o Raio do círculo: "))
# area = math.pi * raio ** 2
# print(f"A área  de um círculo com {raio} é de {area}.")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# string = input("Digite uma string: ")
# string_upper = string.upper()
# print(string_upper)

# 12. Crie um programa que receba o nome completo do usuário e 
# imprima o nome com todas as letras minúsculas.

# nome_usuario = input("Digite seu nome completo: ")
# nome_usuario_lower = nome_usuario.lower()
# print(nome_usuario_lower)

# 13. Desenvolva um programa que peça ao usuário para inserir 
# uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Digite uma frase: ")
# frase_limpa = frase.strip()
# print(frase_limpa)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, 
# em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Digite uma data no formato 'dd/mm/aaaa': ")
# data_separada = data.split("/")
# print(data_separada[0])
# print(data_separada[1])
# print(data_separada[2])

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# str_1 = input("Digite uma string: ")
# str_2 = input("Digite uma outra string: ")
# str_3 = str_1 + str_2
# print(str_3)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo 
# usuário e retorne o resultado da operação AND entre elas.

# exp_1 = bool(input("Digite 'True' ou 'False': "))
# exp_2 = bool(input("Digite 'True' ou 'False': "))
# resultado = exp_1 and exp_2 
# print("Resultado do AND lógico:", resultado)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne
#  o resultado da operação OR.

# exp_1 = bool(input("Digite 'True' ou 'False': "))
# exp_2 = bool(input("Digite 'True' ou 'False': "))
# resultado = exp_1 or exp_2 
# print("Resultado do OR lógico:", resultado)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano
#  e, em seguida, inverta esse valor.

# exp_1 = bool(input("Digite 'True' ou 'False': "))
# resultado_invertido = not exp_1
# print("Resultado do OR lógico: ", resultado_invertido)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# num_1 = input("Digite um número: ")
# num_2 = input("Digite outro número: ")
# igualdade = num_1 == num_2
# print(f"O resultado da igualdade é: {igualdade}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# num_1 = input("Digite um número: ")
# num_2 = input("Digite outro número: ")
# diferenca = num_1 != num_2
# print(f"O resultado da diferença é: {diferenca}")

# #### try-except e if

# 21: Conversor de Temperatura

# try:
#     temp_celsius = float(input("Digite uma temperatura em Celsius: "))
#     temp_fahrenheit = temp_celsius * 1.8 + 32
#     temp_fahrenheit_arredondada = round(temp_fahrenheit,2)
#     print(f"A temperatura {temp_celsius} graus Celsius é igual a {temp_fahrenheit_arredondada} graus Fahreinheit.")
# except:
#     print("Digite um número para que haja conveersão.")

# 22: Verificador de Palíndromo

# try:
#     string_1 = input("Digite uma palavra ou frase: ")
#     string_2 = string_1.replace(" ","")
#     string_3 = string_2.replace(".","")
#     string_4 = string_3.replace(",","")
#     string_reversa = string_4[::-1]
#     resultado = string_4 == string_reversa
#     print(f"É Palíndromo? {resultado}")
# except:
#     print("Digite uma palavra ou frase.")

# 23: Calculadora Simples

# try:
#     num_1 = int(input("Digite um número: "))
#     num_2 = int(input("Digite outro número: "))
#     op = str(input("Digite um dos seguintes operadores (+, -, *, /): "))
#     if op == "+":
#         resultado = num_1 + num_2
#         print(f"O resultado da soma é: {resultado}")
#     elif op == "-":
#         resultado = num_1 - num_2
#         print(f"O resultado da subtração é: {resultado}")
#     elif op == "*":
#         resultado = num_1 * num_2
#         print(f"O resultado da multiplicação é: {resultado}")
#     elif op == "/":
#         resultado = num_1 / num_2
#         print(f"O resultado da divisão é: {resultado}")
# except ZeroDivisionError:
#     print("Não é possível dividir um número por zero.")
# except:    
#     print("Digite uma entrada válida.")

# 24: Classificador de Números

# try:
#     num = int(input("Digite um número: "))
#     if num == 0:
#         print ("Zero.")
#     elif num > 0:
#         if (num % 2) ==  0:
#             print ("Positivo e Par.")
#         else:
#             print ("Positivo e Ímpar.")
#     else:
#         print ("Negativo.")
# except:
#     print("Entrada inválida!")

# 25: Conversão de Tipo com Validação


# lista = input("Digite uma lista de números separados por vírgula: ")
# lista_str = lista.split(",")
# lista_int=[]

# try:
#     for item in lista_str:
#         lista_int.append(int(item.strip()))
#     print(f"Lista de inteiros: {lista_int}.")
# except:
#     print("Digite apenas números e vírgulas.")    
