inf = input().split()

id = int(inf[0])
lightState = inf[1]
state = int(inf[2])

resultado = "CONTINUAR"

if lightState == "r" and state == 1:
    resultado = "ELIMINADO"

print("Jugador", id, resultado)
