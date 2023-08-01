#Exemplo 01:

def calcular_total(valor_hora, horas_cheias):
    total_pagar = valor_hora * horas_cheias
    print(total_pagar)

valor = float(input("Digite o valor da hora (reais): "))
horas = int(input("Digite o valor das horas: "))

calcular_total(valor, horas)

#Exercise 01:

def verificar_numero(numero, intervalo_inferior, intervalo_superior):
    if numero >= intervalo_inferior and numero <= intervalo_superior:
        return True
        
    return False

ret = verificar_numero(-1, 0, 10)
print(ret)

#Exercise 02:

operando1 = float(input("Digite o valor 1 que quer realizar as operações: "))
operando2 = float(input("Digite o valor 2 que quer realizar as operações: "))

def somar(operando1,operando2):
    soma = operando1 + operando2
    return soma

resultado = somar(operando1, operando2)
print(resultado)

def dividir(operando1,operando2):
    if operando1 >= operando2 and operando1 != 0 and operando2 != 0:
        divisao = operando1 / operando2
    elif operando1 != 0 and operando2 != 0:
        divisao = operando2 / operando1
    else:
        print("Divisão por 0")
        return False
    return divisao

resultado = dividir(operando1, operando2)
print(resultado)

def multiplicar(operando1,operando2):
    multiplicacao = operando1 * operando2
    return multiplicacao

resultado = multiplicar(operando1, operando2)
print(resultado)

def subtrair(operando1,operando2):
    if operando1 >= operando2:
        subtracao = operando1 - operando2
    else:
        subtracao = operando2 - operando1
    return subtracao

resultado = subtrair(operando1, operando2)
print(resultado)