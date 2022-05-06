
def thanosVA(sol, numRutas, planActual,info, total):
    if -1 not in sol:
        numRutas+=1
    else:
        if 0 not in sol:
            for planeta in info[planActual]:
                if planeta not in sol:
                    sol[planActual] = planeta
                    numRutas = thanosVA(sol, numRutas, planeta, info, total)
                    sol[planActual] = -1
    return numRutas


if __name__ == "__main__":
    N, M = list(map(int,input().strip().split()))
    listaConexiones = list()
    for i in range(M):
        listaConexiones.append(list(map(int,input().strip().split())))

    data = [] * N
    for i in range(N):
        data.append([])
    for i in range(M):
        data[listaConexiones[i][0]].append(listaConexiones[i][1])
        data[listaConexiones[i][1]].append(listaConexiones[i][0])
    sol = [-1] * N

    totalConexiones = thanosVA(sol,0,0,data,N)
    print(totalConexiones)