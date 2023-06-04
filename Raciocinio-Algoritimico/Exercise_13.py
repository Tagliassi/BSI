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

