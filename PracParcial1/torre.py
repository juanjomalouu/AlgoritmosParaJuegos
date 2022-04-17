
def algoritmoVoraz(lista, tiempo):
    tiempoGastado = 0
    while tiempoGastado<=tiempo and lista != []:
        print(lista[0])
        tiempoGastado +=lista[0][1]
        del lista[0]



if __name__ == "__main__":
    rango = int(input())
    numEnemigos = int(input())
    listaEnemigos = list()
    for i in range(numEnemigos):
        listaAux = list()
        entrada = input().strip().split()
        listaAux.append(entrada[0])
        listaAux.append(int(entrada[1]))
        listaAux.append(int(entrada[2]))
        porcentaje = int(entrada[2])/int(entrada[1])
        listaAux.append(porcentaje)
        listaAux.append(i)
        listaEnemigos.append(listaAux)
    listaEnemigos.sort(key=lambda x:x[4])
    print(listaEnemigos)
    listaEnemigos.sort(key = lambda x:x[3])

    algoritmoVoraz(listaEnemigos, rango)
