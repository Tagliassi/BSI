## Criação de Matriz e atribuição de valores a matriz
# Criação de Matriz de forma direta

# matriz_inic_direta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for linha in range(0, 3):
    # print("Linha", linha)
    # for coluna in range(0, 3):
        # print(matriz_inic_direta[linha][coluna])

# --------------------------------------------------------------------------------------------

# Criação de Matriz de forma dinamica

# nLinhas = 3
# nColunas = 4
# matriz_dinamica = [0] * nLinhas

# for linha in range(nLinhas):
    # matriz_dinamica[linha] = [0] * nColunas
    
# print(matriz_dinamica)

# --------------------------------------------------------------------------------------------

# Criação de Matriz de forma dinamica e curta

#nLinhas = 2
#nColunas = 3
#valor_de_cada_coluna = 0

# Criação de matriz vazia: ncolunas recebe o valor_de_cada_coluna e nlinhas recebe ncolunas para cada linha.

#matriz = [[valor_de_cada_coluna for coluna in range(nColunas)] for linha in range(nLinhas)]

# --------------------------------------------------------------------------------------------

# Criação e atribuição de valores a matriz de forma rápida

#nLinhas = 2
#nColunas = 3

# Criar matriz vazia
#matriz = []

# Obter valores para cada coluna e linha
#for linha in range(nLinhas):
    #valores = []
    #for coluna in range(nColunas):
        #valor = int(input(f"Digite o valor para a linha {linha+1} e coluna {coluna+1}: "))
        #valores.append(valor)
    #matriz.append(valores)

## --------------------------------------------------------------------------------------------

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

#numero_linhas = 3
#numero_colunas = 4
#matriz = [0] * numero_linhas

#for linha in range(numero_linhas):
    #matriz[linha] = [0] * numero_colunas


#for linha in range(numero_linhas):
    #for coluna in range(numero_colunas):
        #matriz[linha][coluna] = float(input("Digite a nota do aluno:"))

#aluno = 0

#for linha in range(numero_linhas):
    #soma = 0
    #for coluna in range(numero_colunas):
        #soma = soma + matriz[linha][coluna]
    #media = soma/numero_colunas
    #aluno = aluno + 1
    #print(f"Media aluno {aluno} =", media)


# Exercise 02 - Reorganização de matrizes:

numero_linhas = 3
numero_colunas = 3
matriz = [0] * numero_linhas

for linha in range(numero_linhas):
    matriz[linha] = [0] * numero_colunas

for linha in range(numero_linhas):
    for coluna in range(numero_colunas):
        matriz[linha][coluna] = int(input("Digite o conteúdo da matriz: "))

for linha in range(numero_linhas -1, -1, -1):
    print("linha", linha)
    for coluna in range(numero_colunas -1, -1,-1):
        print(matriz[linha][coluna])

#[[3, 2, 1], [6, 5, 4], [9, 8, 7]] invertendo as colunas das linhas 

# --------------------------------------------------------------------------------------------

numero_linhas = 3
numero_colunas = 3
matriz = [0] * numero_linhas

for linha in reversed(range(numero_linhas)):
    matriz[linha] = [0] * numero_colunas
    for coluna in reversed(range(numero_colunas)):
        matriz[linha][coluna] = int(input("Digite o conteúdo da matriz: "))

for linha in reversed(range(numero_linhas)):
    print("linha", linha)
    for coluna in reversed(range(numero_colunas)):
        print(matriz[linha][coluna])
    print()

#[[7, 8, 9], [4, 5, 6], [1, 2, 3]] invertendo as posições das linhas 

# --------------------------------------------------------------------------------------------

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for linha in matriz:
    linha.reverse()

print(matriz)
#[[3, 2, 1], [6, 5, 4], [9, 8, 7]]

# --------------------------------------------------------------------------------------------

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_reorganizada = list(reversed(matriz))
print(matriz_reorganizada)

#[[7, 8, 9], [4, 5, 6], [1, 2, 3]]

# --------------------------------------------------------------------------------------------

matriz = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

for linha in matriz:
    linha.reverse()

print(matriz)
# [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# --------------------------------------------------------------------------------------------

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nova_matriz = matriz.copy()  # Cria uma cópia da matriz original

linha_temporaria = nova_matriz[0]
nova_matriz[0] = nova_matriz[1]
nova_matriz[1] = linha_temporaria

print(nova_matriz)
#[[4, 5, 6], [1, 2, 3], [7, 8, 9]] - substituição de linhas

#Exercise 03:

nLinhas = 2
nColunas = 2
valor_de_cada_coluna = 0

matriz_a = []

for linha in range(nLinhas):
    valores = []
    for coluna in range(nColunas):
        valor = int(input(f"Digite o valor para a linha {linha+1} e coluna {coluna+1}: "))
        valores.append(valor)
    matriz_a.append(valores)

matriz_b = []

for linha in range(nLinhas):
    valores = []
    for coluna in range(nColunas):
        valor = int(input(f"Digite o valor para a linha {linha+1} e coluna {coluna+1}: "))
        valores.append(valor)
    matriz_b.append(valores)

matriz_c = [[valor_de_cada_coluna for coluna in range(nColunas)] for linha in range(nLinhas)]

for linha in range(nLinhas):
    for coluna in range(nColunas):
        matriz_c[linha][coluna] = matriz_a[linha][coluna] + matriz_b[linha][coluna]

print(matriz_c)

#Exercise 04:

nLinhas = 5
nColunas = 3
valor_de_cada_coluna = 0

matriz_apostas = [[valor_de_cada_coluna for coluna in range(nColunas)] for linha in range(nLinhas)]

print(matriz_apostas)

print("Apostas do jogador 1")

jogador_01 = []

for linha in range(3):
    valores = []
    for coluna in range(2):
        valor = int(input(f"Digite o valor para a aposta do jogo, sendo o primeiro valor, placar do Brasil e o segundo valor, placar do adversário, jogo {linha +1}: "))
        valores.append(valor)
    jogador_01.append(valores)

for coluna in range(3):
    matriz_apostas[0][coluna] = jogador_01[coluna]

print("Apostas do jogador 2")

jogador_02 = []

for linha in range(3):
    valores = []
    for coluna in range(2):
        valor = int(input(f"Digite o valor para a aposta do jogo, sendo o primeiro valor, placar do Brasil e o segundo valor, placar do adversário, jogo {linha +1}: "))
        valores.append(valor)
    jogador_02.append(valores)

for coluna in range(3):
    matriz_apostas[1][coluna] = jogador_02[coluna]

print("Apostas do jogador 3")

jogador_03 = []

for linha in range(3):
    valores = []
    for coluna in range(2):
        valor = int(input(f"Digite o valor para a aposta do jogo, sendo o primeiro valor, placar do Brasil e o segundo valor, placar do adversário, jogo {linha +1}: "))
        valores.append(valor)
    jogador_03.append(valores)

for coluna in range(3):
    matriz_apostas[2][coluna] = jogador_03[coluna]

print("Apostas dos jogadores")

print(matriz_apostas)