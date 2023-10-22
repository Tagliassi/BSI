# Inicialize um vetor para armazenar os votos para cada linguagem
votos = [0, 0, 0, 0, 0, 0]

# Nomes das linguagens de programação
linguagens = ["Python", "C++", "Java", "Rust", "C#", "Outro"]

# Solicita os votos até que seja informado o valor 0
while True:
    print("Qual linguagem de programação tem a melhor tendência para o futuro?")
    print("1 - Python")
    print("2 - C++")
    print("3 - Java")
    print("4 - Rust")
    print("5 - C#")
    print("6 - Outro")
    print("0 - Encerrar a votação")
    
    voto = int(input("Digite o número da sua escolha: "))
    
    if voto == 0:
        break
    
    if 1 <= voto <= 6:
        votos[voto - 1] += 1
    else:
        print("Voto inválido. Escolha um número de 0 a 6.")

# Calcula o total de votos
total_votos = sum(votos)

# Imprime o cabeçalho
print("Linguagem      Votos     %")

# Imprime os resultados para cada linguagem
for i in range(6):
    percentual = (votos[i] / total_votos) * 100
    print(f"{linguagens[i]:<12} {votos[i]:<8} {percentual:.1f}%")

# Imprime o total
print("------------------- ----- ---")
print(f"Total        {total_votos:<8} 100%")
