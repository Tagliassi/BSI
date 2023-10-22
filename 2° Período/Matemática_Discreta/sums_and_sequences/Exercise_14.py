# Inicialize um vetor A com 5 números inteiros
vetor_A = []

# Solicite os números e armazene no vetor
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor_A.append(numero)

# Calcula a soma dos quadrados dos elementos do vetor
soma_quadrados = sum(x ** 2 for x in vetor_A)

# Imprime a soma dos quadrados
print(f"A soma dos quadrados dos elementos do vetor é: {soma_quadrados}")
