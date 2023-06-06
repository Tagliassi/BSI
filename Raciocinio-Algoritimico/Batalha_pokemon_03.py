import random

# Definir Pokédex
pokedex = {}

# Definir Bag
bag = {
    "Poção": 3,
    "Super Poção": 5,
}

# Função para adicionar Pokémon à Pokédex
def adicionar_pokemon_pokedex(pokemon, tipo, ataques):
    pokedex[pokemon] = {
        "TIPO": tipo,
        "ATAQUES": ataques
    }

# Função para escolher o Pokémon inicial
def escolher_pokemon_inicial(pokemon_inicial):
    pokemons_validos = {
        "Pikachu": ("Elétrico", ["Choque do Trovão", "Onda de Choque"]),
        "Squirtle": ("Água", ["Jato de Água", "Bolhas"]),
        "Charmander": ("Fogo", ["Lança-Chamas", "Brasa"])
    }

    if pokemon_inicial in pokemons_validos:
        print(f"Parabéns, seu pokémon inicial é {pokemon_inicial}")
        tipo, ataques = pokemons_validos[pokemon_inicial]
        adicionar_pokemon_pokedex(pokemon_inicial, tipo, ataques)
    else:
        print("Não reconheci esse pokémon, nenhum pokémon foi selecionado")

# Iniciar aventura e capturar Pokémon inicial
print("Welcome to the Pokemon world")

nome_jogador = input("Digite seu nome jogador: ")
nome_rival = input("Digite o nome do rival: ")

print(f"Olá {nome_jogador}, então o nome do seu rival é {nome_rival}, boa sorte em sua jornada!")

pokemon_inicial = input("Escolha seu pokémon inicial, Pikachu, Charmander ou Squirtle: ")
escolher_pokemon_inicial(pokemon_inicial)

# Capturar novos Pokémon
def pokemon_adventure():
    captured_pokemons = set()
    
    while True:
        print("=========================================================================")
        print("Pokemon Adventure")
        print("Vamos iniciar nossa aventura e explorar o mundo para capturar Pokémon")
        print("1) MATOS ALTOS\n2) CAVERNAS\n3) CACHOEIRA\n4) FLORESTA\n5) FINALIZAR AVENTURA")
        print("=========================================================================")

        lugar = input("Digite um número para escolher um lugar para explorar ou para finalizar a aventura (1, 2, 3, 4 ou 5): ")

        if lugar == "5":
            if len(captured_pokemons) >= 5:
                print("Você capturou os seguintes Pokémon:")
                for pokemon in captured_pokemons:
                    pokemon_count = list(captured_pokemons).count(pokemon)
                    print(f"{pokemon_count}x {pokemon}")
                print("Obrigado por jogar!")
                break
            else:
                print("Você precisa capturar pelo menos 5 Pokémon diferentes para finalizar a aventura.")
        elif lugar in ["1", "2", "3", "4"]:
            grass_land_pokemons = ["Rattata", "Pidgey", "Gloom"]
            cave_pokemons = ["Gengar", "Geodude", "Onix"]
            waterfall_pokemons = ["Squirtle", "Magikarp", "Lapras"]
            forest_pokemons = ["Bulbasaur", "Caterpie", "Chikorita"]

            if lugar == "1":
                caught_pokemon = random.choice(grass_land_pokemons)
            elif lugar == "2":
                caught_pokemon = random.choice(cave_pokemons)
            elif lugar == "3":
                caught_pokemon = random.choice(waterfall_pokemons)
            elif lugar == "4":
                caught_pokemon = random.choice(forest_pokemons)

            captured_pokemons.add(caught_pokemon)
            print("Eba você capturou um", caught_pokemon, "!")
        else:
            print("Lugar inválido, tente novamente")

def get_pokemon_info(pokemon):
    pokemons_info = {
        "Pikachu": {
            "TIPO": "Elétrico",
            "ATAQUES": ["Choque do Trovão", "Onda de Choque"],
            "VIDA": 100,
            "RESISTENCIAS": ["Elétrico"],
            "FRAGILIDADES": ["Terra"],
        },
        "Squirtle": {
            "TIPO": "Água",
            "ATAQUES": ["Jato de Água", "Bolhas"],
            "VIDA": 120,
            "RESISTENCIAS": ["Água", "Fogo", "Gelo"],
            "FRAGILIDADES": ["Elétrico", "Planta"],
        },
        "Charmander": {
            "TIPO": "Fogo",
            "ATAQUES": ["Lança-Chamas", "Brasa"],
            "VIDA": 110,
            "RESISTENCIAS": ["Fogo", "Grama", "Gelo", "Inseto", "Aço", "Fada"],
            "FRAGILIDADES": ["Água", "Terra", "Rocha"],
        },
        "Rattata": {
            "TIPO": "Normal",
            "ATAQUES": ["Investida", "Dente de Sabre"],
            "VIDA": 80,
            "RESISTENCIAS": [],
            "FRAGILIDADES": ["Lutador"],
        },
        "Pidgey": {
            "TIPO": "Normal, Voador",
            "ATAQUES": ["Ataque de Asas", "Tornado"],
            "VIDA": 90,
            "RESISTENCIAS": ["Grama", "Lutador", "Inseto"],
            "FRAGILIDADES": ["Elétrico", "Gelo", "Pedra", "Rocha"],
        },
        "Gloom": {
            "TIPO": "Grama, Venenoso",
            "ATAQUES": ["Ácido", "Pó Venenoso"],
            "VIDA": 100,
            "RESISTENCIAS": ["Água", "Elétrico", "Planta", "Lutador", "Inseto", "Fada"],
            "FRAGILIDADES": ["Fogo", "Gelo", "Voador", "Psíquico"],
        },
        "Gengar": {
            "TIPO": "Fantasma, Venenoso",
            "ATAQUES": ["Bola Sombria", "Soco Sombrio"],
            "VIDA": 130,
            "RESISTENCIAS": ["Venenoso", "Inseto", "Pedra", "Fantasma", "Psíquico", "Fada"],
            "FRAGILIDADES": ["Psíquico", "Fantasma"],
        },
        "Geodude": {
            "TIPO": "Pedra, Terra",
            "ATAQUES": ["Arremesso de Rocha", "Lançamento de Lodo"],
            "VIDA": 120,
            "RESISTENCIAS": ["Normal", "Fogo", "Venenoso", "Voador", "Inseto", "Pedra", "Aço"],
            "FRAGILIDADES": ["Água", "Grama, Lutador", "Terra", "Aço"],
        },
        "Onix": {
            "TIPO": "Pedra, Terra",
            "ATAQUES": ["Terratemor", "Investida de Cabeça"],
            "VIDA": 150,
            "RESISTENCIAS": ["Normal", "Fogo", "Venenoso", "Elétrico", "Voador", "Inseto", "Pedra", "Aço"],
            "FRAGILIDADES": ["Água", "Grama", "Gelo", "Lutador", "Terra, Aço"],
        },
        "Magikarp": {
            "TIPO": "Água",
            "ATAQUES": ["Splash"],
            "VIDA": 80,
            "RESISTENCIAS": ["Fogo", "Água", "Gelo"],
            "FRAGILIDADES": ["Elétrico", "Grama"],
        },
        "Lapras": {
            "TIPO": "Água, Gelo",
            "ATAQUES": ["Pulso do Dragão", "Hidro Bomba", "Raio de Gelo"],
            "VIDA": 160,
            "RESISTENCIAS": ["Água", "Elétrico", "Gelo", "Fogo", "Grama"],
            "FRAGILIDADES": ["Lutador", "Pedra", "Planta", "Elétrico", "Grau, Voador"],
        },
        "Bulbasaur": {
            "TIPO": "Grama, Venenoso",
            "ATAQUES": ["Folha Navalha", "Semente Sanguessuga"],
            "VIDA": 110,
            "RESISTENCIAS": ["Água", "Elétrico", "Planta", "Lutador", "Inseto", "Fada"],
            "FRAGILIDADES": ["Fogo", "Gelo", "Voador", "Psíquico"],
        },
        "Caterpie": {
            "TIPO": "Inseto",
            "ATAQUES": ["Seda", "Ventania"],
            "VIDA": 70,
            "RESISTENCIAS": ["Grama", "Lutador", "Inseto"],
            "FRAGILIDADES": ["Fogo", "Voador", "Pedra"],
        },
        "Chikorita": {
            "TIPO": "Grama",
            "ATAQUES": ["Chicote de Vinha", "Ataque Rápido"],
            "VIDA": 100,
            "RESISTENCIAS": ["Água", "Elétrico", "Grama", "Terra", "Lutador", "Inseto"],
            "FRAGILIDADES": ["Fogo", "Gelo", "Voador", "Inseto", "Venenoso"],
        }
    }

    return pokemons_info[pokemon]

pokemon_adventure()

# Função para consultar informações de um Pokémon na Pokédex
def consultar_pokemon(pokemon):
    pokemon_info = pokedex.get(pokemon)
    if pokemon_info:
        tipo = pokemon_info["TIPO"]
        ataques = ", ".join(pokemon_info["ATAQUES"])
        print(f"Informações de {pokemon}:")
        print(f"Tipo: {tipo}")
        print(f"Ataques: {ataques}")
    else:
        print("Pokémon não encontrado na Pokédex.")

# Consultar informações de Pokémon na Pokédex
while True:
    comando = input("Insira o nome de um Pokémon para consultar suas informações na pokedex ou insira 9 para encerrar: ")

    if comando == "9":
        print("Volte sempre!")
        break

    consultar_pokemon(comando)

# Pokemon Battle

continuar_jogo = True

while continuar_jogo:
    print("=========================================================================")
    print("Pokemon Battle")
    print(f"Vamos iniciar nossa batalha contra o nosso rival {nome_rival} e tentaremos ganhar a todo custo")
    print("1) ESCOLHER POKEMONS PARA A BATALHA\n2) CONSULTAR A BAG\n3) BATALHAR\n4) ENCERRAR POKEMON BATTLE")
    print("=========================================================================")

    opcao = input("Digite sua opção: ")

    # Função para escolher os Pokémon para a batalha
    def escolher_pokemon_batalha():
        pokemons_disponiveis = list(pokedex.keys())
        pokemons_batalha = []

        print("Escolha 6 Pokémons para a batalha:")
        for cont in range(6):
            print(f"Escolha o Pokémon {cont+1}:")
            exibir_pokemons_disponiveis(pokemons_disponiveis)

            escolha = int(input("Digite o número correspondente: ")) - 1

            if escolha >= 0 and escolha < len(pokemons_disponiveis):
                pokemon_escolhido = pokemons_disponiveis.pop(escolha)
                pokemons_batalha.append(pokemon_escolhido)
            else:
                print("Escolha inválida. Tente novamente.")

        return pokemons_batalha

    # Função para exibir os Pokémons disponíveis para escolha
    def exibir_pokemons_disponiveis(pokemons_disponiveis):
        for j, pokemon in enumerate(pokemons_disponiveis):
            print(f"{j+1}) {pokemon}")

    # Função para exibir e atualizar a mochila
    def consultar_bag():
        while True:
            print("================================")
            print("BAG - MOCHILA")
            print("1) Ver itens na mochila")
            print("2) Atualizar quantidade de itens")
            print("3) Fechar a mochila e salvar alterações")
            print("================================")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                exibir_itens()
            elif opcao == "2":
                atualizar_quantidade_itens()
            elif opcao == "3":
                print("Alterações na mochila salvas.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    # Função para exibir os itens na mochila
    def exibir_itens():
        print("Itens disponíveis na mochila:")
        for item, quantidade in bag.items():
            print(f"{item}: {quantidade}")

    # Função para atualizar a quantidade de itens na mochila
    def atualizar_quantidade_itens():
        print("Itens disponíveis na mochila:")
        for item, quantidade in bag.items():
            print(f"{item}: {quantidade}")

        item = input("Digite o nome do item para atualizar a quantidade: ")
        quantidade = int(input("Digite a nova quantidade: "))

        bag[item] = quantidade
        print("Quantidade atualizada com sucesso.")



# Função para realizar a batalha
def batalhar():
    pokemons_jogador = escolher_pokemon_batalha()
    pokemons_inimigo = random.sample(list(pokedex.keys()), 6)
    jogador_atual = 0
    inimigo_atual = 0

    print("Início da batalha!")
    while jogador_atual < 6 and inimigo_atual < 6:
        print(f"Batalha {jogador_atual + inimigo_atual + 1}")
        pokemon_jogador = pokemons_jogador[jogador_atual]
        pokemon_inimigo = pokemons_inimigo[inimigo_atual]
        print(f"Seu Pokémon: {pokemon_jogador}")
        print(f"Inimigo: {pokemon_inimigo}")
        print("----")

        # Turno do jogador
        jogador_terminou_turno = False
        while not jogador_terminou_turno:
            print("Ação:")
            print("1) Atacar")
            print("2) Pokémon")
            print("3) Mochila")
            print("4) Correr")
            acao = input("Escolha uma ação: ")

            if acao == "1":
                ataque_pokemon(pokemon_jogador, pokemon_inimigo)
                jogador_terminou_turno = True
            elif acao == "2":
                pokemons_jogador, jogador_atual = trocar_pokemon(pokemons_jogador, jogador_atual)
                jogador_terminou_turno = True
            elif acao == "3":
                usar_item(pokemon_jogador)
                jogador_terminou_turno = True
            elif acao == "4":
                print("Você fugiu da batalha.")
                jogador_terminou_turno = True
                break
            else:
                print("Ação inválida. Tente novamente.")

        if pokemon_jogador == None:
            pokemons_jogador, jogador_atual = trocar_pokemon(pokemons_jogador, jogador_atual)

        if pokemon_inimigo == None:
            inimigo_atual += 1

    if jogador_atual == 6:
        print("Você venceu a batalha!")
    else:
        print("Você perdeu a batalha.")

def ataque_pokemon(pokemon1, pokemon2):
    tipo_pokemon1 = pokedex[pokemon1]["TIPO"]
    ataques_pokemon1 = pokedex[pokemon1]["ATAQUES"]

    # Mostra os ataques disponíveis para o jogador
    print(f"Ataques disponíveis para {pokemon1}:")
    for i, ataque in enumerate(ataques_pokemon1):
        print(f"{i+1}) {ataque}")

    escolha_ataque = int(input("Escolha o número correspondente ao ataque: ")) - 1

    if escolha_ataque >= 0 and escolha_ataque < len(ataques_pokemon1):
        ataque_escolhido = ataques_pokemon1[escolha_ataque]
        tipo_ataque = ataques[ataque_escolhido]['TIPO']
        tipo_pokemon2 = pokedex[pokemon2]["TIPO"]

        # Verificar a relação de tipos para calcular o dano
        if tipo_ataque in tabela_tipos:
            if tipo_pokemon2 in tabela_tipos[tipo_ataque]:
                print(f"{pokemon1} usou {ataque_escolhido} contra {pokemon2}")
                print("----")
                print("Resultado: O ataque foi super efetivo!")
                # Lógica para aplicar dano aumentado
            elif tipo_ataque == tipo_pokemon2:
                print(f"{pokemon1} usou {ataque_escolhido} contra {pokemon2}")
                print("----")
                print("Resultado: O ataque não teve muito efeito.")
                # Lógica para aplicar dano reduzido
            else:
                print(f"{pokemon1} usou {ataque_escolhido} contra {pokemon2}")
                print("----")
                print("Resultado: O ataque causou dano normal.")
                # Lógica para aplicar dano normal

        else:
            print(f"{pokemon1} usou {ataque_escolhido} contra {pokemon2}")
            print("----")
            print("Resultado: O ataque causou dano normal.")
            # Lógica para aplicar dano normal

    else:
        print("Escolha inválida. Tente novamente.")

    # Função para trocar o Pokémon em batalha
    def trocar_pokemon(pokemons_jogador, jogador_atual):
        print("Pokémons disponíveis:")
        for i, pokemon in enumerate(pokemons_jogador):
            print(f"{i+1}) {pokemon}")

        escolha = int(input("Escolha o número correspondente ao Pokémon: ")) - 1

        if escolha >= 0 and escolha < len(pokemons_jogador):
            novo_pokemon = pokemons_jogador[escolha]
            pokemons_jogador[jogador_atual] = novo_pokemon
            jogador_atual += 1
            print(f"Você trocou para {novo_pokemon}.")
        else:
            print("Escolha inválida. Tente novamente.")

        return pokemons_jogador, jogador_atual

    # Função para usar um item durante a batalha
    def usar_item(pokemon):
        print("Itens disponíveis:")
        for item, quantidade in bag.items():
            print(f"{item}: {quantidade}")

        item = input("Digite o nome do item para usar: ")
        if item in bag:
            if bag[item] > 0:
                bag[item] -= 1
                print(f"Você usou {item} em {pokemon}.")
            else:
                print("Você não possui mais esse item.")
        else:
            print("Item inválido. Tente novamente.")

    # Chamando Funções:

    if opcao == "1":
            escolher_pokemon_batalha()
    elif opcao == "2":
        consultar_bag()
    elif opcao == "3":
        batalhar()
    elif opcao == "4":
        print("Obrigado por jogar!")
        continuar_jogo = False
    else:
        print("Opção inválida. Tente novamente.")