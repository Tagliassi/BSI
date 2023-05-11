# Test

vetor = ["dado_posicao_0", "dado_posicao_1", "dado_posicao_2"]

vetor.append("dado_posicao_3")

for indice_atual in range(len(vetor)):
    print(vetor[indice_atual])

notas = []

for cont in range(5):
    nota = float(input("Digite sua nota: "))
    notas.append(nota)

for cont in range(len(notas)):
    print(notas[cont])

soma = 0 
for cont in range(len(notas)):
    soma = soma + notas[cont]

media = soma/len(notas)
print("Média = ", media)
