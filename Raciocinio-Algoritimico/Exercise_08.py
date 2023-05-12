# Exercise 01:

# notas_alunos = []
# soma_notas = 0

# for cont in range(0, 5, 1):
# nova_nota = int(input("Digite a nota do aluno entre 0 e 10: "))
# while nova_nota < 0 or nova_nota > 10:
# nova_nota = int(input("Digite a nota do aluno entre 0 e 10: "))
# notas_alunos.append(nova_nota)
# print(notas_alunos)
# soma_notas += nova_nota

# media_notas = soma_notas/5
# print("A média das notas é = ", media_notas)

# Exercise 02:

# vetor_inteiros = []

# for cont in range(0, 10, 1):
# dado_inteiro = int(input("Digite o dado: "))
# vetor_inteiros.append(dado_inteiro)
# print(vetor_inteiros)

# localizar_dado = int(input("Digite o dado que quer localizar: "))

# if localizar_dado == len(vetor_inteiros):
# print("A posição desse dado é = ", vetor_inteiros.index(localizar_dado))
# else:
# print("Não está no vetor")

# Exercise 03:

# todos_numeros_apostados = []
# todos_numeros_sorteados = []
# numeros_acertados = []

# for cont in range(0, 6, 1):
# numeros_apostados = int(input("Digite os 6 números que você apostou: "))
# todos_numeros_apostados.append(numeros_apostados)

# for cont in range(0, 6, 1):
# numeros_sorteados = int(input("Digite os 6 números que foram sorteados: "))
# todos_numeros_sorteados.append(numeros_sorteados)

# print(todos_numeros_apostados)
# print(todos_numeros_sorteados)

# for elementos_lista1 in todos_numeros_apostados:
# for elementos_lista2 in todos_numeros_sorteados:
# if (elementos_lista1 == elementos_lista2):
# numeros_acertados.append(elementos_lista1)
# break

# print(numeros_acertados)
# print("Parabéns a quantidade de números que você acertou é = ", len(numeros_acertados))

# Exercise 04:

# faturamento = 0
# mercardorias  = []

# for id_mercadoria in range(1, 3):
    # quantidade = int(input(f"Informe a quantidade vendida da mercadoria {id_mercadoria}: "))
    # preco = float( input(f"Informe o preço de venda da mercadoria {id_mercadoria}: "))
    # mercadoria = [id_mercadoria, quantidade, preco]
    # mercardorias.append(mercadoria)
    # faturamento_mercadoria = quantidade * preco
    # faturamento += faturamento_mercadoria

# print("O faturamento mensal do armazém é: ", faturamento)
# print(mercardorias)

# Exercise 05:

string = input("Digite uma string: ")
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
espaco = [' ']

for caracter in string:
    for caracter_vogal in vogais and espaco:
        if caracter == caracter_vogal:
            print("Existe vogais e espaco")