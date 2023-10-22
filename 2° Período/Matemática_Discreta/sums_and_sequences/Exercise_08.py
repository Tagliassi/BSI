def calcular_somas_01():
    try:

        n = int(input("Digite o tamanho da primeira sequência: "))
        n2 = int(input("Digite o tamanho da segunda sequência: "))
        i = int(input("Digite o primeiro limite inferior: "))
        i2 = int(input("Digite o segundo limite inferior: "))
        #k = (x + y) ** 2
        soma = 0

        if n <= 0:
            print("O tamanho da sequência deve ser maior que zero.")
            return

        valores = []
        for i in range(i, n+1):
            x = i
            for j in range(i2,n2+1):
                y = j  
                iteracao = (x + y) ** 2
                soma += iteracao
                print(iteracao)  
        print(soma) 

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valores numéricos inteiros.")

#if __name__ == "__main__":
    #calcular_somas_01()

def calcular_somas_02():
    try:

        n = int(input("Digite o tamanho da primeira sequência: "))
        n2 = int(input("Digite o tamanho da segunda sequência: "))
        i = int(input("Digite o primeiro limite inferior: "))
        i2 = int(input("Digite o segundo limite inferior: "))
        #k = (x*y) - 5
        soma = 0

        if n <= 0:
            print("O tamanho da sequência deve ser maior que zero.")
            return

        valores = []
        for i in range(i, n+1):
            x = i
            for j in range(i2,n2+1):
                y = j  
                iteracao = (x*y) - 5
                soma += iteracao
                print(iteracao)  
        print(soma) 

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valores numéricos inteiros.")

if __name__ == "__main__":
    calcular_somas_02()
