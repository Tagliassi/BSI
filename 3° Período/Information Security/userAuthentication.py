tentativas_incorretas = 0
usuario_bloqueado = False

def ler_usuarios():
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    usuarios = []

    for linha in linhas:
        # Remover quebra de linha (\n)
        linha = linha.strip()

        # Separar em nome, senha
        campos = linha.split(",")
        nome = campos[0]
        senha = campos[1]
        usuarios.append((nome, senha))

    return usuarios

def adicionar_usuario(login, senha):
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{login},{senha}\n")

while True:
    print("=========================================================================")
    print("USER AUTHENTICATION")
    print("1) CADASTRAR\n2) lOGAR\n3) SAIR")
    print("=========================================================================")

    escolha = input("Digite um número para escolher uma opção (1, 2 OU 3): ")

    if escolha == "1":
        print("VAMOS FAZER O SEU CADASTRO!")

        login = input("Digite o seu login: ")
        senha = input("Digite a sua senha: ")

        adicionar_usuario(login, senha) 

    elif escolha == "2":
        print("VAMOS FAZER O SEU LOGIN!")
        if usuario_bloqueado:
            print("Usuário bloqueado devido a múltiplas tentativas incorretas.")
            continue

        login = input("Digite o seu login: ")
        senha = input("Digite a sua senha: ")

        usuarios = ler_usuarios() 

        if (login, senha) in usuarios:
            print(f"Seja bem vindo, {login}")
            tentativas_incorretas = 0 
        else:
            print("Login ou senha incorreto. Tente novamente mais tarde.")
            tentativas_incorretas += 1
            if tentativas_incorretas >= 5:
                print("Você excedeu o número máximo de tentativas incorretas. Seu acesso será bloqueado.")
                usuario_bloqueado = True

    elif escolha == "3":
        print("Obrigado!")
        break
    else:
        print("Escolha inválida, tente novamente.")