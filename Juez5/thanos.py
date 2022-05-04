
def thanosVA(sol, numRutas, planetaActual, info, totalPlanetas):
    if -1 not in sol:
        numRutas+=1
    else:
        if 0 not in sol:
            for planeta in info[planetaActual]:
                if planeta not in sol:
                    sol[planetaActual] = planeta
                    numRutas = thanosVA(sol, numRutas, planeta, info, totalPlanetas)
                    sol[planetaActual] = -1
    return numRutas

if __name__ == "__main__":
    numPlanetas, numConexiones = list(map(int,input().strip().split()))
    listaConexion = list()
    for i in range(numConexiones):
        listaConexion.append(list(map(int,input().strip().split())))
    info = list()
    for i in range(numPlanetas):
        info.append([])
    for i in range(numConexiones):
        info[listaConexion[i][0]].append(listaConexion[i][1])
        info[listaConexion[i][1]].append(listaConexion[i][0])
    sol = [-1] * numPlanetas
    totalConexiones = thanosVA(sol, 0, 0, info, numPlanetas)
    print(totalConexiones)