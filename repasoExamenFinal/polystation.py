
def dYVPlaystation(listaRec, buscar, ini, fin, nombre):
    listaSolucion = list()
    mitad = (ini + fin) // 2
    if ini > fin:
        diferencia = listaRec[mitad+1][0]-buscar
        listaSolucion.append(nombre)
        listaSolucion.append(listaRec[mitad+1][1])
        listaSolucion.append(diferencia)
        return listaSolucion
    else:
        if buscar == listaRec[mitad][0]:
            diferencia = listaRec[mitad][0] - buscar
            listaSolucion.append(nombre)
            listaSolucion.append(listaRec[mitad][1])
            listaSolucion.append(diferencia)
            return listaSolucion
        else:
            if buscar <= listaRec[mitad][0]:
                return dYVPlaystation(listaRec, buscar, ini, mitad-1, nombre)
            else:
                return dYVPlaystation(listaRec, buscar, mitad+1, fin, nombre)

if __name__ == "__main__":
    numRecompensas = int(input())
    listaRecompensas = list()
    for i in range(numRecompensas):
        info = list(input().strip().split())
        num = int(info[0])
        name = info[1]
        listaRecompensas.append([num,name])
    numJugadores = int(input())
    listaJugadores = list()
    for i in range(numJugadores):
        info = list(input().strip().split())
        num = info[0]
        name = int(info[1])
        listaJugadores.append([num,name])

    ganadores = list()
    for i in range(numJugadores):
        resultado = dYVPlaystation(listaRecompensas, listaJugadores[i][1], 0, numRecompensas-1, listaJugadores[i][0])
        ganadores.append(resultado)
    ganadores.sort(key=lambda x:x[2])
    for i in range(len(ganadores)):
        if ganadores[i][2] == ganadores[0][2]:
            print(ganadores[i][0] + " " + ganadores[i][1])

