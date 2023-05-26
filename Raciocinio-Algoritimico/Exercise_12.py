# Exercise 01:
"""
valor_veiculo = float(input("Digite o valor do produto: "))
valor_comissao = float(input("Digite o valor da comissão: "))

def calcular_comissao(valor_veiculo,valor_comissao):
    percentual_comissao = valor_comissao/100
    return valor_veiculo*percentual_comissao

comissao = calcular_comissao(valor_veiculo, valor_comissao)
print("O valor da comissão é =", comissao)
"""
# Exercise 02:

nLinhas = 5
nColunas = 1
valor_de_cada_coluna = 0
soma_alturas = 0.0
altura_atual = 0.0
altura_maior = 0.0

matriz_alturas = [[valor_de_cada_coluna for coluna in range(nColunas)] for linha in range(nLinhas)]

for linha in range(nLinhas):
    for coluna in range(nColunas):
        matriz_alturas[linha][coluna] = int(input("Digite oa altura de cada criança: "))
        soma_alturas += matriz_alturas[linha][coluna]
        altura_atual = matriz_alturas[linha][coluna]
    if altura_atual > altura_maior:
        altura_atual = altura_maior
media_alturas = soma_alturas/nLinhas

print(matriz_alturas)
print(media_alturas)
print(altura_maior)
