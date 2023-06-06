# Exercise 01

# Função anotar_altura:
# entrada: quantidade de alunos
# saída: lista com a altura dos alunos

def anotar_altura(quantidade_alunos):
    lista = []
    for cont in range(0,quantidade_alunos):
        # str: converte número para string
        print("Digite a altura da criança " + str(cont + 1) + ": ")
        altura = float(input())
        lista.append(altura)
    return lista

# Função localizar_maior:
# entrada: lista com alturas
# saida: maior altura

def localizar_maior(lista):
    if len(lista) > 0:
        maior = lista[0]
        for cont in range(1, len(lista)):
            if maior < lista[cont]:
                maior = lista[cont]
                
        return maior
    else:
        return -1

# Função localizar_menor:
# entrada: lista com alturas
# saída: menor altura

def localizar_menor(lista):
    if len(lista) > 0:
        menor = lista[0]
        
        for cont in range(1, len(lista)):
            if menor > lista[cont]:
                menor = lista[cont]
            
        return menor
    else:
        return -1
    
# Função calcular_alturaMedia:
# entrada: lista com alturas
# saída: media das alturas

def calcular_alturaMedia(lista):
    if len(lista) > 0:
        media = 0
        
        for cont in range(0, len(lista)):
            media += lista[cont]
            
        return media/len(lista)
    else:
        return -1

# Exercise 02:

def criar_conta(saldo_inicial):
    global saldo
    saldo = saldo_inicial
    
def imprimir_saldo():
    print("Saldo = ", saldo)
    
def depositar(novo_saldo):
    global saldo
    saldo += novo_saldo

# Exercise 03:

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']

palavra = input("Digite a palavra que deseja criptografar: ")
letras = list(palavra)

palavra_criptografada = []

for letra in range (len(letras)):
    for caracter in range(len(alfabeto)):
        if letras[letra] == alfabeto[caracter]:
            palavra_criptografada.append(alfabeto[caracter + 3])

print(palavra_criptografada)

# Exercise 04(Recursividade):

Fibonacci = 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)

print(fibo(3))

# Desafio (torre de hanoi)

def hanoi(discos, origem, destino, temp):
    if discos == 1:
        print("Mova o disco", discos, "de", origem, "para", destino)
    else:
        hanoi(discos - 1, origem, temp, destino)
        print("Mova o disco", discos, "de", origem, "para", destino)
        hanoi(discos - 1, temp, destino, origem)

print("Digite o número de discos:")
total_discos = int(input())
hanoi(total_discos, 'A', 'B', 'C')
