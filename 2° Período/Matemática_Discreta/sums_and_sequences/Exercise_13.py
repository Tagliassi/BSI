# Função para calcular a média de um aluno
def calcular_media(notas):
    return sum(notas) / len(notas)

# Número de alunos
num_alunos = 6

# Inicialize uma lista para armazenar as médias dos alunos
medias = []

# Solicite as notas e calcule a média para cada aluno
for i in range(num_alunos):
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)
    
    media = calcular_media(notas)
    medias.append(media)

# Contagem de alunos com média maior ou igual a 7.0
alunos_aprovados = sum(1 for media in medias if media >= 7.0)

# Imprima as médias de todos os alunos
for i, media in enumerate(medias):
    print(f"Média do aluno {i+1}: {media:.2f}")

# Imprima o número de alunos aprovados
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
