import csv
from getpass import getpass

# Rafael Galafassi & Marcos Vinicius

def ler_usuarios():
    with open("usuarios.csv", newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        return {row[0]: row[1] for row in leitor}

def ler_permissoes():
    with open("permissoes.csv", newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        return {row[0]: row[1:] for row in leitor}

def adicionar_usuario(login, senha):
    with open("usuarios.csv", "a", newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([login, senha])

def verificar_autenticacao(usuarios):
    tentativas_incorretas = 0
    usuario_bloqueado = False
    while True:
        if usuario_bloqueado:
            print("Usuário bloqueado devido a múltiplas tentativas incorretas.")
            return None

        login = input("Digite o seu login: ")
        senha = getpass("Digite a sua senha: ")

        if login in usuarios and usuarios[login] == senha:
            print(f"Seja bem vindo, {login}")
            return login
        else:
            print("Login ou senha incorreto. Tente novamente.")
            tentativas_incorretas += 1
            if tentativas_incorretas >= 3:
                print("Você excedeu o número máximo de tentativas incorretas. Seu acesso será bloqueado.")
                usuario_bloqueado = True

def verificar_acesso(permissoes, usuario):
    acao = input("Digite a ação que deseja realizar (ler, escrever, apagar): ")
    recurso = input("Digite o nome do recurso: ")
    arquivo = input("Digite o nome do arquivo: ")

    if (usuario, acao) in permissoes[arquivo] or (usuario, "admin") in permissoes[arquivo]:
        print("Acesso permitido")
    else:
        print("Acesso negado")

def main():
    usuarios = ler_usuarios()
    permissoes = ler_permissoes()

    login = verificar_autenticacao(usuarios)
    if login:
        verificar_acesso(permissoes, login)

if __name__ == "__main__":
    main()
