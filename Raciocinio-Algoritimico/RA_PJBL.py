# Programa: Vending Machine
# Autor: Rafael Galafassi, Vinicius Costa, Marcos Vincius e Vinicius Viana
# Data de criação: 07/04/2023
# Descrição: Programa que simula uma máquina de vendas.
# Observação: Números, pontos e ENTER serão as únicas formas de entrada pelos usuários.

# Declara as variáveis que serão utilizadas no programa
troco = 0
qtdeProduto1 = 0
qtdeProduto1Vendido = 0
valorCompra = 0
totalCedulas = 0
totalMoedas = 0
novoTotalCedulas = 0

# inicializa o loop continuo do programa
while True:
    # Exibe mensagem de boas-vindas e recebe o dado do tipo de usuário
    print("------------------------------------------------------------")
    print("Bem-vindo(a) à máquina de Refrigerantes!")
    print("------------------------------------------------------------")
    print("Digite o tipo de usuário que você é:")

    usuario = input("\n1) ADMINISTRADOR\n2) CONSUMIDOR\n")

    # Verifica se o tipo de usuário é válido e exibe uma resposta
    print("------------------------------------------------------------")
    if usuario == "1" or usuario == "2":
        print(f"Ok, você entrou como usuário {usuario}")
    else:
        print("Usuário inválido, tente novamente")
        continue
    print("------------------------------------------------------------")
    # Se o usuário for administrador habilita as funcionalidades para gerenciar a máquina
    if usuario == "1":
        # solicita a senha para habilitar o sistema
        senha = int(input("Digite a senha para habilitar o sistema: "))
        if senha == 1234:
            # Exibe as opções disponíveis para o administrador
            print("------------------------------------------------------------")
            opcaoAdm = input(
                "Selecione a opção:\n(1) para atualizar o troco na máquina\n(2) para atualizar o estoque de produtos\n(3) para ver a quantidade de dinheiro das vendas\n")
            # Se a opção selecionada for equivalente a 1, o troco será atualizado por tipo e quantidade.
            if opcaoAdm == "1":
                # Solicita a quantidade de cédulas de cada valor e atualiza o total em dinheiro da máquina
                print("------------------------------------------------------------")
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
                print("------------------------------------------------------------")
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
                print("------------------------------------------------------------")
                novo_troco = (totalCedulas + totalMoedas)
                print(f"O total de troco na máquina é de R${novo_troco:.2f}")
                troco = novo_troco
                print("Troco atualizado com sucesso!")
                print("------------------------------------------------------------")
            # Se a opção selecionada for equivalente a 2, o estoque será atualizado por tipo e quantidade de produtos disponíveis.
            elif opcaoAdm == "2":
                print("------------------------------------------------------------")
                print(
                    "A quantidade de unidade(s) de Coca-Cola atual em estoque é igual a: ", qtdeProduto1)
                print("------------------------------------------------------------")
                novaQtdeProduto1 = int(
                    input("Adicione mais unidade(s) de Coca-Cola ao estoque: "))
                qtdeProduto1 = novaQtdeProduto1
                print("Estoque atualizado com sucesso!")
                print("------------------------------------------------------------")
            # Verifica o valor recebido das vendas por produto e valor total durante o funcionamento da máquina
            elif opcaoAdm == "3":
                print("O valor recebido das vendas de Coca-Cola é igual a: R$",
                      (qtdeProduto1Vendido*4))
                print("O valor total das vendas é igual a: R$",
                      (qtdeProduto1Vendido*4))
            # Verifica se usuario selecionou uma opção válida de entrada, caso contrário retorna ao início do loop
            else:
                print("Opção inválida, tente novamente")
                continue
        else:
            print("Senha inválida, tente novamente")
            continue
    # Se o usuário for consumidor habilita as funcionalidades para realizar as compras
    elif usuario == "2":
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
            # Se tiver estoque mostra o valor total da compra ao consumidor
            else:
                qtdeProduto1Vendido = (
                    int(qtdeProduto1) - int(qtdeCompraProduto1))
                valorCompra = (4 * qtdeCompraProduto1)
                print(
                    f"O valor total da compra ficou igual a: R${valorCompra:.2f}")
        else:
            print("Opção inválida, tente novamente")
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
    print("Obrigado por utilizar nossa máquina de refrigerantes!")
    print("------------------------------------------------------------")

    continuar = input("Deseja realizar outra operação? (1) SIM ou (2) NÃO: ")
    if continuar == "1":
        print("Ok, vamos fazer outra compra!")
    elif continuar == "2":
        print("Obrigado por utilizar nosso programa!")
        break
    # Verifica se a opção é válida
    else:
        print("Opção inválida. Digite (1) para continuar ou (2) para sair.")
    print("------------------------------------------------------------")
