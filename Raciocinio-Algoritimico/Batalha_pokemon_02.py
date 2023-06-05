import random

# Definir Pokédex
pokedex = {}

# Definir Bag
bag = {
    "Poção de Cura": 5
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
    captured_pokemons = []
    
    while True:
        print("=========================================================================")
        print("Pokemon Adventure")
        print("Vamos iniciar nossa aventura e explorar o mundo para capturar Pokémon")
        print("1) MATOS ALTOS\n2) CAVERNAS\n3) CACHOEIRA\n4) FLORESTA\n5) FINALIZAR AVENTURA")
        print("=========================================================================")

        lugar = input("Digite um número para escolher um lugar para explorar ou para finalizar a aventura (1, 2, 3, 4 ou 5): ")

        if lugar == "5":
            print("Você capturou os seguintes Pokémon:")
            for pokemon in captured_pokemons:
                pokemon_count = captured_pokemons.count(pokemon)
                print(f"{pokemon_count}x {pokemon}")
                tipo, ataques = get_pokemon_info(pokemon)
                adicionar_pokemon_pokedex(pokemon, tipo, ataques)
            print("Obrigado por jogar!")
            break
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

            captured_pokemons.append(caught_pokemon)
            print("Eba você capturou um", caught_pokemon, "!")
        else:
            print("Lugar inválido, tente novamente")

# Função para obter informações de um Pokémon
def get_pokemon_info(pokemon):
    pokemons_info = {
        "Pikachu": ("Elétrico", ["Choque do Trovão", "Onda de Choque"]),
        "Squirtle": ("Água", ["Jato de Água", "Bolhas"]),
        "Charmander": ("Fogo", ["Lança-Chamas", "Brasa"]),
        "Rattata": ("Normal", ["Investida", "Dente de Sabre"]),
        "Pidgey": ("Normal, Voador", ["Ataque de Asas", "Tornado"]),
        "Gloom": ("Grama, Venenoso", ["Ácido", "Pó Venenoso"]),
        "Gengar": ("Fantasma, Venenoso", ["Bola Sombria", "Soco Sombrio"]),
        "Geodude": ("Pedra, Terra", ["Arremesso de Rocha", "Lançamento de Lodo"]),
        "Onix": ("Pedra, Terra", ["Terratemor", "Investida de Cabeça"]),
        "Magikarp": ("Água", ["Splash"]),
        "Lapras": ("Água, Gelo", ["Pulso do Dragão", "Hidro Bomba", "Raio de Gelo"]),
        "Bulbasaur": ("Grama, Venenoso", ["Folha Navalha", "Semente Sanguessuga"]),
        "Caterpie": ("Inseto", ["Seda", "Ventania"]),
        "Chikorita": ("Grama", ["Chicote de Vinha", "Ataque Rápido"])
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

print("=========================================================================")
print("Pokemon Battle")
print(f"Vamos iniciar nossa batalha contra o nosso rival {nome_rival} e tentaremos ganhar a todo custo")
print("=========================================================================")

# Função para escolher os Pokémon para a batalha
def escolher_pokemon_batalha():
    pokemons_disponiveis = list(pokedex.keys())
    pokemons_batalha = []

    print("Escolha 6 Pokémon para a batalha:")
    for cont in range(6):
        print(f"Escolha o Pokémon {cont+1}:")
        for j, pokemon in enumerate(pokemons_disponiveis):
            print(f"{j+1}) {pokemon}")

        escolha = int(input("Digite o número correspondente: ")) - 1

        if escolha >= 0 and escolha < len(pokemons_disponiveis):
            pokemon_escolhido = pokemons_disponiveis[escolha]
            pokemons_batalha.append(pokemon_escolhido)
            pokemons_disponiveis.remove(pokemon_escolhido)
        else:
            print("Escolha inválida. Tente novamente.")

    return pokemons_batalha

# Função para exibir e atualizar a bag
def consultar_bag():
    while True:
        print("================================")
        print("BAG - MOCHILA")
        print("1) Atualizar quantidade de itens")
        print("2) Ver os items e suas quantidades")
        print("3) Fechar a bag e salvar alterações")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            atualizar_quantidade_itens()
        elif opcao == "2":
            print("Alterações na bag salvas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para atualizar a quantidade de itens na bag
def atualizar_quantidade_itens():
    print("Itens disponíveis:")
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

    print("Início da batalha!")
    for i in range(6):
        print(f"Batalha {i+1}")
        pokemon_jogador = pokemons_jogador[i]
        pokemon_inimigo = pokemons_inimigo[i]
        print(f"Seu Pokémon: {pokemon_jogador}")
        print(f"Inimigo: {pokemon_inimigo}")
        print("----")
        print("Ação:")
        print("1) Atacar")
        print("2) Usar item")
        acao = input("Escolha uma ação: ")

        if acao == "1":
            ataque_pokemon(pokemon_jogador, pokemon_inimigo)
        elif acao == "2":
            usar_item(pokemon_jogador)
        else:
            print("Ação inválida. Tente novamente.")

# Função para realizar um ataque entre dois Pokémon
def ataque_pokemon(pokemon1, pokemon2):
    tipo_pokemon1 = pokedex[pokemon1]["TIPO"]
    ataques_pokemon1 = pokedex[pokemon1]["ATAQUES"]
    ataque_escolhido = random.choice(ataques_pokemon1)

    print(f"{pokemon1} usou {ataque_escolhido} contra {pokemon2}")
    print("----")
    print("Resultado: ...")
    
# Lógica do combate...

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
