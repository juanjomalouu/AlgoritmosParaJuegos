
def kruskal(cantidad_nodos, listaArcos):
    sol = []
    arcos = sorted(listaArcos, key=lambda x: x[2])
    ejes = 0
    padre = [x for x in range(cantidad_nodos)]
    while ejes < cantidad_nodos -1:
        eje = arcos.pop(0)
        x = get_root(padre,eje[0])
        y = get_root(padre,eje[1])
        if x != y:
            ejes+=1
            sol.append(eje[2])
            padre[x] = y
    return sol

def get_root(padre, i):
    if padre[i] == i:
        return i
    return get_root(padre, padre[i])