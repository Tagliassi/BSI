print("Welcome to the pokemon world")

nomeJogador = input("Digite seu nome jogador:")
generoJogador = input("Digite seu gênero jogador:")
nomeRival = input("Digite o nome do rival:")

print(f"Olá {nomeJogador}, então o nome do seu rival é {nomeRival}, boa sorte em sua jornada!")

pokemonInicial = input(
    "Escolha seu Pokémon inicial, Pikachu, Charmander ou Pidgey:")

if pokemonInicial == "Pikachu" or pokemonInicial == "Charmander" or pokemonInicial == "Pidgey":
    print(f"Parabéns seu pokemon inicial é {pokemonInicial}")
else:
    print("Não reconheci esse pokemon, nenhum pokemon foi selecionado")
