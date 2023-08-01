# Exercise 01

# caracteres_minuto = int(input("Digite a quantidade de caracteres que você digita por minuto: "))
# caracteres_hora = caracteres_minuto * 60
# pagina = 1000
# numero_paginas_hora = caracteres_hora/pagina
# print("O número de páginas que você escreve por hora é igual a",numero_paginas_hora, "pagina(s)")

# Exercise 02

# numero_viagens_aviao_p = 0
# numero_viagens_aviao_m = 0
# numero_viagens_aviao_g = 0
# soma_aviao_p = 0
# soma_aviao_m = 0
# soma_aviao_g = 0

# for numero_viagens_total in range(0, 10, 1):

# print("Digite o tipo de avião que realizou a viagem")
# tipo_aviao = int(
# input("1) Avião pequeno, 2) Avião médio ou 3) Avião grande: "))

# while tipo_aviao <= 0 or tipo_aviao > 3:
# tipo_aviao = int(input("1) Avião pequeno, 2) Avião médio ou 3) Avião grande "))

# if tipo_aviao == 1:
# tempo_viagem_avião_p = int(input("Digite o tempo da viagem em minutos: "))
# soma_aviao_p = soma_aviao_p + tempo_viagem_avião_p
# numero_viagens_aviao_p = numero_viagens_aviao_p + 1
# elif tipo_aviao == 2:
# tempo_viagem_avião_m = int(input("Digite o tempo da viagem em minutos: "))
# soma_aviao_m = soma_aviao_m + tempo_viagem_avião_m
# numero_viagens_aviao_m = numero_viagens_aviao_m + 1
# else:
# tempo_viagem_avião_g = int(input("Digite o tempo da viagem em minutos: "))
# soma_aviao_g = soma_aviao_g + tempo_viagem_avião_g
# numero_viagens_aviao_g = numero_viagens_aviao_g + 1

# tempo_medio_aviao_p = soma_aviao_p/numero_viagens_aviao_p
# tempo_medio_aviao_m = soma_aviao_m/numero_viagens_aviao_m
# tempo_medio_aviao_g = soma_aviao_g/numero_viagens_aviao_g

# print("O tempo médio por tipo de avião é:")
# print("Avião pequeno =", tempo_medio_aviao_p)
# print("Avião médio =", tempo_medio_aviao_m)
# print("Avião grande =", tempo_medio_aviao_g)

# Exercise 03

# valor_produto = float(input("Digite o valor do produto: "))

# while valor_produto < 0:
# valor_produto = float(input("Digite o valor do produto: "))

# valor_tres_parcelas = valor_produto/3
# print("O valor do produto para pagamento em três parcelas é igual a:",valor_tres_parcelas)

# Exercise 04

nota_recebida = int(input("Digite a nota recebida entre 0 e 100: "))

while nota_recebida < 0 or nota_recebida > 100:
    nota_recebida = int(input("Digite a nota recebida entre 0 e 100: "))

if nota_recebida == 0:
    print("Conceito E")
elif nota_recebida >= 1 and nota_recebida <= 35:
    print("Conceito D")
elif nota_recebida >= 36 and nota_recebida <= 60:
    print("Conceito C")
elif nota_recebida >= 61 and nota_recebida <= 85:
    print("Conceito B")
else:
    print("Conceito A")
