#var = 60
#for cont in range(10, 100, 10):
    #if cont == var:
        #print("Saindo antes")
        #break
    #var = var - 10
#print("Var = ", var)

#var = 5
#for cont_ext in range(4):
    #for cont_int in range(4):
        #if cont_ext == cont_int:
            #print("Var = ", var)
#print(cont_ext)

#qtde_pratos = int(input("Digite a quantidade de pratos: "))
#soma_pesos = 0

#temp_celsius = float(input("Temp em C:"))
#temp_fahr = (temp_celsius * (9/5)) + 32
#print("Temp em F: ", temp_fahr)

#for i in range(qtde_pratos):
  #nome_prato = input("Digite o nome do prato: ")
  #peso_prato = float(input("Digite o peso do prato em kg: "))
  #soma_pesos += peso_prato

#media_quilo_prato = soma_pesos / qtde_pratos

#print(f"A média de peso dos pratos é {media_quilo_prato:.2f} kg.")

cont_votos1 = 0
cont_votos2 = 0
numero_estudantes = int(input("Numero estudantes: "))
for cont_votos in range(numero_estudantes):
    print("Digite 1 p/ cand 1")
    print("Digite 2 p/ cand 2")
    voto = int(input("Escolha: "))
if voto == 1:
    cont_votos1 = cont_votos1 + 1
elif voto == 2:
    cont_votos2 = cont_votos2 + 1
else:
    print("Voto inválido")
print("Votos cand 1: ", cont_votos1)
print("Votos cand 2: ", cont_votos2)




