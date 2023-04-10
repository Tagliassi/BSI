import random

print("=========================================================================")
print("Pokemon Adventure")
print("Vamos iniciar nossa aventura e explorar o mundo para capturar Pokémon")
print("1) MATOS ALTOS, 2) CAVERNAS, 3) FINALIZAR AVENTURA")
print("=========================================================================")

lugar = input("Escolha um lugar para explorar, 1 ou 2 ou 3: ")
comandoJogador = ''
capturedPokemons = []
grassLandPokemons = ["Ratata", "Pidgey", "Entei"]
cavernePokemons = ["Zubat", "Geodute", "Raticate"]

while comandoJogador != "3":
    if lugar == "1":
        pokemonAleatorio = random.randint(0, len(grassLandPokemons)-1)
        catchedPokemons = grassLandPokemons[pokemonAleatorio]
        capturedPokemons.append(catchedPokemons)
        print("Eba você capturou um" + str(capturedPokemons) + " !")
    elif lugar == "2":
        pokemonAleatorio = random.randint(0, len(cavernePokemons)-1)
        catchedPokemons = cavernePokemons[pokemonAleatorio]
        capturedPokemons.append(catchedPokemons)
        print("Eba você capturou um" + str(capturedPokemons) + " !")
    elif lugar == "3":
        print("Obrigado por jogar!, Você capturou os seguintes Pokémon:")
        for pokemon in capturedPokemons:
        print("- " + pokemon)
        print("Obrigado por jogar!")       
    else:
        print("Lugar inválido, tente novamente")
        lugar = input("Escolha um lugar para explorar, 1 ou 2 ou 3:")
