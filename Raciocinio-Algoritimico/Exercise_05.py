# 01:

# soma = 0
# for contador in range(1, 11, 1):
# soma = contador + soma
# print(soma)

# 02:
# numero_inteiro = int(input("Digite um numero inteiro: "))
# multiplicação = 0
# for tabuada in range(0, 11, 1):
# multiplicação = numero_inteiro * tabuada
# print(multiplicação)


# 03:
# numero_inteiro = int(input("Digite um numero inteiro"))
# while numero_inteiro != 0:
# numero_inteiro = int(input("Digite um numero inteiro"))
# print(numero_inteiro)

# 04:
# contador = 0
# while contador == 10:
# numero_inteiro = int(input("Digite um numero inteiro"))
# if numero_inteiro > 0:
# print(numero_inteiro)
# contador += 1
# else:
# print("Número negativo")

# 05:
# numero_inteiro = int(input("Digite um número inteiro: "))
# fatorial = 1

# for numero_atual in range(1, numero_inteiro + 1, 1):
# fatorial = fatorial * numero_atual
# print(fatorial)

# print("O fatorial de", numero_inteiro, "é", fatorial)

# 05.2:
# contador = 0
# fatorial = 1

# numero = int(input("Digite um numero para calculo do fatorial = "))

# if numero >= 1:
# contador = numero
# while contador > 1:
# fatorial = fatorial * contador
# contador = contador - 1
# print("Fatorial = ", fatorial)
# elif numero == 0:
# print("Fatorial = ", fatorial)
# else:
# print("Numero negativo!")

# 06:
# contador = 1
# numero = int(input("Digite um numero inteiro "))

# while contador < 5:
# novo_numero = int(input("Digite um numero inteiro "))
# if novo_numero > numero:
# numero = novo_numero
# contador += 1
# print("O maior numero é ", numero)

# 07:

massa_inicial_material = float(input("Digite a massa em gramas do material: "))
massa_atual_material = massa_inicial_material
tempo_em_segundos = 0

while massa_atual_material >= 0.5:
    massa_atual_material = massa_atual_material / 2
    tempo_em_segundos = tempo_em_segundos + 50

print("Massa final em gramas do material é = ", massa_atual_material)
print("Tempo necessário em segundos para a massa chegar a esse valor é =",
      tempo_em_segundos)
