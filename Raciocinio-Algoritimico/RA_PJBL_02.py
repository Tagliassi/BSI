# Programa: Vending Machine
# Autor: Rafael Galafassi, Vinicius Costa, Marcos Vincius e Vinicius Viana
# Data de criação: 07/06/2023
# Versão: 2.0
# Descrição: Programa que simula uma máquina de vendas.
# Observação: letras maiúsculas e números de 0 à 9 serão a única forma de entrada.

# Matriz para armazenar os produtos, quantidades e os preços
produtos = [["Refrigerante A", 10, 2.5],["Refrigerante B", 5, 3.0],["Refrigerante C", 8, 2.0]]
relatorios_de_pagamento = []  # Matriz para armazenar informações de vendas: Quantidade de produto X vendido, valor total da compra. Se for em PIX, Quantidade de produto X vendido, valor total da compra e telefone do consumidor.
pagamentos_dinheiro = [] # Lista para armazenar os pagamentos em dinheiro
pagamentos_pix = [] # Lista para armazenar os pagamentos via PIX
# Matriz para armazenar a quantidade de dinheiro por tipo (cédulas e moedas)
# Moedas de 0.25, 0.5, 1.0 // Cédulas de 2, 5, 10
quantidade_dinheiro = [[0, 0, 0],[0, 0, 0]]

def login(usuario, senha):
    # Implementar a lógica de autenticação
    pass

def visualizar_produtos():
    print("Produtos disponíveis:")

def adicionar_estoque(refrigerante, quantidade):
    # Implementar a lógica para adicionar a quantidade especificada ao estoque do refrigerante
    pass

def visualizar_quantidade_dinheiro():
    print("Quantidade de dinheiro por tipo:")
    print("Moedas:")
    print(f"0.25: {quantidade_dinheiro[0][0]}")
    print(f"0.5: {quantidade_dinheiro[0][1]}")
    print(f"1.0: {quantidade_dinheiro[0][2]}")
    print("Cédulas:")
    print(f"2: {quantidade_dinheiro[1][0]}")
    print(f"5: {quantidade_dinheiro[1][1]}")
    print(f"10: {quantidade_dinheiro[1][2]}")

def modificar_quantidade_dinheiro():
    print("Modificar quantidade de dinheiro por tipo:")
    print("Moedas:")
    
    print("Cédulas:")

def visualizar_relatorios():
    # Relatório de vendas
    print("Relatório de pagamentos:")
    pass

def atualizar_quantidade_dinheiro(valor_inserido):
    # Implementar a lógica para atualizar a quantidade de dinheiro, por exemplo o usuario recebeu troco, tem que diminuir e se comprou tem que aumentar
    pass

def realizar_pagamento(refrigerante, quantidade, opcao_pagamento):
    # Implementar a lógica para pagamento dos produtos, via pix ou dinheiro.
    pass

def entregar_produto(refrigerante, quantidade):
    # Implementar a lógica para entregar o produto ao consumidor
    pass

def main():
    while True:
        print("Bem-vindo(a) ao Sistema de Pagamentos da Máquina de Venda Automática!")
        print("Selecione uma opção:")
        print("1. Administrador")
        print("2. Consumidor")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            usuario = input("Usuário: ")
            senha = input("Senha: ")
            if login(usuario, senha):
                print("Login do administrador bem-sucedido.")
                # Exibir menu do administrador e chamar funções correspondentes
            else:
                print("Usuário ou senha inválidos.")

        elif opcao == "2":
            print("Login do consumidor bem-sucedido.")
            visualizar_produtos()
            refrigerante = int(input("Digite o número do refrigerante desejado: "))
            quantidade = int(input("Digite a quantidade desejada: "))
            print("Selecione uma opção de pagamento:")
            print("1. PIX")
            print("2. Dinheiro")
            opcao_pagamento = input("Opção de pagamento: ")
            realizar_pagamento(refrigerante, quantidade, opcao_pagamento)

        elif opcao == "3":
            print("Obrigado por utilizar o Sistema de Pagamentos da Máquina de Venda Automática!")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

main()