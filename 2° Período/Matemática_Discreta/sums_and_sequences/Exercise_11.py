import random

# Função para sortear 6 números e colocá-los na lista 'num'
def sorteia():
    num = []
    for i in range(6):
        num.append(random.randint(1, 100))  # Você pode ajustar o intervalo dos números conforme desejado
    return num

# Função para mostrar a soma dos valores pares e os pares ordenados
def somaPar(num):
    pares = [x for x in num if x % 2 == 0]
    soma = sum(pares)
    pares_ordenados = [(num[i], num[i + 1]) for i in range(0, len(num), 2)]
    
    print("Números sorteados:")
    for i, n in enumerate(num):
        print(f"Número {i+1}: {n}")
    
    print("\nPares ordenados:")
    for i, (n1, n2) in enumerate(pares_ordenados):
        print(f"Par {i+1}: ({n1}, {n2})")
    
    print("\nPares que foram somados:")
    for i, p in enumerate(pares):
        print(f"Par {i+1}: {p}")
    
    print(f"\nSoma dos valores pares: {soma}")

# Chama a função sorteia para obter a lista de números
numeros_sorteados = sorteia()

# Chama a função somaPar para calcular a soma dos pares e mostrar os resultados
somaPar(numeros_sorteados)
