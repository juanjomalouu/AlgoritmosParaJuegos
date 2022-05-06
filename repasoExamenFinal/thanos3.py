

def thanosVA(sol, datos, planetaActual, numRutas):
    if -1 not in sol:
        numRutas +=1
    else:
        if 0 not in sol:
            for planeta in datos[planetaActual]:
                if planeta not in sol:
                    sol[planetaActual] = planeta
                    numRutas = thanosVA(sol, datos, planeta, numRutas)
                    sol[planetaActual] = -1
    return numRutas

if __name__ == "__main__":
    N, M = list(map(int,input().strip().split()))
    listaConex = list()
    for i in range(M):
        listaConex.append(list(map(int,input().strip().split())))
    datos = list()
    for i in range(N):
        datos.append([])
    for i in range(M):
        datos[listaConex[i][0]].append(listaConex[i][1])
        datos[listaConex[i][1]].append(listaConex[i][0])

    sol = [-1] * N
    sol = thanosVA(sol, datos, )
