import random

# Definir Pokédex
pokedex = {}

# Função para adicionar Pokémon à Pokédex
def adicionar_pokemon_pokedex(pokemon):
    pokedex[pokemon] = {
        "TIPO": "Desconhecido",
        "ATAQUES": ()
    }

# Função para atualizar informações de um Pokémon na Pokédex
def atualizar_pokemon_pokedex(pokemon, tipo, ataques):
    if pokemon in pokedex:
        pokedex[pokemon]["TIPO"] = tipo
        pokedex[pokemon]["ATAQUES"] = ataques
        print(f"As informações de {pokemon} foram atualizadas na Pokédex.")
    else:
        print("Pokémon não encontrado na Pokédex.")

# Função para escolher o Pokémon inicial
def escolher_pokemon_inicial(pokemon_inicial):
    pokemons_validos = ["Pikachu", "Charmander", "Squirtle"]

    if pokemon_inicial in pokemons_validos:
        print(f"Parabéns, seu pokémon inicial é {pokemon_inicial}")
        adicionar_pokemon_pokedex(pokemon_inicial)
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
                adicionar_pokemon_pokedex(pokemon)
            print("Obrigado por jogar!")
            break
        elif lugar in ["1", "2", "3", "4"]:
            grass_land_pokemons = ["Ratata", "Pidgey", "Gloom"]
            cave_pokemons = ["Gengar", "Geodute", "Onix"]
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
            adicionar_pokemon_pokedex(caught_pokemon)
        else:
            print("Lugar inválido, tente novamente")

pokemon_adventure()

print("Eba você capturou seu pokemon inicial e todos os pokemons que queria, agora atualize as informações de cada um em sua pokedex")

# Atualizar informações de cada Pokémon capturado
captured_pokemons = list(pokedex.keys())
total_pokemons = len(captured_pokemons)
updated_pokemons = 0

for pokemon in captured_pokemons:
    tipo = input(f"Digite o tipo do Pokémon {pokemon}: ")
    ataques = tuple(input(f"Digite os ataques do Pokémon {pokemon} separados por vírgula: ").split(","))
    atualizar_pokemon_pokedex(pokemon, tipo, ataques)
    updated_pokemons += 1
    remaining_pokemons = total_pokemons - updated_pokemons
    print(f"{remaining_pokemons} Pokémon(s) faltando para atualizar")

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
