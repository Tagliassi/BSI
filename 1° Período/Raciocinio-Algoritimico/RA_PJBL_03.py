# Programa: Vending Machine
# Autor: Rafael Galafassi, Vinicius Costa, Marcos Vincius e Vinicius Viana
# Data de criação: 07/06/2023
# Versão: 2.0
# Descrição: Programa que simula uma máquina de vendas.
# Observação: letras maiúsculas e números de 0 à 9 serão a única forma de entrada.

# Matriz para armazenar os produtos, quantidades e os preços
produtos = [["Coca", 10, 2.5],["Guaraná", 5, 3.0],["Pepsi", 8, 2.0]]
relatorios_de_pagamento = []  # Matriz para armazenar informações de vendas: Quantidade de produto X vendido, valor total da compra. Se for em PIX, Quantidade de produto X vendido, valor total da compra e telefone do consumidor.
pagamentos_dinheiro = [] # Lista para armazenar os pagamentos em dinheiro
pagamentos_pix = [] # Lista para armazenar os pagamentos via PIX
# Matriz para armazenar a quantidade de dinheiro por tipo (cédulas e moedas)
# Moedas de 0.25, 0.5, 1.0 // Cédulas de 2, 5, 10 // valor_total_pix // quantidade_dinheiro
quantidade_dinheiro = [[0, 0, 0],[0, 0, 0],[0],[0]]
numeros_validos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
telefone_valido = ['4','1','0','1','2','3','4','5','6','7','8','9']

def login(usuario, senha):
     # Implementar a lógica de autenticação
    if usuario == "Administrador" and senha == "1234":
        print("Login do administrador bem-sucedido.")
        return True
    else:
        print("Usuário ou senha inválidos.")
        return False


def visualizar_produtos():
    print("Produtos disponíveis:")
    for produto in produtos:
        nome = produto[0]
        quantidade = produto[1]
        preco = produto[2]
        print(f"{produtos.index(produto)+1}. Refrigerante: {nome} - Quantidade: {quantidade} - Preço: {preco}")
    

def adicionar_estoque(refrigerante, quantidade):

    for produto in produtos:
        if produto[0] == refrigerante:
            produto[1] += quantidade
            
            print("Foram adicionadas", quantidade, "novas unidades de", refrigerante, "ao estoque.")
            return
    
    print("Produto não encontrado no estoque, ou quantidade invalida, digite novamente!")

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
    print("PIX:")
    print("Valor total - ", quantidade_dinheiro[2][0])
    print("DINHEIRO:")
    print("Total - ", quantidade_dinheiro[3][0])

# aq
def modificar_quantidade_dinheiro_moeda():
    print("Modificar quantidade de moedas:")
    tipos = ["R$0.25", "R$0.50", "R$1.00"]
    valor_total = 0

    for ContDinheiro in range(len(tipos)):
        print("Moedas:")
        try:
            quantidade_dinheiro[0][ContDinheiro] = int(input(f"Digite a nova quantidade de moedas de {tipos[ContDinheiro]}: "))
        except ValueError:
            print("Digite um número inteiro por favor!")
            return

        if ContDinheiro == 0:
            valor_total += quantidade_dinheiro[0][ContDinheiro]*0.25
        elif ContDinheiro == 1:
            valor_total += quantidade_dinheiro[0][ContDinheiro]*0.50
        elif ContDinheiro == 2:
            valor_total += quantidade_dinheiro[0][ContDinheiro]*1.00
        
    quantidade_dinheiro[3][0] += valor_total 
    print("Dinheiro Total na máquina: ", quantidade_dinheiro[3][0])

def modificar_quantidade_dinheiro_cedula():
    print("Modificar quantidade de cédulas:")
    tipos = ["R$2.00", "R$5.00", "R$10.00"]
    valor_total = 0

    for ContDinheiro in range(len(tipos)):
        print("Cédulas:")
        try:
            quantidade_dinheiro[1][ContDinheiro] = int(input(f"Digite a nova quantidade de cédulas de {tipos[ContDinheiro]}: "))
        except ValueError:
            print("Digite um número inteiro por favor!")
            return
            
        if ContDinheiro == 0:
            valor_total += quantidade_dinheiro[0][ContDinheiro]*2
        elif ContDinheiro == 1:
            valor_total += quantidade_dinheiro[0][ContDinheiro]*5
        elif ContDinheiro == 2:
            valor_total += quantidade_dinheiro[0][ContDinheiro]*10
        
    quantidade_dinheiro[3][0] += valor_total 
    print("Dinheiro Total na máquina: ", quantidade_dinheiro[3][0])

def visualizar_relatorios():
    # Relatório de vendas
    print("Relatório de pagamentos:")
    escolha = input("1. Pagamentos PIX\n2. Pagamentos Dinheiro\n3. Obter todo relatório.\n")

    if escolha == "1":
        print("\n\n")
        total_vendas = 0
        for i in range(len(pagamentos_pix)):
            total_vendas += pagamentos_pix[i][0]

        print(f"Total de vendas:{total_vendas}\nUltimos pagamentos:")
        print("---------------------------------------------------------------------")
        for i in range(len(pagamentos_pix)):
            print(f"Número do pix enviado: {pagamentos_pix[i][1]}\nValor enviado: {pagamentos_pix[i][0]}\n")
        print("---------------------------------------------------------------------")
    elif escolha == "2":
        print("\n\n")
        total_vendas = 0

        for i in range(len(pagamentos_dinheiro)):
            total_vendas += pagamentos_dinheiro[i][0]

        print(f"Total de vendas:{total_vendas}\nUltimos pagamentos:")
        print("---------------------------------------------------------------------")

        for i in range(len(pagamentos_dinheiro)):
            print(f"Valor Pago: {pagamentos_dinheiro[i][0]}\nTroco dado: {pagamentos_dinheiro[i][1]}\n")
        print("---------------------------------------------------------------------")
    elif escolha == "3":
        print("\n\n")
        total_vendas_pix = 0
        total_vendas_dinheiro = 0

        for i in range(len(pagamentos_pix)):
            total_vendas_pix += pagamentos_pix[i][0]

        for i in range(len(pagamentos_dinheiro)):
            total_vendas_dinheiro += pagamentos_dinheiro[i][0]

        print(f"Total de vendas PIX:{total_vendas_pix}\n")
        print(f"Total de vendas Dinheiro:{total_vendas_dinheiro}\n")
        print("---------------------------------------------------------------------")
        print("Ultimas vendas Dinheiro:")

        print("---------------------------------------------------------------------")
        for i in range(len(pagamentos_dinheiro)):
            print(f"Valor Pago: {pagamentos_dinheiro[i][0]}\nTroco dado: {pagamentos_dinheiro[i][1]}\n")
        print("---------------------------------------------------------------------")

        print("Ultimas vendas Pix:")
        print("---------------------------------------------------------------------")
        for i in range(len(pagamentos_pix)):
            print(f"Número do pix enviado: {pagamentos_pix[i][1]}\nValor enviado: {pagamentos_pix[i][0]}\n")
        print("---------------------------------------------------------------------")
    else:
        print("Opção inválida.")

def atualizar_quantidade_dinheiro(valor_inserido):
    if valor_inserido == "1":
        quantidade_dinheiro[0][0]+1
        quantidade_dinheiro[3][0] += quantidade_dinheiro[0][0]*0.25
        return 0.25
    elif valor_inserido == "2":
        quantidade_dinheiro[0][1]+1
        quantidade_dinheiro[3][0] += quantidade_dinheiro[0][1]*0.50
        return 0.50
    elif valor_inserido == "3":
        quantidade_dinheiro[0][2]+1
        quantidade_dinheiro[3][0] += quantidade_dinheiro[0][2]*1.00
        return 1.00
    elif valor_inserido == "4":
        quantidade_dinheiro[1][0]+1
        quantidade_dinheiro[3][0] += quantidade_dinheiro[1][0]*2.00
        return 2.00
    elif valor_inserido == "5":
        quantidade_dinheiro[1][1]+1
        quantidade_dinheiro[3][0] += quantidade_dinheiro[1][1]*5.00
        return 5.00
    elif valor_inserido == "6":
        quantidade_dinheiro[1][2]+1
        quantidade_dinheiro[3][0] += quantidade_dinheiro[1][2]*10.00
        return 10.00
    else:
        return 0
    
    # Implementar a lógica para atualizar a quantidade de dinheiro, por exemplo o usuario recebeu troco, tem que diminuir e se comprou tem que aumentar
    # return
    # if valor_inserido in [0.25, 0.5, 1.0, 2.0, 5.0, 10.0]:
    #     if valor_inserido == 0.25:
    #         quantidade_dinheiro[0][0] += 1
    #     elif valor_inserido == 0.50:
    #         quantidade_dinheiro[0][1] += 1
    #     elif valor_inserido == 1.0:
    #         quantidade_dinheiro[0][2] += 1
    #     elif valor_inserido == 2.0:
    #         quantidade_dinheiro[1][0] += 1
    #     elif valor_inserido == 5.0:
    #         quantidade_dinheiro[1][1] += 1
    #     elif valor_inserido == 10.0:
    #         quantidade_dinheiro[1][2] += 1

def realizar_pagamento(refrigerante, quantidade, opcao_pagamento):
    preco_unitario = 0
    valor_pago = 0 

    if opcao_pagamento == 1:

        if refrigerante == "1" and quantidade <= produtos[0][1]:
            preco_unitario = produtos[0][2]
            produtos[0][1] = produtos[0][1] - quantidade
        elif refrigerante == "2" and quantidade <= produtos[1][1]:
            preco_unitario = produtos[1][2]
            produtos[1][1] = produtos[1][1] - quantidade
        elif refrigerante =="3" and quantidade <= produtos[2][1]:
            preco_unitario = produtos[2][2]
            produtos[2][1] = produtos[2][1] - quantidade
        else:
           return print("Quantidade acima da disponível")

        valor_total = quantidade * preco_unitario

        print("Digite o telefone nesse padrão: ** *********")
        telefone = input("Digite o numéro de telefone referente ao seu pix: ")
        while len(telefone) != len(telefone_valido):
            print("Digite o telefone nesse padrão: ** *********")
            telefone = input("Digite o numéro de telefone referente ao seu pix: ")

        print("Valor total da compra: ", valor_total)
        valor_pago = float(input("Digite o valor a ser pago: "))

        if valor_pago == valor_total:
            pix = [valor_pago, telefone]
            pagamentos_pix.append(pix)
            quantidade_dinheiro[2][0] += valor_pago
            relatorios_de_pagamento.append(pagamentos_pix)
            print("Pagamento realizado com sucesso.")
        elif valor_pago != valor_total:
            print("Insira o valor correto!! >:(")
            realizar_pagamento(refrigerante, quantidade, opcao_pagamento)
        return

    elif opcao_pagamento == 2:

        if refrigerante == "1" and quantidade <= produtos[0][1]:
            preco_unitario = produtos[0][2]
            produtos[0][1] = produtos[0][1] - quantidade
        elif refrigerante == "2" and quantidade <= produtos[1][1]:
            preco_unitario = produtos[1][2]
            produtos[1][1] = produtos[1][1] - quantidade
        elif refrigerante =="3" and quantidade <= produtos[2][1]:
            preco_unitario = produtos[2][2]
            produtos[2][1] = produtos[2][1] - quantidade
        else:
           return print("Quantidade acima da disponível")
        
        valor_total = quantidade * preco_unitario
        print("Valor a ser pago: ", valor_total)

        while valor_pago < valor_total:
            valor_inserido = input("Digite o valor inserido em cédulas ou moedas até atingir o valor total da compra: \n1. 0.25\n2. 0.50\n3. 1.00\n4. 2.00\n5. 5.00\n6. 10.00\n")
            valor_pago += atualizar_quantidade_dinheiro(valor_inserido)
            
            valor_em_falta = 0
            if (valor_total - valor_pago) < 0:
                valor_em_falta = 0

                troco = valor_pago - valor_total
                if troco >= 0:
                    pagamentos_dinheiro.append([valor_total, troco])
                    print("Pagamento em dinheiro efetuado, seu troco é de: ",troco)
                    quantidade_dinheiro[3][0] += valor_total
                    print(f"Entregar {quantidade} unidade(s) do produto {refrigerante}")
                else:
                    print("Troco indisponivel para o valor inserido")
                    continue
            else:
                valor_em_falta = valor_total - valor_pago
                print("Valor em falta: ", valor_em_falta)
            # if verificar_troco_disponivel(valor_total, valor_inserido):
                
            # else:
            #     print("Não é possível efetuar esse pagamento, pois não temos troco disponivel.")
            
    else:
        print("Opção de pagamento inválida")

def verificar_troco_disponivel(valor_total, valor_inserido):
    simulacao_vlr_pago = 0

    if valor_inserido == "1":
        simulacao_vlr_pago += 0.25
    elif valor_inserido == "2":
        simulacao_vlr_pago += 0.50
    elif valor_inserido == "3":
        simulacao_vlr_pago += 1.00
    elif valor_inserido == "4":
        simulacao_vlr_pago += 2.00
    elif valor_inserido == "5":
        simulacao_vlr_pago += 5.00
    elif valor_inserido == "6":
        simulacao_vlr_pago += 10.00

    if quantidade_dinheiro[3][0] <= abs(valor_total - simulacao_vlr_pago):
        return False
    else:
        return True
                

def main():
    while True:
        print("Bem-vindo(a) ao Sistema de Pagamentos da Máquina de Venda Automática!")
        print("Selecione uma opção:")
        print("1. Administrador")
        print("2. Consumidor")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            algarismos_validos = [1, 2, 3, 4, 5, '1', '2', '3', '4', '5']
            usuario = "Administrador"
            senha = input("Senha: ")

            if login(usuario, senha):
                print("Selecione uma opção:")
                print("1. Visualizar produtos no estoque")
                print("2. Adicionar produtos no estoque")
                print("3. Visualizar quantidade de dinheiro")
                print("4. Modificar quantidade de dinheiro")
                print("5. Visualizar relatórios de pagamento")
                opcao_adm = input("Digite uma opção:")
                if opcao_adm == "1":
                    visualizar_produtos()
                elif opcao_adm == "2":
                    refrigerante = input(f"Digite o número do refrigerante desejado: \n1. {produtos[0][0]}\n2. {produtos[1][0]}\n3. {produtos[2][0]}\n")
                    if refrigerante == "1" or refrigerante == "2" or refrigerante == "3":
                        quantidade = int(input("Digite a quantidade que quer adicionar ao estoque: "))
                        adicionar_estoque(refrigerante, quantidade)
                    else:
                        print("Valor inválido.")
                elif opcao_adm == "3":
                    visualizar_quantidade_dinheiro()
                elif opcao_adm == "4":
                    escolha = input("Escolha:\n1. Moeda\n2. Cedula\n")
                    if escolha == "1":
                        modificar_quantidade_dinheiro_moeda()
                    elif escolha == "2":
                        modificar_quantidade_dinheiro_cedula()
                    else:
                        print("Escolha inválida.")
                elif opcao_adm == "5":
                    visualizar_relatorios()
                elif opcao_adm != algarismos_validos:
                    print("Digite uma opção válida!")

        elif opcao == "2":
            print("Login do consumidor bem-sucedido.")
            visualizar_produtos()
            refrigerante = (input("Digite o número do refrigerante desejado: "))
            if refrigerante == "1":
                quantidade = int(input("Digite a quantidade desejada: "))

                if produtos[0][1] >= quantidade:
                    print("Selecione uma opção de pagamento:")
                    print("1. PIX")
                    print("2. Dinheiro")
                    opcao_pagamento = int(input("Opção de pagamento: "))
                    realizar_pagamento(refrigerante, quantidade, opcao_pagamento)
                else:
                    print(f"Produto selecionado não possui {quantidade} de estoque")
            elif refrigerante == "2":
                quantidade = int(input("Digite a quantidade desejada: "))

                if produtos[1][1] >= quantidade:
                    print("Selecione uma opção de pagamento:")
                    print("1. PIX")
                    print("2. Dinheiro")
                    opcao_pagamento = int(input("Opção de pagamento: "))
                    realizar_pagamento(refrigerante, quantidade, opcao_pagamento)
                else:
                    print(f"Produto selecionado não possui {quantidade} de estoque")
            elif refrigerante == "3":
                quantidade = int(input("Digite a quantidade desejada: "))

                if produtos[2][1] >= quantidade:
                    print("Selecione uma opção de pagamento:")
                    print("1. PIX")
                    print("2. Dinheiro")
                    opcao_pagamento = int(input("Opção de pagamento: "))
                    realizar_pagamento(refrigerante, quantidade, opcao_pagamento)
                else:
                    print(f"Produto selecionado não possui {quantidade} de estoque")
            else:
                print("Selecione um valor válido.")
        elif opcao == "3":
            print("Obrigado por utilizar o Sistema de Pagamentos da Máquina de Venda Automática!")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

main()

