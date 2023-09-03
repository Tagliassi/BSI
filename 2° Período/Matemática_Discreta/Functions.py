import matplotlib.pyplot as plt
import numpy as np

def funcao1oGrau(a,b,x):
    return (a*x + b)

vetorX = np.arange(-5,5,0.5) #1 to 0.5

#A função retorna um array NumPy que contém a sequência de números dentro do intervalo especificado, com o espaçamento determinado pelo valor do parâmetro step.
print(vetorX) #[-5 -4 -3 -2 -1  0  1  2  3  4] 

# Calcula os valores de y usando a função de primeiro grau
vetorY = funcao1oGrau(2, 5, vetorX)
print("Valores de y:", vetorY)

# Plotando o gráfico da função com uma reta
plt.plot(vetorX, vetorY)
#aqui estamos plotando ponto a ponto do vetor x com o respectivo y
plt.scatter(vetorX, vetorY)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(y=0, color='k')
plt.title('Gráfico da Função de Primeiro Grau')
#aqui criamos uma grid para a tabela
plt.grid(True)
#aqui chamamos a função para mostrar a janela
plt.show() 

# a) O que podemos observar? Criamos o gráfico da função
# b) Altere o valor utilizado no terceiro parâmetro da função arange na criação do vetorX para 0.5
# c) Encontre um valor para esse mesmo parâmetro em que a função fique “contínua”. 0.1
# d) Mude a função scatter para a função plot. O que podemos notar? Gerou uma reta

# a. Função do 2º grau: f(x) = ax² + bx + c
# Definir os parâmetros a, b e c
a = 1
b = 2
c = 1

# Gerar valores de x
x = np.arange(-10, 10, 1)

# Calcular os valores de y
y = a * x**2 + b * x + c

# Plotar gráfico discreto
plt.scatter(x, y, label='f(x) = ax² + bx + c')

# Plotar gráfico contínuo
x_cont = np.arange(-10, 10, 0.1)
y_cont = a * x_cont**2 + b * x_cont + c
plt.plot(x_cont, y_cont, label='Contínuo')

plt.legend()
plt.title('Gráfico da Função do 2º Grau')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

# b. Função exponencial: f(x) = ab^x

# Definir os parâmetros a e b
a = 1
b = 2

# Gerar valores de x
x = np.arange(2, 5, 1)

# Calcular os valores de y
y = a * b**x

# Plotar gráfico discreto
plt.scatter(x, y, label='f(x) = ab^x')

# Plotar gráfico contínuo
x_cont = np.arange(2, 5, 0.1)
y_cont = a * b**x_cont
plt.plot(x_cont, y_cont, label='Contínuo')

plt.legend()
plt.title('Gráfico da Função Exponencial')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

# c. Função modular: f(x) = |x|

# Gerar valores de x
x = np.arange(-2, 2, 1)

# Calcular os valores de y
y = np.abs(x)

# Plotar gráfico discreto
plt.scatter(x, y, label='f(x) = |x|')

# Plotar gráfico contínuo
x_cont = np.arange(-2, 2, 0.1)
y_cont = np.abs(x_cont)
plt.plot(x_cont, y_cont, label='Contínuo')

plt.legend()
plt.title('Gráfico da Função Modular')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

# d. Função seno: f(x) = sen(x)

# Gerar valores de x
x = np.linspace(-2*np.pi, 2*np.pi, 100)

# Calcular os valores de y
y = np.sin(x)

# Plotar gráfico discreto
plt.scatter(x, y, label='f(x) = sen(x)')

# Plotar gráfico contínuo
x_cont = np.linspace(-2*np.pi, 2*np.pi, 1000)
y_cont = np.sin(x_cont)
plt.plot(x_cont, y_cont, label='Contínuo')

plt.legend()
plt.title('Gráfico da Função Seno')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()