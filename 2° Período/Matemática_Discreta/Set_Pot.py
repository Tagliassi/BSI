def conjPot(A):
    n = len(A)
    power_set = [] # Lista para armazenar os subconjuntos

    for i in range(2 ** n):  # Loop para todas as combinações de bits
        subset = []  # Inicializar um subconjunto vazio para cada i
        for j in range(n):  # Loop para cada bit no número i
            if (i >> j) & 1:  # Verifica se o bit j-ésimo está definido em i
                subset.append(A[j])  # Se sim, adiciona o elemento correspondente a subset
        power_set.append(subset)  # Adiciona o subconjunto gerado ao conjunto potência

    # Imprimir os subconjuntos
    print("{", end="")
    for subset in power_set:
        print("{", end="")
        print(",".join(map(str, subset)), end="")
        print("}", end="")
    print("}")

conjPot({1, 2, 3})