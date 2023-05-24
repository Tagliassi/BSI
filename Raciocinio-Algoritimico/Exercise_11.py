#Exemplo 01:
"""
def calcular_total(valor_hora, horas_cheias):
    total_pagar = valor_hora * horas_cheias
    print(total_pagar)

valor = float(input("Digite o valor da hora (reais): "))
horas = int(input("Digite o valor das horas: "))

calcular_total(valor, horas)
"""

def verificar_numero(numero, intervalo_inferior, intervalo_superior):
    if numero >= intervalo_inferior and numero <= intervalo_superior:
        return True
        
    return False

ret = verificar_numero(-1, 0, 10)
print(ret)