# Definindo o número de caixas, livros e o seu peso.
numeroCaixas = int(input("Quantas caixas o caminhão pode transportar:"))
numeroLivros = int(input("Quantos livros pode ter em cada caixa:"))
pesoLivro = float(input("Qual é o peso de um livro:"))
# Realizando o cálculo da quantidade de livros transportados pelo caminhão e o peso total da carga.
livrosCaminhao = numeroLivros * numeroCaixas
cargaTotal = numeroLivros * pesoLivro
# Mostrando na tela o resultado do cálculo.
print("Quantidade de livros transportadas pelo caminhão é igual a:", livrosCaminhao)
print("Quantidade de carga transportada pelo caminhão em quilos é igual a:", cargaTotal)

qtdeCopias = int(input("Quantas copias foram realizadas:"))
custoTotal = float(input("Qual o custo total da impressão:"))
valorCopia = custoTotal/qtdeCopias
print("O valor pago por copia é igual a:", valorCopia)

idade = int(input("Qual a sua idade:"))
idadeMeses = idade*12
idadePermitida = 18*12
if idade >= 18:
    print("Pode dirigir e votar")
else:
    mesesParaDirigir = idadePermitida - idadeMeses
    print("Não pode dirigir ainda, falta",
          mesesParaDirigir, "meses para poder dirigir")

idade = int(input("Qual a sua idade:"))
if idade < 16:
    print("Não pode votar e dirigir")
elif idade >= 16 and idade < 18:
    print("Pode votar e não pode dirigir")
else:
    print("Pode votar e dirigir")
print("Fim do programa!")

# Perguntando o peso do boxeador:
pesoBoxeador = float(
    input("Digite o seu peso para identificar qual categoria você pertence:"))
# Verificando qual categoria o boxeador pertence:
if pesoBoxeador < 50:
    print("Você é peso palha")
elif pesoBoxeador >= 50 or pesoBoxeador < 60:
    print("Você é peso pluma")
elif pesoBoxeador >= 60 or pesoBoxeador < 76:
    print("Você é peso leve")
elif pesoBoxeador >= 76 or pesoBoxeador < 88:
    print("Você é peso pluma")
else:
    print("Você é peso super pesado")

# Analisando 3 medidas para verificar se é um triângulo
comprimentoA = float(input("Digite o valor do comprimento A:"))
comprimentoB = float(input("Digite o valor do comprimento B:"))
comprimentoC = float(input("Digite o valor do comprimento C:"))
# Se for um triângulo, irá classificar de acordo com suas medidas ou retonará como nã osendo um triângulo
if comprimentoA < (comprimentoB + comprimentoC) and comprimentoB < (comprimentoA + comprimentoC) and comprimentoC < (comprimentoB + comprimentoA):
    print("É um triângulo")
    if (comprimentoA == comprimentoB) and (comprimentoC == comprimentoB):
        print("É um triângulo Equilatero")
    elif (comprimentoA == comprimentoB) or (comprimentoB == comprimentoC) or (comprimentoA == comprimentoC):
        print("É um triângulo Isósceles")
    else:
        print("É um triângulo Escaleno")
else:
    print("Não é um triângulo")

salarioFuncionario = float(input("Digite o seu salário:"))

if salarioFuncionario < 1257.13:
    print("Sem desconto")
elif salarioFuncionario >= 1257.13 and salarioFuncionario <= 2512.08:
    print((salarioFuncionario - (salarioFuncionario * 0.15)), "com desconto de 15%")
else:
    print((salarioFuncionario - (salarioFuncionario * 0.275)),
          "com desconto de 27.5%")
