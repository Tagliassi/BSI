# Programa: Vending Machine
# Autor: Rafael Galafassi, Vinicius Costa, Marcos Vincius e Vinicius Viana
# Data de criação: 07/06/2023
# Versão: 2.0
# Descrição: Programa que simula uma máquina de vendas.
# Observação: letras maiúsculas e números de 0 à 9 serão a única forma de entrada.

# Matriz para armazenar os produtos, quantidades e os preços
produtos = [["Refrigerante A", 10, 2.5],["Refrigerante B", 5, 3.0],["Refrigerante C", 8, 2.0]]
relatorios = []  # Matriz para armazenar informações de vendas
pagamentos_dinheiro = [] # Lista para armazenar os pagamentos em dinheiro
pagamentos_pix = [] # Lista para armazenar os pagamentos via PIX
# Matriz para armazenar a quantidade de dinheiro por tipo (cédulas e moedas)

quantidade_dinheiro = [
    [0, 0, 0],  # Moedas de 0.25, 0.5, 1.0
    [0, 0, 0]   # Cédulas de 2, 5, 10
]

def login(usuario, senha):
    # Implementar a lógica de autenticação
    pass

def adicionar_estoque(refrigerante, quantidade):
    # Implementar a lógica para adicionar a quantidade especificada ao estoque do refrigerante
    pass

def visualizar_relatorios():
    # Relatório de vendas em pix
    print("Relatório de pagamentos via PIX:")
    for pagamento in pagamentos_pix:
        telefone = pagamento["telefone"]
        valor = pagamento["valor"]
        print(f"Telefone: {telefone} - Valor: R${valor:.2f}")
    pass

def visualizar_produtos():
    print("Produtos disponíveis:")
    for produto in produtos:
        nome = produto[0]
        quantidade = produto[1]
        preco = produto[2]
        print(f"Nome: {nome} - Quantidade: {quantidade} - Preço: {preco}")

def realizar_pagamento(refrigerante, quantidade, opcao_pagamento):
    preco_unitario = produtos[refrigerante][2]
    valor_total = quantidade * preco_unitario

    if opcao_pagamento == "1":  # PIX
        telefone = input("Digite o número de telefone para pagamento via PIX: ")
        pagamentos_pix.append({"telefone": telefone, "valor": valor_total})
        print("Realizando pagamento via PIX...")
        # Lógica para processar o pagamento via PIX

    elif opcao_pagamento == "2":  # Dinheiro
        valor_pago = 0.0
        while valor_pago < valor_total:
            print(f"Valor total: R${valor_total:.2f}")
            valor_inserido = float(input("Digite o valor inserido (moeda ou cédula): "))

            # Verifica se o valor inserido é válido
            if valor_inserido in [0.25, 0.5, 1.0, 2.0, 5.0, 10.0]:
                valor_pago += valor_inserido
            else:
                print("Valor inválido. Insira uma moeda de 0.25, 0.5 ou 1.0 real, ou uma cédula de 2, 5 ou 10 reais.")

        troco = valor_pago - valor_total

        if troco >= 0:
            pagamentos_dinheiro.append({"valor": valor_total})
            print(f"Pagamento em dinheiro efetuado. Troco: R${troco:.2f}")
            # Lógica para entregar o produto
        else:
            print("Valor insuficiente. Pagamento não efetuado.")
            
    else:
        print("Opção de pagamento inválida.")

def entregar_produto(refrigerante, quantidade):
    # Implementar a lógica para entregar o produto ao consumidor
    pass

def atualizar_quantidade_dinheiro(valor_inserido):
    if valor_inserido == 0.25:
        quantidade_dinheiro[0][0] += 1
    elif valor_inserido == 0.5:
        quantidade_dinheiro[0][1] += 1
    elif valor_inserido == 1.0:
        quantidade_dinheiro[0][2] += 1
    elif valor_inserido == 2.0:
        quantidade_dinheiro[1][0] += 1
    elif valor_inserido == 5.0:
        quantidade_dinheiro[1][1] += 1
    elif valor_inserido == 10.0:
        quantidade_dinheiro[1][2] += 1

def modificar_quantidade_dinheiro():
    print("Modificar quantidade de dinheiro por tipo:")
    print("Moedas:")
    quantidade_dinheiro[0][0] = int(input("Quantidade de moedas de 0.25: "))
    quantidade_dinheiro[0][1] = int(input("Quantidade de moedas de 0.5: "))
    quantidade_dinheiro[0][2] = int(input("Quantidade de moedas de 1.0: "))
    print("Cédulas:")
    quantidade_dinheiro[1][0] = int(input("Quantidade de cédulas de 2: "))
    quantidade_dinheiro[1][1] = int(input("Quantidade de cédulas de 5: "))
    quantidade_dinheiro[1][2] = int(input("Quantidade de cédulas de 10: "))

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
            usuario = input("Usuário: ")
            senha = input("Senha: ")
            if login(usuario, senha):
                print("Login do consumidor bem-sucedido.")
                visualizar_produtos()
                refrigerante = int(input("Digite o número do refrigerante desejado: "))
                quantidade = int(input("Digite a quantidade desejada: "))
                print("Selecione uma opção de pagamento:")
                print("1. PIX")
                print("2. Dinheiro")
                opcao_pagamento = input("Opção de pagamento: ")
                realizar_pagamento(refrigerante, quantidade, opcao_pagamento)
            else:
                print("Usuário ou senha inválidos.")

        elif opcao == "3":
            print("Obrigado por utilizar o Sistema de Pagamentos da Máquina de Venda Automática!")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

main()

