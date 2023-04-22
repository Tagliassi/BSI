# Programa: Vending Machine
# Autor: Rafael Galafassi, Vinicius Costa, Marcos Vincius e Vinicius Viana
# Data de criação: 07/04/2023
# Versão: 1.0
# Descrição: Programa que simula uma máquina de vendas.
# Observação: Números, pontos e ENTER serão as únicas formas de entrada pelos usuários.

qtd_produto_agua = 0
qtd_produto_agua_vendido = 0
qtd_produto_cha = 0
qtd_produto_cha_vendido = 0
qtd_produto_guarana = 0
qtd_produto_guarana_vendido = 0
qtd_produto_coca = 0
qtd_produto_coca_vendido = 0

troco = 0
valor_compra = 0
total_cedulas = 0
total_moedas = 0
novo_total_cedulas = 0
senha = ""

while True:
    print("------------------------------------------------------------")
    print("Bem-vindo(a) à máquina de Refrigerantes!")
    print("------------------------------------------------------------")
    print("Digite o tipo de usuário que você é:")

    usuario = input("\n1) ADMINISTRADOR\n2) CONSUMIDOR\n")

    print("------------------------------------------------------------")
    if usuario == "1" or usuario == "2":
        print("Ok, você entrou como usuário", usuario)
    else:
        print("Usuário inválido, tente novamente")
        continue
    print("------------------------------------------------------------")
    if usuario == "1":
        senha = input("Digite a senha para habilitar o sistema: ")
        while senha != "1234":
            print("Senha inválida, tente novamente")
            senha = input("Digite a senha para habilitar o sistema: ")
        print("------------------------------------------------------------")
        opcao_adm = input(
            "Selecione a opção:\n(1) para atualizar o troco na máquina\n(2) para atualizar o estoque de produtos\n(3) para ver a quantidade de dinheiro das vendas\n")
        if opcao_adm == "1":
            print("------------------------------------------------------------")
            print("Digite a quantidade de cédulas")
            qtd_cedulas_2 = int(
                input("Digite a quantidade de notas de 2: "))
            qtd_cedulas_5 = int(
                input("Digite a quantidade de notas de 5: "))
            qtdeCedulas10 = int(
                input("Digite a quantidade de notas de 10: "))
            qtd_cedulas_20 = int(
                input("Digite a quantidade de notas de 20: "))
            novo_total_cedulas = (qtd_cedulas_2*2) + (qtd_cedulas_5*5) + \
                (qtdeCedulas10*10) + (qtd_cedulas_20*20)
            total_cedulas = novo_total_cedulas
            print(
                "A quantidade de cédulas de 2 reais é de: ", qtd_cedulas_2)
            print(
                "A quantidade de cédulas de 5 reais é de: ", qtd_cedulas_5)
            print(
                "A quantidade de cédulas de 10 reais é de: ", qtdeCedulas10)
            print(
                "A quantidade de cédulas de 20 reais é de: ", qtd_cedulas_20)
            print(
                "O total de dinheiro em cedulas na máquina é de R$", total_cedulas)
            print("------------------------------------------------------------")
            print("Digite a quantidade de moedas")
            qtd_moedas_5 = int(
                input("Digite a quantidade de moedas de 5 centavos: "))
            qtd_moedas_10 = int(
                input("Digite a quantidade de moedas de 10 centavos: "))
            qtd_moedas_25 = int(
                input("Digite a quantidade de moedas de 25 centavos: "))
            qtd_moedas_50 = int(
                input("Digite a quantidade de moedas de 50 centavos: "))
            qtd_moedas_1 = int(
                input("Digite a quantidade de moedas de 1 real: "))
            novo_total_moedas = ((qtd_moedas_5*5)/100) + ((qtd_moedas_10*10)/100) + \
                ((qtd_moedas_25*25)/100) + \
                ((qtd_moedas_50*50)/100) + (qtd_moedas_1*1)
            total_moedas = novo_total_moedas
            print(
                "A quantidade de moedas de 5 centavos é de: ", qtd_moedas_5)
            print(
                "A quantidade de moedas de 10 centavos é de: ", qtd_moedas_10)
            print(
                "A quantidade de moedas de 25 centavos é de: ", qtd_moedas_25)
            print(
                "A quantidade de moedas de 50 centavos é de: ", qtd_moedas_50)
            print("A quantidade de moedas de 1 real é de: ", qtd_moedas_1)
            print(
                "O total de dinheiro em moedas na máquina é de R$", total_moedas)

            print("------------------------------------------------------------")
            novo_troco = (total_cedulas + total_moedas)
            print("O total de troco na máquina é de R$", novo_troco)
            troco = novo_troco
            print("Troco atualizado com sucesso!")
            print("------------------------------------------------------------")
        elif opcao_adm == "2":
            print("------------------------------------------------------------")
            nova_qtd_produto_coca = int(
                input("Adicione mais unidade(s) de Coca-Cola ao estoque: "))
            qtd_produto_coca += nova_qtd_produto_coca
            print(
                "A quantidade de unidade(s) de Coca-Cola atual em estoque é igual a: ", qtd_produto_coca)
            print("------------------------------------------------------------")

            nova_qtd_produto_guarana = int(
                input("Adicione mais unidade(s) de Guaraná ao estoque: "))
            qtd_produto_guarana += nova_qtd_produto_guarana
            print("A quantidade de unidade(s) de Guaraná atual em estoque é igual a: ",
                  qtd_produto_guarana)
            print("------------------------------------------------------------")

            nova_qtd_produto_cha = int(
                input("Adicione mais unidade(s) de Chá ao estoque: "))
            qtd_produto_cha += nova_qtd_produto_cha
            print(
                "A quantidade de unidade(s) de Chá atual em estoque é igual a: ", qtd_produto_cha)
            print("------------------------------------------------------------")

            nova_qtd_produto_agua = int(
                input("Adicione mais unidade(s) de Água ao estoque: "))
            qtd_produto_agua += nova_qtd_produto_agua
            print(
                "A quantidade de unidade(s) de Água atual em estoque é igual a: ", qtd_produto_agua)
            print("------------------------------------------------------------")

            print("Estoque atualizado com sucesso!")
            print("------------------------------------------------------------")
        elif opcao_adm == "3":
            print("O valor recebido das vendas de Coca-Cola é igual a: R$",
                  (qtd_produto_coca_vendido*4))
            print("O valor recebido das vendas de Guaraná é igual a: R$",
                  (qtd_produto_guarana_vendido*4))
            print("O valor recebido das vendas de Chá é igual a: R$",
                  (qtd_produto_cha_vendido*3))
            print("O valor recebido das vendas de Água é igual a: R$",
                  (qtd_produto_agua_vendido*2))
            print("O valor total das vendas é igual a: R$", ((qtd_produto_coca_vendido*4) +
                  (qtd_produto_guarana_vendido*4) + (qtd_produto_cha_vendido*3) + (qtd_produto_agua_vendido*2)))
        else:
            print("Opção inválida, tente novamente")
            continue
    elif usuario == "2":
        print("Selecione o produto que deseja comprar, somente cédulas até R$20 e/ou moedas são aceitas para efetuar o pagamento.")
        produto = input(
            "1) Coca-Cola R$ 4.00\n2) Guaraná R$ 4.00\n3) Chá R$ 3.00\n4) Água R$ 2.00\n")
        if produto == "1":
            qtd_compra_coca = int(
                input("Quantas unidades de Coca gostaria de comprar: "))
            if int(qtd_compra_coca) > int(qtd_produto_coca):
                print(
                    "Infelizmente só temos ", qtd_produto_coca, " unidades desse produto, tente novamente.")
                continue
            else:
                qtd_produto_coca_vendido = (
                    int(qtd_produto_coca) - int(qtd_compra_coca))
                valor_compra = (4 * qtd_compra_coca)
                print(
                    "\n--------------------------------------------------------------------")
                print(
                    "O valor total da compra ficou igual a: R$", valor_compra)
                print(
                    "\n--------------------------------------------------------------------")

        elif produto == "2":
            qtdeCompraGuarana = int(
                input("Quantas unidades de Guaraná gostaria de comprar: "))
            if int(qtdeCompraGuarana) > int(qtd_produto_guarana):
                print(
                    "Infelizmente só temos ", qtd_produto_guarana, " unidades desse produto, tente novamente.")
                continue
            else:
                qtd_produto_guarana_vendido = (
                    int(qtd_produto_guarana) - int(qtdeCompraGuarana))
                valor_compra = (4 * qtdeCompraGuarana)
                print(
                    "O valor total da compra ficou igual a: R$", valor_compra)
        elif produto == "3":
            qtdeCompraCha = int(
                input("Quantas unidades de Chá gostaria de comprar: "))
            if int(qtdeCompraCha) > int(qtd_produto_cha):
                print(
                    "Infelizmente só temos ", qtd_produto_cha, "unidades desse produto, tente novamente.")
                continue
            else:
                qtd_produto_cha_vendido = (
                    int(qtd_produto_cha) - int(qtdeCompraCha))
                valor_compra = (3 * qtdeCompraCha)
                print(
                    "O valor total da compra ficou igual a: R$", valor_compra)
        elif produto == "4":
            qtdeCompraAgua = int(
                input("Quantas unidades de Água gostaria de comprar: "))
            if int(qtdeCompraAgua) > int(qtd_produto_agua):
                print(
                    "Infelizmente só temos ", qtd_produto_agua, " unidades desse produto, tente novamente.")
                continue
            else:
                qtd_produto_agua_vendido = (
                    int(qtd_produto_agua) - int(qtdeCompraAgua))
                valor_compra = (2 * qtdeCompraAgua)
                print(
                    "O valor total da compra ficou igual a: R$", valor_compra)
        else:
            print("Opção inválida, tente novamente")
            continue

        print("Digite o numero correspondente ao dinheiro para pagar:")

        continuar_loop = True

        while continuar_loop:
            print("----------------------------------------------------------------")
            dinheiro_inserido = int(input(
                "1 - Moeda R$0,05\n2 - Moeda R$0,10\n3 - Moeda R$0,25\n4 - Moeda R$0,50\n5 - Moeda R$1,00\n6 - Nota R$2,00\n7 - Nota R$5,00\n8 - Nota R$10,00\n9 - Nota R$20,00\n10 - Nota R$50,00\n===================================================\nValor: "))
            print("----------------------------------------------------------------")

            if dinheiro_inserido == 1:
                if valor_compra < 0.05:
                    print("\n------------\nVocê inseriu R$",
                          round(0.05, 2), " reais\n")

                    valor_compra -= 0.05
                    if valor_compra <= 0:
                        troco += valor_compra
                        print(
                            "----------------------------------------------------------------")
                        print("Foi dado R$", abs(valor_compra),
                              "de troco para você")
                        print(
                            "----------------------------------------------------------------")
                        print("Novo saldo de troco da máquina: ", troco)
                    else:
                        print(
                            "A máquina não possui troco suficiente para essa quantidade de dinheiro, por favor insira outra quantidade...")
                else:
                    valor_compra -= 0.05
            elif dinheiro_inserido == 2:
                if valor_compra < 0.10:
                    print("\n------------\nVocê inseriu R$",
                          round(0.10, 2), " reais\n")

                    valor_compra -= 0.10
                    if valor_compra <= 0:
                        troco += valor_compra
                        print(
                            "----------------------------------------------------------------")
                        print("Foi dado R$", abs(valor_compra),
                              "de troco para você")
                        print(
                            "----------------------------------------------------------------")
                        print("Novo saldo de troco da máquina: ", troco)
                    else:
                        print(
                            "A máquina não possui troco suficiente para essa quantidade de dinheiro, por favor insira outra quantidade...")
                else:
                    valor_compra -= 0.10
            elif dinheiro_inserido == 3:
                if valor_compra < 0.25:
                    print("\n------------\nVocê inseriu R$",
                          round(0.25, 2), " reais\n")

                    valor_compra -= 0.25
                    if valor_compra <= 0:
                        troco += valor_compra
                        print(
                            "----------------------------------------------------------------")
                        print("Foi dado R$", abs(valor_compra),
                              "de troco para você")
                        print(
                            "----------------------------------------------------------------")
                        print("Novo saldo de troco da máquina: ", troco)
                    else:
                        print(
                            "A máquina não possui troco suficiente para essa quantidade de dinheiro, por favor insira outra quantidade...")
                else:
                    valor_compra -= 0.25
            elif dinheiro_inserido == 4:
                if valor_compra < 0.50:
                    print("\n------------\nVocê inseriu R$",
                          round(0.50, 2), " reais\n")

                    valor_compra -= 0.50
                    if valor_compra <= 0:
                        troco += valor_compra
                        print(
                            "----------------------------------------------------------------")
                        print("Foi dado R$", abs(valor_compra),
                              "de troco para você")
                        print(
                            "----------------------------------------------------------------")
                        print("Novo saldo de troco da máquina: ", troco)
                    else:
                        print(
                            "A máquina não possui troco suficiente para essa quantidade de dinheiro, por favor insira outra quantidade...")
                else:
                    valor_compra -= 0.50
            elif dinheiro_inserido == 5:
                if valor_compra < 1.00:
                    print("\n------------\nVocê inseriu R$",
                          round(1, 2), " reais\n")

                    valor_compra -= 1
                    if valor_compra <= 0:
                        troco += valor_compra
                        print(
                            "----------------------------------------------------------------")
                        print("Foi dado R$", abs(valor_compra),
                              "de troco para você")
                        print(
                            "----------------------------------------------------------------")
                        print("Novo saldo de troco da máquina: ", troco)
                    else:
                        print(
                            "A máquina não possui troco suficiente para essa quantidade de dinheiro, por favor insira outra quantidade...")
                else:
                    valor_compra -= 1.00
            elif dinheiro_inserido == 6:
                if valor_compra < 2:
                    print("\n------------\nVocê inseriu R$",
                          round(2, 2), " reais\n")

                    valor_compra -= 2
                    if valor_compra <= 0:
                        troco += valor_compra
                        print(
                            "----------------------------------------------------------------")
                        print("Foi dado R$", abs(valor_compra),
                              "de troco para você")
                        print(
                            "----------------------------------------------------------------")
                        print("Novo saldo de troco da máquina: ", troco)
                    else:
                        print(
                            "A máquina não possui troco suficiente para essa quantidade de dinheiro, por favor insira outra quantidade...")
                else:
                    valor_compra -= 2
            elif dinheiro_inserido == 7:
                if valor_compra < 5:
                    print("\n------------\nVocê inseriu R$",
                          round(5, 2), " reais\n")

                    valor_compra -= 5
                    if valor_compra <= 0:
                        troco += valor_compra
                        print(
                            "----------------------------------------------------------------")
                        print("Foi dado R$", abs(valor_compra),
                              "de troco para você")
                        print(
                            "----------------------------------------------------------------")
                        print("Novo saldo de troco da máquina: ", troco)
                    else:
                        print(
                            "A máquina não possui troco suficiente para essa quantidade de dinheiro, por favor insira outra quantidade...")
                else:
                    valor_compra -= 5
            elif dinheiro_inserido == 8:
                if valor_compra < 10:
                    print("\n------------\nVocê inseriu R$",
                          round(10, 2), " reais\n")

                    valor_compra -= 10
                    if valor_compra <= 0:
                        troco += valor_compra
                        print(
                            "----------------------------------------------------------------")
                        print("Foi dado R$", abs(valor_compra),
                              "de troco para você")
                        print(
                            "----------------------------------------------------------------")
                        print("Novo saldo de troco da máquina: ", troco)
                    else:
                        print(
                            "A máquina não possui troco suficiente para essa quantidade de dinheiro, por favor insira outra quantidade...")
                else:
                    valor_compra -= 10
            elif dinheiro_inserido == 9:
                if valor_compra < 20:
                    print("\n------------\nVocê inseriu R$",
                          round(20, 2), " reais\n")

                    valor_compra -= 20
                    sobra = valor_compra - 20
                    if valor_compra <= 0:
                        troco += valor_compra
                        print(
                            "----------------------------------------------------------------")
                        print("Foi dado R$", abs(valor_compra),
                              "de troco para você")
                        print(
                            "----------------------------------------------------------------")
                        print("Novo saldo de troco da máquina: ", troco)
                    else:
                        print(
                            "A máquina não possui troco suficiente para essa quantidade de dinheiro, por favor insira outra quantidade...")
                else:
                    valor_compra -= 20
            elif dinheiro_inserido == 10:
                if valor_compra < 50:
                    print("\n------------\nVocê inseriu R$",
                          round(50, 2), " reais\n")

                    valor_compra -= 50
                    if valor_compra <= 0:
                        troco += valor_compra
                        print(
                            "----------------------------------------------------------------")
                        print("Foi dado R$", abs(valor_compra),
                              "de troco para você")
                        print(
                            "----------------------------------------------------------------")
                        print("Novo saldo de troco da máquina: ", troco)
                    else:
                        print(
                            "A máquina não possui troco suficiente para essa quantidade de dinheiro, por favor insira outra quantidade...")
                else:
                    valor_compra -= 50
            else:
                print("Nota inválida")

            print("----------------------------------------------------------------")
            if valor_compra <= 0:
                print("Produto(s) pago(s) com sucesso !!")
                continuar_loop = False
            else:
                print("----------------------------------------------------------------")
                print("Ainda falta R$", round(valor_compra, 2),
                      " para pagar, insira mais dinheiro")
                print("----------------------------------------------------------------")

    print("------------------------------------------------------------")
    print("Obrigado por utilizar nossa máquina de refrigerantes, você irá retornar ao menu principal!")
