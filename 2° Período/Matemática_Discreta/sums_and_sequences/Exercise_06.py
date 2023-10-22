#sequencias e somas: Média aritmética

n = int(input("Qual o tamanho da sequência?\n"))
x = []
soma = 0

while len(x) < n:
    a = int(input("Digite um valor:\n"))
    x.append(a)

for a in x:
    soma += a
    print(soma)
media = soma/n

# Exibe o resultado
print(f"A média das alturas é: {media:.2f} metros")

