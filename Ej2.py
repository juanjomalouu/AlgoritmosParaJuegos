from random import randint
print("Introduzca el numero mayor en el que se peude generar la patata")
n = int(input())
aleatorio = randint(0,n)

def preguntarUsuario():
    print("Introduzca un numero para adivinar: ")
    numUser = int(input())
    return numUser

def checkSize (num, aleatorio):
    acierto = False
    if num > aleatorio:
        print("El numero introducido es mayor")
    elif num < aleatorio:
        print("El numero introducido es menor")
    else:
        acierto = True
        print("Has acertado")
    return acierto
acertado = False
while acertado==False:
    acertado= checkSize(preguntarUsuario(),aleatorio)