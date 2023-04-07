# Programa: Vending Machine
# Autor: Rafael Galafassi
# Data de criação: 07/04/2023
# Descrição: Programa que simula uma máquina de vendas.

while True:
    # Exibe mensagem de boas-vindas
    print("Bem-vindo(a) à máquina de Refrigerantes!")
    print("Digite o tipo de usuário que você é:")

    usuario = input("ADMINISTRADOR OU CONSUMIDOR: ")

    # Verifica se o tipo de usuário é válido e exibe mensagem
    if usuario == "ADMINISTRADOR" or usuario == "CONSUMIDOR":
        print(f"Ok, você entrou como {usuario}")
    else:
        print("Entrada inválida tente novamente")
        continue

    # Inicializa as variáveis que serão utilizadas na operação
    troco = 0
    qtdeProduto1 = 0
    qtdeProduto1Vendido = 0
    valorCompra = 0
    totalCedulas = 0
    totalMoedas = 0
    novoTotalCedulas = 0

    if usuario == "ADMINISTRADOR":
        # Se o usuário for administrador, solicita a senha para habilitar o sistema
        senha = int(input("Digite a senha para habilitar o sistema: "))
        if senha == 1234:
            # Exibe as opções disponíveis para o administrador
            print("Selecione a opção (1) para atualizar o troco na máquina ou (2) para atualizar o estoque de produtos ou (3) para ver a quantidade de dinheiro das vendas: ")
            dinheiro = input(
                "1) Atualizar troco ou 2) Atualizar estoque de produtos ou 3) Valor das vendas: ")
            # Se a opção selecionada for atualizar o troco na máquina
            if dinheiro == "1":
                # Solicita a quantidade de cédulas de cada valor e atualiza o total em dinheiro da máquina
                print("Digite a quantidade de cédulas")
                qtdeCedulas2 = int(
                    input("Digite a quantidade de notas de 2: "))
                qtdeCedulas5 = int(
                    input("Digite a quantidade de notas de 5: "))
                qtdeCedulas10 = int(
                    input("Digite a quantidade de notas de 10: "))
                qtdeCedulas20 = int(
                    input("Digite a quantidade de notas de 20: "))
                novoTotalCedulas = (qtdeCedulas2*2) + (qtdeCedulas5*5) + \
                    (qtdeCedulas10*10) + (qtdeCedulas20*20)
                totalCedulas = novoTotalCedulas
                print(
                    f"A quantidade de cédulas de 2 reais é de: {qtdeCedulas2}")
                print(
                    f"A quantidade de cédulas de 5 reais é de: {qtdeCedulas5}")
                print(
                    f"A quantidade de cédulas de 10 reais é de: {qtdeCedulas10}")
                print(
                    f"A quantidade de cédulas de 20 reais é de: {qtdeCedulas20}")
                print(
                    f"O total de dinheiro em cedulas na máquina é de R${totalCedulas}")
                # Solicita a quantidade de moedas de cada valor e atualiza o total em dinheiro da máquina
                print("Digite a quantidade de moedas")
                qtdeMoedas5 = int(
                    input("Digite a quantidade de moedas de 5 centavos: "))
                qtdeMoedas10 = int(
                    input("Digite a quantidade de moedas de 10 centavos: "))
                qtdeMoedas25 = int(
                    input("Digite a quantidade de moedas de 25 centavos: "))
                qtdeMoedas50 = int(
                    input("Digite a quantidade de moedas de 50 centavos: "))
                qtdeMoedas1 = int(
                    input("Digite a quantidade de moedas de 1 real: "))
                novoTotalMoedas = ((qtdeMoedas5*5)/100) + ((qtdeMoedas10*10)/100) + \
                    ((qtdeMoedas25*25)/100) + \
                    ((qtdeMoedas50*50)/100) + (qtdeMoedas1*1)
                totalMoedas = novoTotalMoedas
                print(
                    f"A quantidade de moedas de 5 centavos é de: {qtdeMoedas5}")
                print(
                    f"A quantidade de moedas de 10 centavos é de: {qtdeMoedas10}")
                print(
                    f"A quantidade de moedas de 25 centavos é de: {qtdeMoedas25}")
                print(
                    f"A quantidade de moedas de 50 centavos é de: {qtdeMoedas50}")
                print(f"A quantidade de moedas de 1 real é de: {qtdeMoedas1}")
                print(
                    f"O total de dinheiro em moedas na máquina é de R${totalMoedas:.2f}")
                # Atualiza a quantidade de troco disponível na máquina
                novo_troco = (totalCedulas + totalMoedas)
                print(f"O total de troco na máquina é de R${novo_troco:.2f}")
                troco = novo_troco
                print("Troco atualizado com sucesso!")
            # Atualiza o estoque da máquina
            elif dinheiro == "2":
                print(qtdeProduto1)
                novaQtdeProduto1 = int(
                    input("Adicione mais unidades de Coca-Cola ao estoque:"))
                qtdeProduto1 = novaQtdeProduto1
            # Verifica o valor recebido das vendas durante o funcionamento da máquina
            elif dinheiro == "3":
                print("O valor recebido das vendas do produto 1 é igual a: R$",
                      (qtdeProduto1Vendido*4))
            # Verifica se usuario selecionou uma opção válida
            else:
                print("Opção inválida digite novamente")
                continue
        else:
            print("Senha inválida")
            continue
    # Verifica se o usuário é consumidor
    elif usuario == "CONSUMIDOR":
        # Apresenta informações de pagamento e produtos disponíveis
        print("Selecione o produto que deseja comprar, somente cédulas até R$20 e/ou moedas são aceitas para efetuar o pagamento.")
        produto = input("1) Coca-Cola R$ 4.00: ")
        # Verifica qual produto o consumidor escolheu e quantas unidades irá comprar
        if produto == "1":
            qtdeCompraProduto1 = int(
                input("Quantas unidades de Coca gostaria de comprar: "))
            # Verifica se tem estoque do produto para o consumidor comprar
            if int(qtdeCompraProduto1) > int(qtdeProduto1):
                print(
                    f"Infelizmente só temos {qtdeProduto1} unidades desse produto, tente novamente.")
                continue
            # Se tiver estoque mostra o valor toral da compra ao consumidor
            else:
                qtdeProduto1Vendido = (
                    int(qtdeProduto1) - int(qtdeCompraProduto1))
                valorCompra = (4 * qtdeCompraProduto1)
                print(
                    f"O total do valor da compra ficou igual a: R${valorCompra:.2f}")
        else:
            print("Entrada inválida, tente novamente")
            continue
        # Apresenta as formas de pagamento ao consumidor
        print("Selecione as formas de pagamento abaixo:")
        pagamento = input("1) Cédulas ou 2) Moedas ou 3) Cédulas e Moedas: ")
        # Verifica a opção de pagamento escolhida pelo consumidor
        if pagamento == "1":
            # Recebe os valores em cédulas digitados pelo consumidor
            print("Digite a quantidade de cédulas para o pagamento")
            qtdeCedulas2 = int(input("Digite a quantidade de notas de 2: "))
            qtdeCedulas5 = int(input("Digite a quantidade de notas de 5: "))
            qtdeCedulas10 = int(input("Digite a quantidade de notas de 10: "))
            qtdeCedulas20 = int(input("Digite a quantidade de notas de 20: "))
            totalRecebido = (qtdeCedulas2*2) + (qtdeCedulas5*5) + \
                (qtdeCedulas10*10) + (qtdeCedulas20*20)
            # Verifica se tem troco para finalizar a compra
            if float(troco) < totalRecebido:
                print("Não foi possível realizar a compra")
            elif totalRecebido > valorCompra:
                troco = totalRecebido - valorCompra
                print(
                    f"Seu troco é de R${troco}, boa compra e receba suas {qtdeCompraProduto1} Coca-Colas")
            elif totalRecebido == valorCompra:
                print(
                    f"Sem troco, boa compra e receba suas {qtdeCompraProduto1} Coca-Colas")
            else:
                divida = (valorCompra-totalRecebido)
                print(
                    f"Falta R${divida} para finalizar a compra, insira mais cédulas")
        elif pagamento == "2":
            # Recebe os valores em moedas digitados pelo consumidor
            print("Digite a quantidade de moedas para o pagamento")
            qtdeMoedas5 = int(
                input("Digite a quantidade de moedas de 5 centavos: "))
            qtdeMoedas10 = int(
                input("Digite a quantidade de moedas de 10 centavos: "))
            qtdeMoedas25 = int(
                input("Digite a quantidade de moedas de 25 centavos: "))
            qtdeMoedas50 = int(
                input("Digite a quantidade de moedas de 50 centavos: "))
            qtdeMoedas1 = int(
                input("Digite a quantidade de moedas de 1 real: "))
            totalRecebido = ((qtdeMoedas5*5)/100) + ((qtdeMoedas10*10)/100) + \
                ((qtdeMoedas25*25)/100) + \
                ((qtdeMoedas50*50)/100) + (qtdeMoedas1*1)
            # Verifica se tem troco para finalizar a compra
            if float(troco) < totalRecebido:
                print("Não foi possível realizar a compra")
            elif totalRecebido > valorCompra:
                troco = totalRecebido - valorCompra
                print(
                    f"Seu troco é de R${troco}, boa compra e receba suas {qtdeCompraProduto1} Coca-Colas")
            elif totalRecebido == valorCompra:
                print(
                    f"Sem troco, boa compra e receba suas {qtdeCompraProduto1} Coca-Colas")
            else:
                divida = (valorCompra-totalRecebido)
                print(
                    f"Falta R${divida} para finalizar a compra, insira mais cédulas")
        elif pagamento == "3":
            # Recebe os valores em cédulas e moedas digitados pelo consumidor
            print("Digite a quantidade de cédulas para o pagamento")
            qtdeCedulas2 = int(input("Digite a quantidade de notas de 2: "))
            qtdeCedulas5 = int(input("Digite a quantidade de notas de 5: "))
            qtdeCedulas10 = int(input("Digite a quantidade de notas de 10: "))
            qtdeCedulas20 = int(input("Digite a quantidade de notas de 20: "))
            totalRecebidoCedulas = (
                qtdeCedulas2*2) + (qtdeCedulas5*5) + (qtdeCedulas10*10) + (qtdeCedulas20*20)
            print("Digite a quantidade de moedas para o pagamento")
            qtdeMoedas5 = int(
                input("Digite a quantidade de moedas de 5 centavos: "))
            qtdeMoedas10 = int(
                input("Digite a quantidade de moedas de 10 centavos: "))
            qtdeMoedas25 = int(
                input("Digite a quantidade de moedas de 25 centavos: "))
            qtdeMoedas50 = int(
                input("Digite a quantidade de moedas de 50 centavos: "))
            qtdeMoedas1 = int(
                input("Digite a quantidade de moedas de 1 real: "))
            totalRecebidoMoedas = ((qtdeMoedas5*5)/100) + ((qtdeMoedas10*10)/100) + (
                (qtdeMoedas25*25)/100) + ((qtdeMoedas50*50)/100) + (qtdeMoedas1*1)
            totalRecebido = totalRecebidoCedulas + totalRecebidoMoedas
            # Verifica se tem troco para finalizar a compra
            if float(troco) < totalRecebido:
                print("Não foi possível realizar a compra")
            elif totalRecebido > valorCompra:
                troco = totalRecebido - valorCompra
                print(
                    f"Seu troco é de R${troco}, boa compra e receba suas {qtdeCompraProduto1} Coca-Colas")
            elif totalRecebido == valorCompra:
                print(
                    f"Sem troco, boa compra e receba suas {qtdeCompraProduto1} Coca-Colas")
            else:
                divida = (valorCompra-totalRecebido)
                print(
                    f"Falta R${divida} para finalizar a compra, insira mais cédulas")
        else:
            print("Opção inválida, tente novamente")
            continue
    # Mostra mensagem de agradecimento, finaliza a compra e pede se o consumidor quer realizar outra ou encerra o programa
    print("Obrigado por utilizar nossa máquina de refrigerantes")
    continuar = input("Deseja realizar outra compra? (SIM ou NÃO): ")
    if continuar == "SIM":
        print("Ok, vamos fazer outra compra!")
    elif continuar == "NÃO":
        print("Obrigado por utilizar nosso programa!")
        break
    # Verifica se a opção é válida
    else:
        print("Opção inválida. Digite 'SIM' para continuar ou 'NÃO' para sair.")
