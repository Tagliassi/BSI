# Definindo o conjunto original
C = {2, 3, 4}

# Lista para guardar os subconjuntos gerados
subsets = []

# Função recursiva para gerar subconjuntos
def generate_subsets(current_set, remaining_elements):
    # Caso base: Se não houver elementos restantes
    if not remaining_elements:
        subsets.append(current_set)
        return
    
    # Chamada recursiva sem incluir o primeiro elemento
    generate_subsets(current_set, remaining_elements[1:])
    
    # Chamada recursiva incluindo o primeiro elemento
    generate_subsets(current_set + [remaining_elements[0]], remaining_elements[1:])

# Inicialização da função recursiva com conjunto vazio e elementos de C
generate_subsets([], list(C))

# Verificação e impressão dos resultados
for subset in subsets:
    if set(subset).issubset(C):
        print(f"{subset} é um subconjunto de C")
    else:
        print(f"{subset} NÃO é um subconjunto de C")
