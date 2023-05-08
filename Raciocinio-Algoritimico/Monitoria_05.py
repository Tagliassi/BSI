#Tuplas e dicionários

#meu_dicionario = {"chave_1" : "item1", "chave_2" : "item2"}
#meu_dicionario = {}

#minha_tupla = ("item1","item2","item3")
#minha_tupla = ()

pokedex = {"GENGAR" :{
    "TIPO" : "GHOST",
    "ATAQUES" : ("SHADOW BALL", "LICK", "BITE")
    },
    "VOLTORB" :
    {
        "TIPO" : "ELETRICO",
        "ATAQUES" :  ("THUNDEBOLT", "HEADBUTT", "SHOCKWAVE") 
     },
    "GROWLITHE" :
    {
        "TIPO" : ("FOGO", "NORMAL"),
        "ATAQUES" :  ("CHARGE", "FLAMETHROWER", "SCRATCH") 
     }

    }

comando = 0

while comando != 9:
    comando = input("Insira um nome de um pokemon para consultar suas informacoes \n ou insira 9 para encerrar: ")

    if comando != 9:
        print(pokedex.get(comando))
    else:
        print("Volte sempre")
