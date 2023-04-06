# pokemon = input("Digite CAPTURAR para pegar um pokémon ou EXIT para sair:")
# todosOsNomesPokemon = ""

# while pokemon != "EXIT":
# nome = input("Digite o pokémon que você capturou:")
# todosOsNomesPokemon += nome + ' '
# print(f"{nome} foi capturado com sucesso!")
# pokemon = input("Digite CAPTURAR para pegar um pokémon ou EXIT para sair:")

# print("Obrigado por jogar! Aqui estão os pokémons que você capturou:")
# print(todosOsNomesPokemon)

import random

print("=========================================================================")
print("Vamos iniciar nossa aventura e explorar o mundo para capturar Pokémon")
print("1) MATOS ALTOS 2) CAVERNAS")
print("=========================================================================")

lugar = input("Escolha um lugar para explorar, 1 ou 2: ")
pokemonsCapturados = []
comandoJogador = ''

while comandoJogador != "EXIT":
    if lugar == "1":
        pokemonAleatorioMato = random.randint(1, 3)
        if pokemonAleatorioMato == 1:
            print("Parabéns voce pegou um Ratata")
            pokemonsCapturados = pokemonsCapturados + ["Ratata"]
        elif pokemonAleatorioMato == 2:
            print("Parabéns voce pegou um Pidgey")
            pokemonsCapturados = pokemonsCapturados + ["Pidgey"]
        else:
            print("Parabéns voce pegou um Dito")
            pokemonsCapturados = pokemonsCapturados + ["Dito"]
    elif lugar == "2":
        pokemonAleatorioCaverna = random.randint(4, 6)
        if pokemonAleatorioCaverna == 4:
            print("Parabéns voce pegou um Zubat")
            pokemonsCapturados = pokemonsCapturados + ["Zubat"]
        elif pokemonAleatorioCaverna == 5:
            print("Parabéns voce pegou um Geodute")
            pokemonsCapturados = pokemonsCapturados + ["Geodute"]
        else:
            print("Parabéns voce pegou um Raticate")
            pokemonsCapturados = pokemonsCapturados + ["Raticate"]
    else:
        print("Lugar inválido, tente novamente")
        lugar = input("Escolha um lugar para explorar, 1 ou 2:")
        continue

    comandoJogador = input(
        "Digite EXIT para sair ou aperte ENTER para continuar a capturar pokémon:")
    if comandoJogador == "EXIT":
        break
    lugar = input("Escolha um lugar para explorar, 1 ou 2:")

print("Você capturou os seguintes Pokémon:")
for pokemon in pokemonsCapturados:
    print("- " + pokemon)
print("Obrigado por jogar!")
