# Programa: Vending Machine
# Autor: Rafael Galafassi, Vinicius Costa, Marcos Vincius e Vinicius Viana
# Data de criação: 07/04/2023
# Descrição: Programa que simula uma máquina de vendas.
# Observação: Números, pontos e ENTER serão as únicas formas de entrada pelos usuários.

# Declara as variáveis que serão utilizadas no programa.
# Produtos
qtdeProdutoAgua = 0
qtdeProdutoAguaVendido = 0
qtdeProdutoCha = 0
qtdeProdutoChaVendido = 0
qtdeProdutoGuarana = 0
qtdeProdutoGuaranaVendido = 0
qtdeProdutoCoca = 0
qtdeProdutoCocaVendido = 0
# Dados
troco = 0
valorCompra = 0
totalCedulas = 0
totalMoedas = 0
novoTotalCedulas = 0
senha = ""

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
        senha = input("Digite a senha para habilitar o sistema: ")
        while senha != "1234":
            print("Senha inválida, tente novamente")
            senha = input("Digite a senha para habilitar o sistema: ")
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
            # Coca
            print(
                "A quantidade de unidade(s) de Coca-Cola atual em estoque é igual a: ", qtdeProdutoCoca)
            print("------------------------------------------------------------")
            novaqtdeProdutoCoca = int(
                input("Adicione mais unidade(s) de Coca-Cola ao estoque: "))
            qtdeProdutoCoca += novaqtdeProdutoCoca
            # Guaraná
            print("A quantidade de unidade(s) de Guaraná atual em estoque é igual a: ",
                  qtdeProdutoGuarana)
            print("------------------------------------------------------------")
            novaqtdeProdutoGuarana = int(
                input("Adicione mais unidade(s) de Guaraná ao estoque: "))
            qtdeProdutoGuarana += novaqtdeProdutoGuarana
            # Chá
            print(
                "A quantidade de unidade(s) de Chá atual em estoque é igual a: ", qtdeProdutoCha)
            print("------------------------------------------------------------")
            novaqtdeProdutoCha = int(
                input("Adicione mais unidade(s) de Chá ao estoque: "))
            qtdeProdutoCha += novaqtdeProdutoCha
            # Água
            print(
                "A quantidade de unidade(s) de Água atual em estoque é igual a: ", qtdeProdutoAgua)
            print("------------------------------------------------------------")
            novaqtdeProdutoAgua = int(
                input("Adicione mais unidade(s) de Água ao estoque: "))
            qtdeProdutoAgua += novaqtdeProdutoAgua
            print("Estoque atualizado com sucesso!")
            print("------------------------------------------------------------")
        # Verifica o valor recebido das vendas por produto e valor total durante o funcionamento da máquina
        elif opcaoAdm == "3":
            print("O valor recebido das vendas de Coca-Cola é igual a: R$",
                  (qtdeProdutoCocaVendido*4))
            print("O valor recebido das vendas de Guaraná é igual a: R$",
                  (qtdeProdutoGuaranaVendido*4))
            print("O valor recebido das vendas de Chá é igual a: R$",
                  (qtdeProdutoChaVendido*3))
            print("O valor recebido das vendas de Água é igual a: R$",
                  (qtdeProdutoAguaVendido*2))
            print("O valor total das vendas é igual a: R$", ((qtdeProdutoCocaVendido*4) +
                  (qtdeProdutoGuaranaVendido*4) + (qtdeProdutoChaVendido*3) + (qtdeProdutoAguaVendido*2)))
        # Verifica se usuario selecionou uma opção válida de entrada, caso contrário retorna ao início do loop
        else:
            print("Opção inválida, tente novamente")
            continue
    # Se o usuário for consumidor habilita as funcionalidades para realizar as compras
    elif usuario == "2":
        # Apresenta informações de pagamento e produtos disponíveis
        print("Selecione o produto que deseja comprar, somente cédulas até R$20 e/ou moedas são aceitas para efetuar o pagamento.")
        produto = input(
            "1) Coca-Cola R$ 4.00\n2) Guaraná R$ 4.00\n3) Chá R$ 3.00\n4) Água R$ 2.00\n")
        # Verifica qual produto o consumidor escolheu e quantas unidades irá comprar
        if produto == "1":
            qtdeCompraCoca = int(
                input("Quantas unidades de Coca gostaria de comprar: "))
            # Verifica se tem estoque do produto para o consumidor comprar
            if int(qtdeCompraCoca) > int(qtdeProdutoCoca):
                print(
                    f"Infelizmente só temos {qtdeProdutoCoca} unidades desse produto, tente novamente.")
                continue
            # Se tiver estoque mostra o valor total da compra ao consumidor
            else:
                qtdeProdutoCocaVendido = (
                    int(qtdeProdutoCoca) - int(qtdeCompraCoca))
                valorCompra = (4 * qtdeCompraCoca)
                print(
                    f"O valor total da compra ficou igual a: R${valorCompra:.2f}")
        elif produto == "2":
            qtdeCompraGuarana = int(
                input("Quantas unidades de Guaraná gostaria de comprar: "))
            # Verifica se tem estoque do produto para o consumidor comprar
            if int(qtdeCompraGuarana) > int(qtdeProdutoGuarana):
                print(
                    f"Infelizmente só temos {qtdeProdutoGuarana} unidades desse produto, tente novamente.")
                continue
            # Se tiver estoque mostra o valor total da compra ao consumidor
            else:
                qtdeProdutoGuaranaVendido = (
                    int(qtdeProdutoGuarana) - int(qtdeCompraGuarana))
                valorCompra = (4 * qtdeCompraGuarana)
                print(
                    f"O valor total da compra ficou igual a: R${valorCompra:.2f}")
        elif produto == "3":
            qtdeCompraCha = int(
                input("Quantas unidades de Chá gostaria de comprar: "))
            # Verifica se tem estoque do produto para o consumidor comprar
            if int(qtdeCompraCha) > int(qtdeProdutoCha):
                print(
                    f"Infelizmente só temos {qtdeProdutoCha} unidades desse produto, tente novamente.")
                continue
            # Se tiver estoque mostra o valor total da compra ao consumidor
            else:
                qtdeProdutoChaVendido = (
                    int(qtdeProdutoCha) - int(qtdeCompraCha))
                valorCompra = (3 * qtdeCompraCha)
                print(
                    f"O valor total da compra ficou igual a: R${valorCompra:.2f}")
        elif produto == "4":
            qtdeCompraAgua = int(
                input("Quantas unidades de Água gostaria de comprar: "))
            # Verifica se tem estoque do produto para o consumidor comprar
            if int(qtdeCompraAgua) > int(qtdeProdutoAgua):
                print(
                    f"Infelizmente só temos {qtdeProdutoAgua} unidades desse produto, tente novamente.")
                continue
            # Se tiver estoque mostra o valor total da compra ao consumidor
            else:
                qtdeProdutoAguaVendido = (
                    int(qtdeProdutoAgua) - int(qtdeCompraAgua))
                valorCompra = (2 * qtdeCompraAgua)
                print(
                    f"O valor total da compra ficou igual a: R${valorCompra:.2f}")
        else:
            print("Opção inválida, tente novamente")
            continue

        # Apresenta as formas de pagamento ao consumidor
        print("Digite o numero correspondente ao dinheiro para pagar:")
        
        continuar_loop = True

        while continuar_loop:
            print("----------------------------------------------------------------")
            dinheiro_inserido = int(input("1 - Moeda R$0,05\n2 - Moeda R$0,10\n3 - Moeda R$0,25\n4 - Moeda R$0,50\n5 - Moeda R$1,00\n6 - Nota R$2,00\n7 - Nota R$5,00\n8 - Nota R$10,00\n9 - Nota R$20,00\n10 - Nota R$50,00\n===================================================\nValor: "))
            print("----------------------------------------------------------------")

            if dinheiro_inserido == 1:
                if valorCompra < 0.05: 
                    print("\nValor informado é maior que o valor total da compra:", round(valorCompra, 2), "-----(POR FAVOR INSIRA OUTRO VALOR)")
                else:
                    valorCompra -= 0.05
            elif dinheiro_inserido == 2:
                if valorCompra < 0.10: 
                    print("\nValor informado é maior que o valor total da compra:", round(valorCompra, 2), "-----(POR FAVOR INSIRA OUTRO VALOR)")
                else:
                    valorCompra -= 0.10 
            elif dinheiro_inserido == 3:
                if valorCompra < 0.25:
                    print("\nValor informado é maior que o valor total da compra:", round(valorCompra, 2), "-----(POR FAVOR INSIRA OUTRO VALOR)")
                else:
                    valorCompra -= 0.25
            elif dinheiro_inserido == 4:
                if valorCompra < 0.50:
                    print("\nValor informado é maior que o valor total da compra:", round(valorCompra, 2), "-----(POR FAVOR INSIRA OUTRO VALOR)")
                else:
                    valorCompra -= 0.50
            elif dinheiro_inserido == 5:
                if valorCompra < 1.00:
                    print("\nValor informado é maior que o valor total da compra:", round(valorCompra, 2), "-----(POR FAVOR INSIRA OUTRO VALOR)")
                else:
                    valorCompra -= 1.00
            elif dinheiro_inserido == 6:
                if valorCompra < 2:
                    print("\nValor informado é maior que o valor total da compra:", round(valorCompra, 2), "-----(POR FAVOR INSIRA OUTRO VALOR)")
                else:
                    valorCompra -= 2
            elif dinheiro_inserido == 7:
                if valorCompra < 5:
                    print("\nValor informado é maior que o valor total da compra:", round(valorCompra, 2), "-----(POR FAVOR INSIRA OUTRO VALOR)")
                else:
                    valorCompra -= 5
            elif dinheiro_inserido == 8:
                if valorCompra < 10:
                    print("\nValor informado é maior que o valor total da compra:", round(valorCompra, 2), "-----(POR FAVOR INSIRA OUTRO VALOR)")
                else:
                    valorCompra -= 10
            elif dinheiro_inserido == 9:
                if valorCompra < 20:
                    print("\nValor informado é maior que o valor total da compra:", round(valorCompra, 2), "-----(POR FAVOR INSIRA OUTRO VALOR)")
                else:
                    valorCompra -= 20
            elif dinheiro_inserido == 10:
                if valorCompra < 50:
                    print("\nValor informado é maior que o valor total da compra: ", round(valorCompra, 2), "-----(POR FAVOR INSIRA OUTRO VALOR)")
                else:
                    valorCompra -= 50
            else:
                print("Nota inválida")
            
            print("----------------------------------------------------------------")
            if valorCompra < 0.04:
                print("Produto(s) pago(s) com sucesso !!")
                continuar_loop = False
            else:
                print("----------------------------------------------------------------")
                print("Ainda falta R$", round(valorCompra, 2), " para pagar, insira mais dinheiro")
                print("----------------------------------------------------------------")

    # Mostra mensagem de agradecimento, finaliza a compra e pede se o consumidor quer realizar outra ou encerra o programa
    print("Obrigado por utilizar nossa máquina de refrigerantes, você irá retornar ao menu principal!")
    print("------------------------------------------------------------")