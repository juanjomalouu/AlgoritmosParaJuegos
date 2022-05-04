
def esSolucion(miRuta, totalPlanetas):
    return len(miRuta) == totalPlanetas

def esFactible(listaConexion, miRuta, planetaActual, i,totalPlanetas):
    if listaConexion[i][0] == planetaActual:
        if listaConexion[i][1] not in miRuta and len(miRuta) <= totalPlanetas:
            return True
    elif listaConexion[i][1] == planetaActual:
        if listaConexion[i][0] not in miRuta and len(miRuta) <= totalPlanetas:
            return True
    else:
        return False

def thanosVA(listaConexion, numRutas, miRuta, planetaActual, totalPlanetas):
    if esSolucion(miRuta, totalPlanetas):
        hayConexion = False
        for i in listaConexion:
            if planetaActual in i and 0 in i:
                hayConexion = True
        if hayConexion:
            numRutas+=1
    else:
        for i in range(len(listaConexion)):
            if esFactible(listaConexion, miRuta, planetaActual, i,totalPlanetas):
                if listaConexion[i][0] != planetaActual:
                    miRuta.append(listaConexion[i][0])
                    numRutas = thanosVA(listaConexion, numRutas, miRuta, listaConexion[i][0],totalPlanetas)
                    miRuta.pop()
                else:
                    miRuta.append(listaConexion[i][1])
                    numRutas = thanosVA(listaConexion, numRutas, miRuta,listaConexion[i][1],totalPlanetas)
                    miRuta.pop()
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
    sol = [-1]*numPlanetas
    print(info)
    totalConexiones = thanosVA(sol, 0, 0, info, numPlanetas)
    print(totalConexiones)