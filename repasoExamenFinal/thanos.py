
def thanosVA(sol, numConex, situacion, info, N):
    if -1 not in sol:
        numConex+=1
    else:
        if 0 not in sol:
            for planeta in info[situacion]:
                if planeta not in sol:
                    sol[situacion] = planeta
                    numConex = thanosVA(sol, numConex, planeta, info, N)
                    sol[situacion] = -1
    return numConex


if __name__ == "__main__":
    N, M = list(map(int,input().strip().split()))
    listaPosibilidades = list()
    for i in range(M):
        listaPosibilidades.append(list(map(int,input().strip().split())))
    info = list()
    for i in range(N):
        info.append([])
    for i in range(M):
        info[listaPosibilidades[i][0]].append(listaPosibilidades[i][1])
        info[listaPosibilidades[i][1]].append(listaPosibilidades[i][0])
    sol = [-1] * N
    totalConexiones = thanosVA(sol, 0, 0, info, N)


    print(totalConexiones)