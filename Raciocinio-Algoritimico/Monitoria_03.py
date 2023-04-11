import random

lugar = ''
capturedPokemons = []
grassLandPokemons = ["Ratata", "Pidgey", "Entei"]
cavernePokemons = ["Zubat", "Geodute", "Raticate"]

while lugar != "3":

    print("=========================================================================")
    print("Pokemon Adventure")
    print("Vamos iniciar nossa aventura e explorar o mundo para capturar Pokémon")
    print("1) MATOS ALTOS\n2) CAVERNAS\n3) FINALIZAR AVENTURA")
    print("=========================================================================")

    lugar = input("Escolha um lugar para explorar, 1 ou 2 ou 3: ")

    if lugar == "1":
        pokemonAleatorio = random.randint(0, len(grassLandPokemons)-1)
        catchedPokemons = grassLandPokemons[pokemonAleatorio]
        capturedPokemons.append(catchedPokemons)
        print("Eba você capturou um " + str(catchedPokemons) + " !")
    elif lugar == "2":
        pokemonAleatorio = random.randint(0, len(cavernePokemons)-1)
        catchedPokemons = cavernePokemons[pokemonAleatorio]
        capturedPokemons.append(catchedPokemons)
        print("Eba você capturou um " + str(catchedPokemons) + " !")
    elif lugar == "3":
        print("Você capturou os seguintes Pokémon:")
        for pokemon in capturedPokemons:
            pokemonCont = str(capturedPokemons.count(pokemon))
            print(pokemonCont + "x " + pokemon)
        print("Obrigado por jogar!")
    else:
        print("Lugar inválido, tente novamente")
        lugar = input("Escolha um lugar para explorar, 1 ou 2 ou 3:")
