# Exercise 01:

# numero = input("Digite seu número de celular: ")

# if numero[0] == "4" and numero[1] == "1":
# print("É um número de Curitiba")
# else:
# print("Não é um número de Curitiba")

# Exercise 02:

# salarios = []

# for cont in range(12):
# salario_mes = int(
# input("Digite seu salário de cada mês respectivamente: "))
# salarios.append(salario_mes)

# Calcular a média dos salários
# media_salarios = sum(salarios) / len(salarios)

# print("Média de salário recebido:", media_salarios)

# Imprimir os valores abaixo da média
# print("Valores abaixo da média:")
# for salario in salarios:
# if salario < media_salarios:
# print(salario)

# Exercise 03:

# Biblioteca random
# import random

# Gera um Captcha de 6 caracteres
# captcha = []
# for caracteres in range(6):
# random choice escolhe um elemento aleatório de um sequencia de elementos.
# random_caracter = random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
# captcha.append(random_caracter)
# ''.join faz a concatenação de strings
# captcha = ''.join(captcha)

# Exibe o Captcha gerado
# print("Captcha gerado:", captcha)

# Solicita ao usuário que digite a resposta
# user_answer = input("Digite o captcha: ")

# Valida a resposta fornecida pelo usuário
# if captcha == user_answer:
# print("Captcha válido!")
# else:
# print("Captcha inválido.")

# Exercise 04:

string = input("Digite uma palavra: ")
n_gramas = []
bi_gramas = []
bi_gramas_unico = []

for n_grama in string:
    n_gramas.append(n_grama)

print(n_gramas)

for cont in range(len(string) - 1):
    bi_grama = n_gramas[cont] + n_gramas[cont+1]
    bi_gramas.append(bi_grama)

print(bi_gramas)

for bi_grama in bi_gramas:
    if bi_gramas.count(bi_grama) == 1:
        bi_gramas_unico.append(bi_grama)

print(bi_gramas_unico)
print("A quantidade de bi-gramas únicos é =", len(bi_gramas_unico))
