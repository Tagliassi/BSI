# Exercise 01:

numero = input("Digite seu número de celular: ")

if numero[0] == "4" and numero[1] == "1":
    print("É um número de Curitiba")
else:
    print("Não é um número de Curitiba")

# Exercise 02:

salarios = [2500, 3000, 2800, 3200, 2700, 2600, 2900, 3100, 2800, 3000, 2600, 2700]

for cont in range(12):
    salario_mes = int(input("Digite seus salarios:"))
    salarios.append(salario_mes)

# Calcular a média dos salários
media_salarios = sum(salarios) / len(salarios)

print("Média de salário recebido:", media_salarios)

# Imprimir os valores abaixo da média
print("Valores abaixo da média:")
for salario in salarios:
    if salario < media_salarios:
        print(salario)
