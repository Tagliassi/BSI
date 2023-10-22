
vetor = []

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    vetor.append(numero)

vetor.reverse()

print("Números na ordem inversa:")
for i, numero in enumerate(vetor):
    print(f"{i + 1} - {numero}")
