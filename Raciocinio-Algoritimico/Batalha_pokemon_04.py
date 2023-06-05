import random

# Definir Pokédex
pokedex = {}

# Definir Bag
bag = {
    "Poção": 3,
    "Super Poção": 5,
}

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

# Função para adicionar Pokémon à Pokédex
def adicionar_pokemon_pokedex(pokemon):
    global pokedex
    pokedex[pokemon] = get_pokemon_info(pokemon)

# Função para escolher o Pokémon inicial
def escolher_pokemon_inicial():
    pokemons_validos = [
        "Pikachu",
        "Squirtle",
        "Charmander",
    ]
    
    while True:
        pokemon_inicial = input("Escolha seu pokémon inicial (Pikachu, Squirtle, Charmander): ")
        if pokemon_inicial in pokemons_validos:
            print(f"Parabéns, seu pokémon inicial é {pokemon_inicial}")
            info = get_pokemon_info(pokemon_inicial)
            vida = info["VIDA"]
            resistencias = info["RESISTENCIAS"]
            fragilidades = info["FRAGILIDADES"]
            adicionar_pokemon_pokedex(pokemon_inicial)
            break
        else:
            print("Pokémon inválido. Escolha um dos seguintes pokémons: Pikachu, Squirtle, Charmander.")

try:
    escolher_pokemon_inicial()
except ValueError as e:
    print(str(e))

# Iniciar aventura e capturar Pokémon inicial
print("Welcome to the Pokemon world")

nome_jogador = input("Digite seu nome jogador: ")
nome_rival = input("Digite o nome do rival: ")

print(f"Olá {nome_jogador}, então o nome do seu rival é {nome_rival}, boa sorte em sua jornada!")

# Capturar novos Pokémon
def pokemon_adventure():
    captured_pokemons = []

    print("=========================================================================")
    print("Pokemon Adventure")
    print("Vamos iniciar nossa aventura e explorar o mundo para capturar Pokémon")
    print("1) MATOS ALTOS\n2) CAVERNAS\n3) CACHOEIRA\n4) FLORESTA\n5) FINALIZAR AVENTURA")
    print("=========================================================================")
    
    while True:
        lugar = input("Digite um número para escolher um lugar para explorar ou para finalizar a aventura (1, 2, 3, 4 ou 5): ")

        if lugar == "5":
            if len(captured_pokemons) >= 5:
                print("Você capturou os seguintes Pokémon:")
                for pokemon in captured_pokemons:
                    pokemon_count = captured_pokemons.count(pokemon)
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
                wild_pokemon = random.choice(grass_land_pokemons)
            elif lugar == "2":
                wild_pokemon = random.choice(cave_pokemons)
            elif lugar == "3":
                wild_pokemon = random.choice(waterfall_pokemons)
            else:
                wild_pokemon = random.choice(forest_pokemons)

            print(f"Você encontrou um {wild_pokemon} selvagem!")
            capture = input("Deseja capturá-lo? (S/N): ")
            if capture.upper() == "S":
                captured_pokemons.append(wild_pokemon)
                adicionar_pokemon_pokedex(wild_pokemon)  
                print(f"Parabéns, você capturou o {wild_pokemon}!")
            else:
                print("Você decidiu não capturar o Pokémon.")

pokemon_adventure()

# Função para escolher os Pokémon para a batalha
def escolher_pokemon_batalha():
    print("Escolha os 6 Pokémon para a batalha:")
    pokemon_batalha = []

    while len(pokemon_batalha) < 6:
        exibir_pokemons_disponiveis()

        escolha = input("Escolha um Pokémon pelo número (ou X para finalizar a escolha): ")
        if escolha.lower() == "x":
            break
        elif escolha.isdigit() and 1 <= int(escolha) <= len(pokedex):
            pokemon_escolhido = list(pokedex.keys())[int(escolha) - 1]
            if pokemon_escolhido not in pokemon_batalha:
                pokemon_batalha.append(pokemon_escolhido)
                print(f"Você escolheu {pokemon_escolhido} para a batalha.")
            else:
                print(f"Você já escolheu {pokemon_escolhido} para a batalha.")
        else:
            print("Escolha inválida, tente novamente.")

    return pokemon_batalha

# Função para exibir os Pokémon disponíveis na Pokédex
def exibir_pokemons_disponiveis():
    print("Pokémons da sua pokedex:")
    for i, pokemon in enumerate(pokedex, 1):
        print(f"{i}) {pokemon}")

# Função para consultar informações de um Pokémon na Pokédex
def consultar_pokemon(pokemon):
    pokemon_info = pokedex.get(pokemon)
    if pokemon_info:
        tipo = pokemon_info["TIPO"]
        ataques = pokemon_info["ATAQUES"]
        vida = pokemon_info["VIDA"]
        resistencias = pokemon_info["RESISTENCIAS"]
        fragilidades = pokemon_info["FRAGILIDADES"]
        print(f"Informações de {pokemon}:")
        print(f"Tipo: {tipo}")
        print(f"Ataques: {ataques}")
        print(f"Vida: {vida}")
        print(f"Resistências: {resistencias}")
        print(f"Fragilidades: {fragilidades}")
    else:
        print("Pokémon não encontrado na Pokédex.")

# Função para realizar a batalha
def batalhar():
    print("Batalha iniciada!")
    # Implemente a lógica da batalha aqui

# Função para consultar a Bag
def consultar_bag():
    print("Consultando Bag...")
    print("Itens disponíveis:")
    for item, quantidade in bag.items():
        print(f"{item}: {quantidade}")

# Função para exibir itens da Bag
def exibir_itens():
    print("Itens disponíveis na bag:")
    for i, item in enumerate(bag, 1):
        print(f"{i}) {item}")

# Função para atualizar a quantidade de itens na Bag
def atualizar_quantidade_itens(item, quantidade):
    if item in bag:
        bag[item] += quantidade
        print(f"A quantidade de {item}(s) foi atualizada para {bag[item]}.")
    else:
        bag[item] = quantidade
        print(f"O item {item} foi adicionado à Bag com quantidade {quantidade}.")

# Loop principal do jogo
while True:
    print("=========================================================================")
    print("POKEMON GAME")
    print("1) AVENTURA\n2) BATALHAR\n3) POKÉDEX\n4) BAG\n5) SAIR")
    print("=========================================================================")

    escolha = input("Digite um número para escolher uma opção (1, 2, 3, 4 ou 5): ")

    if escolha == "1":
        pokemon_adventure()
    elif escolha == "2":
        pokemon_batalha = escolher_pokemon_batalha()
        if len(pokemon_batalha) < 6:
            print("Você precisa escolher 6 Pokémon para a batalha.")
        else:
            batalhar()
    elif escolha == "3":
        exibir_pokemons_disponiveis()
        pokemon = input("Digite o NOME do pokemon que queira ver as informações: ")
        consultar_pokemon(pokemon)
    elif escolha == "4":
        consultar_bag()
        exibir_itens()
        item_bag = input("Digite o número do item que deseja adicionar (ou X para sair): ")
        if item_bag.lower() == "x":
            continue
        elif item_bag.isdigit() and 1 <= int(item_bag) <= len(bag):
            item_escolhido = list(bag.keys())[int(item_bag) - 1]
            quantidade_itens = int(input("Digite a quantidade de itens que deseja adicionar: "))
            atualizar_quantidade_itens(item_escolhido, quantidade_itens)
        else:
            print("Escolha inválida, tente novamente.")
    elif escolha == "5":
        print("Obrigado por jogar!")
        break
    else:
        print("Escolha inválida, tente novamente.")
