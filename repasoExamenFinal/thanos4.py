
def thanosVA(sol, datos, numRutas, planActual):
    if -1 not in sol:
        numRutas+=1
    else:
        if 0 not in sol:
            for planeta in datos[planActual]:
                if planeta not in sol:
                    sol[planActual] = planeta
                    numRutas = thanosVA(sol, datos, numRutas, planeta)
                    sol[planActual] = -1
    return numRutas



if __name__ == "__main__":
    N, M = list(map(int,input().strip().split()))
    listaConexiones = list()
    for i in range(M):
        listaConexiones.append(list(map(int,input().strip().split())))
    datos = list()
    for i in range(N):
        datos.append([])
    for i in range(M):
        datos[listaConexiones[i][0]].append(listaConexiones[i][1])
        datos[listaConexiones[i][1]].append(listaConexiones[i][0])

    sol = [-1] * N
    numRutas = 0
    planActual = 0
    total = N
    mejorSol = thanosVA(sol, datos, numRutas, planActual)
    print(mejorSol)