pokedex = {"GENGAR" : 
           {  "TIPO" : "GHOST", 
            "ATAQUES" : ("SHADOW BALL", "LICK", "BITE"),
            "VIDA" : 12
           },
           "VOLTORB" :
           {
             "TIPO" : "ELETRICO",
             "ATAQUES" : ("THUNDERBOLT", "HEADBUTT", "SHOCKWAVE"),
             "VIDA" : -20
           },
           "GROWLITHE" :
           {
             "TIPO" : ("FOGO", "NORMAL"),
             "ATAQUES" : ("CHARGE", "FLAMETHROWER", "SCRATCH"),
             "VIDA" : 12
           }      
          }

comando = 0

def estaVivo(vidaPokemon):
  if vidaPokemon > 0:
    print("Esta Vivo")
  else :
    print("Esta Morto")

while(comando != 9):

  comando = input("Insira um nome de pokemon para obter suas informações! \n Ou insira 9 para encerrar: ")

  pokemon = pokedex.get(comando)
  estaVivo(pokemon.get("VIDA"))