# Formato pokemon: [NOME, TIPO, NOMEATAQUE, VIDA, DANO]
pokemon1 = ["Blastoise", "Water", "Watergun", 186, 40]
pokemon2 = ["Charizard", "Fire", "Flamethrower", 185, 85]


def isAlive(pokemon):
    hp = pokemon[3]
    if hp > 0:
        return True
    return False


def checkEffectivines(atkType, defensorType):
    if atkType == "Water":
        if defensorType == "Fire" or defensorType == "Ground" or defensorType == "Rock":
            return "Super Effective"
        elif defensorType == "Grass" or defensorType == "Dragon" or defensorType == "Water":
            return "Ineffective"

    if atkType == "Fire":
        if defensorType == "Bug" or defensorType == "Steel" or defensorType == "Ice" or defensorType == "Grass":
            return "Super Effective"
        elif defensorType == "Rock" or defensorType == "Dragon" or defensorType == "Water" or defensorType == "Fire":
            return "Ineffective"
    return "Neutral"


def attack(attacker, defender):
    attackerName = attacker[0]
    attackerType = attacker[1]
    attackerAtkName = attacker[2]
    attackerAtkDamage = attacker[4]

    defenderName = defender[0]
    defenderType = defender[1]

    print(attackerName + " atacou: " + defenderName + "\nCom o ataque: " +
          attackerAtkName)

    damageDealed = attackerAtkDamage

    if checkEffectivines(attackerType, defenderType) == "Super Effective":
        damageDealed = damageDealed * 2
    elif checkEffectivines(attackerType, defenderType) == "Ineffective":
        damageDealed = damageDealed / 2

    defender[3] -= damageDealed

    print(defenderName + " recebeu " + str(damageDealed) + " de dano!")
    print("Ele está atualmente com: " + str(defender[3]) + " de vida!\n")

    if isAlive(defender) == False:
        print(defenderName + " está fora de combate!")


while isAlive(pokemon1) and isAlive(pokemon2):
    attack(pokemon1, pokemon2)

    if isAlive(pokemon2):
        attack(pokemon2, pokemon1)
