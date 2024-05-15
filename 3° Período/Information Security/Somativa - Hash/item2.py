import hashlib
import csv
import itertools
import time

def crack_hash(hash_value):
    """
    Função para realizar ataque de força bruta em um hash SHA-256.

    Argumentos:
        hash_value (str): Valor do hash SHA-256 a ser crackeado.

    Retorno:
        str: Senha original encontrada, se bem-sucedido.
        None: Se o ataque falhar.
    """
    start_time = time.time()
    attempts = 0  # contador de tentativas

    for senha_tentativa in itertools.product(range(33, 127), repeat=4):  # Gerando todas as combinações de caracteres ASCII imprimíveis de comprimento 4
        senha = ''.join(map(chr, senha_tentativa))
        senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        attempts += 1
        if senha_hash == hash_value:
            end_time = time.time()
            tempo_total = end_time - start_time
            print(f"Resumo da quebra de hash:")
            print(f"Hash quebrado: {hash_value}")
            print(f"Senha encontrada: {senha}")
            print(f"Número de tentativas: {attempts}")
            print(f"Tempo total: {tempo_total} segundos")
            return senha, tempo_total

    # Se nenhum hash correspondente for encontrado, imprime um resumo indicando que a senha não foi encontrada
    end_time = time.time()
    tempo_total = end_time - start_time
    print(f"Resumo da quebra de hash:")
    print(f"Hash quebrado: {hash_value}")
    print(f"Senha não encontrada")
    print(f"Número de tentativas: {attempts}")
    print(f"Tempo total: {tempo_total} segundos")
    return None, None

def main():
    """
    Função principal para executar o ataque de força bruta.
    """
    with open("usuarios.csv", newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        usuarios = list(leitor)

    total_tempo = 0

    for usuario in usuarios[:4]:  # Apenas os primeiros 4 usuários
        username, hash_value = usuario
        print(f"Quebrando hash para o usuário: {username}")
        senha_encontrada, tempo_para_quebrar = crack_hash(hash_value)
        if tempo_para_quebrar is not None:
            total_tempo += tempo_para_quebrar
        if senha_encontrada:
            print(f"Senha encontrada para o usuário {username}: {senha_encontrada}")
        else:
            print(f"Senha não encontrada para o usuário {username}")

    print(f"Tempo total para quebrar os hashes de 4 usuários: {total_tempo} segundos")
    print(f"Tempo médio por senha: {total_tempo / 4} segundos")

if __name__ == "__main__":
    main()
