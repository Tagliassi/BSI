# Exercise 01:

def calcular_Imc(peso, altura):

    return peso / (altura * altura)

print(calcular_Imc(50, 1.70))

# Exercise 02:

def detector_de_palavra():
    palavra = 1
    string = str(input("Digite uma string para contar o numero de palaras: "))
    for caracter in range (len(string)):
        if string[caracter] == ' ':
            palavra = palavra + 1
    return palavra

print("Há um total de", detector_de_palavra(), "palavras nessa string")
    