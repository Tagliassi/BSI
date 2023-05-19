# Criação de Matriz de forma direta

# matriz_inic_direta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for linha in range(0, 3):
    # print("Linha", linha)
    # for coluna in range(0, 3):
        # print(matriz_inic_direta[linha][coluna])

# Criação de Matriz de forma dinamica

# nLinhas = 3
# nColunas = 4
# matriz_dinamica = [0] * nLinhas

# for linha in range(nLinhas):
    # matriz_dinamica[linha] = [0] * nColunas
    
# print(matriz_dinamica)


# Exemplo 01:

#nLinhas = 2
#nColunas = 2
#matriz = [0] * nLinhas

#for linha in range(nLinhas):
    #matriz[linha] = [0] * nColunas

#for linha in range(nLinhas):
    #for coluna in range(nColunas):
        #matriz[linha][coluna] = int(input('Digite um número: '))
#print(matriz)

#for linha in range(nLinhas):
    #soma = 0
    #for coluna in range(nColunas):
        #soma = soma + matriz[linha][coluna]
    #print('Soma na linha ', linha, ' = ', soma)

# Exercise 01:

numero_linhas = 3
numero_colunas = 4
matriz = [0] * numero_linhas

for linha in range(numero_linhas):
    matriz[linha] = [0] * numero_colunas

print(matriz)

for linha in range(numero_linhas):
    for coluna in range(numero_colunas):
        matriz[linha][coluna] = float(input("Digite a nota do aluno:"))
print(matriz)

for linha in range(numero_linhas):
    soma = 0
    for coluna in range(numero_colunas):
        soma = soma + matriz[linha][coluna]
    media = soma/numero_colunas
    print("Media =", media)