import copy


def mochilaBT(datos, sol, mejorSol, k):
    if esSolucion(sol,datos):
        mejorSol = mejorSolucion(sol, mejorSol)
    else:
        for i in range(k, datos['N']):
            if esFactible(sol, datos, i):
                sol = asignar(sol, datos,i)
                mejorSol = mochilaBT(datos, sol, mejorSol, i)
                sol = borrar(sol, datos,i)
    return mejorSol

def mejorSolucion(sol1, sol2):
    if sol1["valor"] > sol2["valor"]:
        mejor = copy.deepcopy(sol1)
    else:
        mejor = copy.deepcopy(sol2)
    return mejor

def esFactible(sol, datos, k):
    return sol["peso"] + datos["peso"][k] <= datos["M"] and sol["id"][k] == 0

def asignar(sol, datos, i):
    sol["id"][i] += 1
    sol["peso"]+= datos["peso"][i]
    sol["valor"]+= datos["valor"][i]
    return sol

def borrar(sol, datos, i):
    sol["id"][i] -= 1
    sol["peso"]-= datos["peso"][i]
    sol["valor"]-= datos["valor"][i]
    return sol

def esSolucion(sol,datos):
    return sol["peso"] + min(datos["peso"]) > datos["M"]

def inicializarSol():
    sol = {}
    sol["id"] = [0] * N
    sol["valor"] = 0
    sol["peso"] = 0
    return sol

if __name__ == "__main__":
    N, M = list(map(int,input().strip().split()))
    datos = {}
    datos["N"] = N
    datos["M"] = M
    datos["id"] = list()
    datos["valor"] = list()
    datos["peso"] = list()
    for i in range(N):
        E, V, P = list(map(int,input().strip().split()))
        datos["id"].append(E)
        datos["valor"].append(V)
        datos["peso"].append(P)

    sol = inicializarSol()
    mejorSol = inicializarSol()

    mejorSol = mochilaBT(datos, sol, mejorSol, 0)
    print(mejorSol)