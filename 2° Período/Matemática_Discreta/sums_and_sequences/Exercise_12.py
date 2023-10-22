# Função para verificar se um caractere é uma consoante
def is_consoante(caractere):
    consoantes = "bcdfghjklmnpqrstvwxyz"  # Lista de consoantes em minúsculas
    return caractere.lower() in consoantes

# Função para contar as consoantes e imprimir no formato de relação
def contar_consoantes_e_imprimir(vetor):
    consoantes = [caractere for caractere in vetor if is_consoante(caractere)]
    num_consoantes = len(consoantes)
    
    print("Consoantes lidas:")
    for i, consoante in enumerate(consoantes):
        print(f"Consoante {i+1}: {consoante}")
    
    print(f"\nTotal de consoantes lidas: {num_consoantes}")

# Lê um vetor de 6 caracteres
vetor = []
for i in range(6):
    caractere = input(f"Digite o {i+1}º caractere: ")
    vetor.append(caractere)

# Chama a função para contar as consoantes e imprimir a relação
contar_consoantes_e_imprimir(vetor)
