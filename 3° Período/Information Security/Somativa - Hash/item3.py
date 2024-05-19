# Rafael Galafassi & Marcos Vinicius

# Importa o módulo csv para lidar com arquivos CSV, os para gerar salt, a função getpass para ocultar a entrada de senha no terminal, e time para delays.
import csv
import os
from getpass import getpass
import hashlib
import time

# Função para gerar um salt aleatório
def gerar_salt():
    return os.urandom(16).hex()

# Função para ler os usuários do arquivo CSV e retorná-los como um dicionário.
def ler_usuarios():
    with open("usuarios.csv", newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        return {row[0]: (row[1], row[2]) for row in leitor}

# Função para ler as permissões dos arquivos do arquivo CSV e retorná-las como um dicionário de listas.
def ler_permissoes():
    with open("permissoes.csv", newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        permissoes = {}
        for row in leitor:
            if len(row) >= 2:
                permissoes[row[0]] = row[1:]
        return permissoes

# Função para adicionar um novo usuário ao arquivo CSV de usuários, armazenando o hash SHA-256 da senha.
def adicionar_usuario(login, senha, permissoes_padrao):
    salt = gerar_salt()
    senha_hash = hashlib.sha256((senha + salt).encode()).hexdigest()

    # Adiciona o usuário ao arquivo de usuários com o hash da senha e o salt
    with open("usuarios.csv", "a", newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([login, senha_hash, salt])

    # Adiciona as permissões padrão do novo usuário ao arquivo de permissões
    with open("permissoes.csv", "r+", newline='', encoding='utf-8') as arquivo_permissoes:
        leitor_permissoes = csv.reader(arquivo_permissoes)
        linhas_permissoes = list(leitor_permissoes)

        # Atualiza as permissões existentes com as permissões padrão do novo usuário
        for i, linha in enumerate(linhas_permissoes):
            arquivo, *permissoes = linha
            if arquivo != "":
                permissoes.extend([f"{login}:{permissao}" for permissao in permissoes_padrao])
                linhas_permissoes[i] = [arquivo] + permissoes

        # Retorna ao início do arquivo e reescreve todas as linhas com as atualizações
        arquivo_permissoes.seek(0)
        escritor_permissoes = csv.writer(arquivo_permissoes)
        escritor_permissoes.writerows(linhas_permissoes)

# Função para verificar a autenticação do usuário, comparando o hash da senha fornecida com o hash armazenado.
def verificar_autenticacao():
    tentativas_incorretas = 0
    tempo_bloqueio = 30  # Tempo inicial de espera em segundos
    while True:
        usuarios = ler_usuarios()

        print("\nDigite uma opção para começar:")
        print("1. Cadastrar")
        print("2. Autenticar")
        print("3. Sair")
        opcao = input(">>> ")

        if opcao == "1":
            novo_login = input("Digite o novo nome de usuário com até 4 caracteres: ")
            nova_senha = getpass("Digite a senha para o novo usuário com até 4 caracteres: ")
            # Define suas permissões padrão aqui
            permissoes_padrao = ["ler", "escrever"]
            if len(novo_login) >= 4 and len(nova_senha) >= 4:
                adicionar_usuario(novo_login, nova_senha, permissoes_padrao)
                print(f"\nUsuário {novo_login} cadastrado com sucesso!\n")
            else:
                print("Cadastro de usuário ou senha com menos de 4 caracteres.")
        elif opcao == "2":
            login = input("Digite seu nome de usuário: ")
            senha = getpass("Digite sua senha: ")

            if login in usuarios:
                senha_hash_armazenada, salt = usuarios[login]
                senha_hash = hashlib.sha256((senha + salt).encode()).hexdigest()

                if senha_hash == senha_hash_armazenada:
                    print(f"\nUsuário {login} autenticado!\n")
                    return login
                else:
                    print("Login ou senha incorreto. Tente novamente.")
            else:
                print("Login ou senha incorreto. Tente novamente.")
            
            print(f"Tentativa {tentativas_incorretas + 1}")
            tentativas_incorretas += 1
            if tentativas_incorretas >= 3:
                print(f"Você excedeu o número máximo de tentativas incorretas. Aguardando {tempo_bloqueio} segundos.")
                for i in range(tempo_bloqueio, 0, -1):
                    print(f"Esperando {i} segundos...")
                    time.sleep(1)
                tentativas_incorretas = 0  # Resetar após o tempo de espera
                tempo_bloqueio *= 2  # Dobra o tempo de espera a cada falha
        elif opcao == "3":
            print("\nSaindo...")
            return None
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Função para verificar o acesso do usuário aos arquivos com base em suas permissões.
def verificar_acesso(permissoes, usuario):
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
                        print("Acesso negado. Você não tem permissão para esta operação no arquivo.")
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

# Função principal que controla o fluxo do programa.
def main():
    permissoes = ler_permissoes()

    login = verificar_autenticacao()
    if login:
        verificar_acesso(permissoes, login)

main()
