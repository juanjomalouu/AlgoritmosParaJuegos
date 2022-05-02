
def inicializarGrafo():
    grafo = {}
    grafo['n'] = 4
    grafo['adyacencia'] = [[1,2,3],[0],[0,3],[0,2]]
    return grafo

def inicializarSolucion(grafo):
    sol = [0] * grafo['n']
    return sol

def coloreadoVA(grafo,m,sol,nodo):
    if nodo >= grafo['n']:
        esSol = True
    else:
        esSol = False
        color = 1
        while not esSol and color <=m:
            if esFactible(grafo, sol, nodo, color):
                sol[nodo] = color
                [sol, esSol] = coloreadoVA(grafo,m,sol,nodo+1)
                if not esSol:
                    sol[nodo] = 0
            color +=1
    return sol, esSol

def esFactible(grafo,sol,nodo,color):
    factible = True
    adyacenciaNodo = grafo['adyacencia'][nodo][:]
    i = 0
    while factible and i < len(adyacenciaNodo):
        if adyacenciaNodo[i] < nodo:
            factible = color != sol[adyacenciaNodo[i]]
        i+=1
    return factible




#Prog Ppal:
grafo = inicializarGrafo()
sol = inicializarSolucion(grafo)
m = 3
nodo = 0
[sol, esSol] = coloreadoVA(grafo,m,sol,nodo)
if esSol:
    print(sol)
else:
    print("No ha sido posible encontrar una sol")