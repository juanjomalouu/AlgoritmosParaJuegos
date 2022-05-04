
def inicializarTuplaVacia(N):
    sol = {}
    sol['tupla'] = [0] * N
    sol['coste'] = 0
    return sol

def printCasillas(casillas,n):
    for i in range(n):
        for j in range(n):
            print(casillas[i][j], end=" ")
        print()

def existeConexionInicial(planetaActual, conexiones):
    existe = False
    for i in range(len(conexiones)):
        if planetaActual in conexiones[i] and 0 in conexiones[i]:
            existe = True
    return existe

def esSolucion(planetasVisitados, totalPlanetas, conexiones):
    return planetasVisitados == totalPlanetas and existeConexionInicial(planetasVisitados, conexiones)

def esFactible(sol, planeta, planetasVisitados):
    return planeta not in sol['tupla'][0:planetasVisitados]

def asignar(sol,planeta,k,datos,N):
    sol['tupla'][k] = planeta
    sol['coste'] += datos[sol['tupla'][k-1]][planeta]
    if k == N-1:
        sol['coste'] += datos[planeta][sol['tupla'][0]]
    return sol

def borrar(sol,planeta,k,datos,N):
    sol['tupla'][k] = 0
    sol['coste'] -= datos[sol['tupla'][k-1]][planeta]
    if k == N-1:
        sol['coste'] -= datos[planeta][sol['tupla'][0]]
    return sol

def thanosVA(sol, conexiones, numSols, planetasVisitados):
    N = numPlanetas
    if esSolucion(planetasVisitados, N, conexiones):
        return 1
    else:
        for planeta in range(1,N):
            if esFactible(sol, planeta, planetasVisitados):
                sol = asignar(sol, planeta, planetasVisitados, conexiones, N)
                numSols += thanosVA(sol, conexiones,numSols, planetasVisitados+1)
                sol = borrar(sol, planeta, planetasVisitados, conexiones, N)
    return numSols

if __name__ == "__main__":
    numPlanetas, numConexiones = list(map(int,input().strip().split()))
    listaConexiones = [0]*numPlanetas
    for i in range(len(listaConexiones)):
        listaConexiones[i] = [0]*numPlanetas
    planetasVisitados = [0] * numPlanetas
    for i in range(numConexiones):
        lineaConexion = list(map(int,input().strip().split()))
        listaConexiones[lineaConexion[0]][lineaConexion[1]] = 1
        listaConexiones[lineaConexion[1]][lineaConexion[0]] = 1
    k = 1
    conexionesFinales = inicializarTuplaVacia(numConexiones)
    #printCasillas(listaConexiones, numPlanetas)
    totalConexiones = thanosVA(conexionesFinales, listaConexiones, 0, k)
    print(totalConexiones)