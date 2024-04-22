# Rafael Galafassi & Marcos Vinicius

import csv
from getpass import getpass

def ler_usuarios():
    with open("usuarios.csv", newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        return {row[0]: row[1] for row in leitor}

def ler_permissoes():
    with open("permissoes.csv", newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        permissoes = {}
        for row in leitor:
            if len(row) >= 2:
                permissoes[row[0]] = row[1:]
        return permissoes

def adicionar_usuario(login, senha):
    with open("usuarios.csv", "a", newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([login, senha])

def verificar_autenticacao():
    tentativas_incorretas = 0
    usuario_bloqueado = False
    while True:
        usuarios = ler_usuarios()

        if usuario_bloqueado:
            print("Usuário bloqueado devido a múltiplas tentativas incorretas.")
            return None

        print("\nDigite uma opção para começar:")
        print("1. Cadastrar")
        print("2. Autenticar")
        print("3. Sair")
        opcao = input(">>> ")

        if opcao == "1":
            novo_login = input("Digite o novo nome de usuário: ")
            nova_senha = getpass("Digite a senha para o novo usuário: ")
            adicionar_usuario(novo_login, nova_senha)
            print(f"\nUsuário {novo_login} cadastrado com sucesso!\n")
        elif opcao == "2":
            login = input("Digite seu nome de usuário: ")
            senha = getpass("Digite sua senha: ")

            if login in usuarios and usuarios[login] == senha:
                print(f"\nUsuário {login} autenticado!\n")
                return login
            else:
                print("Login ou senha incorreto. Tente novamente.")
                tentativas_incorretas += 1
                if tentativas_incorretas >= 3:
                    print("Você excedeu o número máximo de tentativas incorretas. Seu acesso será bloqueado.")
                    usuario_bloqueado = True
        elif opcao == "3":
            print("\nSaindo...")
            return None
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def verificar_acesso(permissoes, usuario):
    # Problema ao ler as permissões do user
    while True:
        print("\nComandos disponíveis:")
        print("1. Ler arquivo")
        print("2. Criar arquivo")
        print("3. Excluir arquivo")
        print("4. Sair")

        opcao = input("\nDigite uma opção: ")

        if opcao == "4":
            print("\nSaindo...")
            break
        elif opcao in ["1", "2", "3"]:
            if opcao == "1":
                opcao = "ler"
            elif opcao == "2":
                opcao = "escrever"
            elif opcao == "3":
                opcao = "apagar"

            nome_arquivo = input("Digite o nome do arquivo: ")

            if nome_arquivo in permissoes:
                permissoes_arquivo = permissoes[nome_arquivo]

                permissoes_chave_valor = []
                for item in permissoes_arquivo:
                    chave, valor = item.split(':')
                    v = valor.split(";")
                    permissoes_chave_valor.append([chave, v])

                for chave, valor in permissoes_chave_valor:
                    if opcao in valor:
                        print("-------------------------------")
                        print("Acesso permitido.")
                        print("-------------------------------")
                    else:
                        print("-------------------------------")
                        print("Acesso negado. Você não tem permissão para excluir este arquivo.")
                        print("-------------------------------")
                    break
                else:
                    print("-------------------------------")
                    print("Acesso negado. Você não tem permissão para esta operação no arquivo.")
                    print("-------------------------------")
            else:
                print("-------------------------------")
                print("Arquivo não encontrado.")
                print("-------------------------------")
        else:
            print("-------------------------------")
            print("Opção inválida. Por favor, escolha uma opção válida.")
            print("-------------------------------")

def main():
    permissoes = ler_permissoes()

    login = verificar_autenticacao()
    if login:
        verificar_acesso(permissoes, login)

main()