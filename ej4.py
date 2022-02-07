cadena = input("Introduzca la palabra a adivinar")
listaLetras = "_"*len(cadena)

intentos = 0

def comprobarLetra(letra, cadena, listaLetras):
    for i in range(len(cadena)):
        if letra == cadena[i]:
            listaLetras[i] = letra
            print("Has acertado, la letra se encuentra: ")
            print(listaLetras)
        elif i==len(cadena):
            print("Fallaste XD")
    return listaLetras

while intentos < 10 and listaLetras != cadena:
    print("Introduce una letra: ")
    letra = input()
    listaLetras = comprobarLetra(letra,cadena,listaLetras)


