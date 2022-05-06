import copy


def mochilaVA(datos, sol, mejorSol, k):
    if esSolucion(datos, sol):
        if mejorSol["valor"] < sol["valor"]:
            mejorSol = copy.deepcopy(sol)
    else:
        for i in range(k, datos["N"]):
            if esFactible(datos, i, sol):
                sol = asignar(sol, i, datos)
                mejorSol = mochilaVA(datos, sol, mejorSol, i)
                sol = borrar(sol, i, datos)
    return mejorSol

def esSolucion(datos, sol):
    return sol["peso"] + min(datos["peso"]) > datos["M"]

def esFactible(datos,i,sol):
    return sol["peso"] + datos["peso"][i] <= datos["M"]  and sol["id"][i] == 0

def asignar(sol, i, datos):
    sol["id"][i] += 1
    sol["peso"] += datos["peso"][i]
    sol["valor"] += datos["valor"][i]
    return sol

def borrar(sol, i, datos):
    sol["id"][i] -= 1
    sol["peso"] -= datos["peso"][i]
    sol["valor"] -= datos["valor"][i]
    return sol

def inicializarSol(N):
    sol = {}
    sol["id"] = [0] * N
    sol["peso"] = 0
    sol["valor"] = 0
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
        E,V,P = list(map(int,input().strip().split()))
        datos["id"].append(E)
        datos["valor"].append(V)
        datos["peso"].append(P)

    sol = inicializarSol(N)
    mejorSol = inicializarSol(N)

    mejorSol = mochilaVA(datos, sol, mejorSol, 0)
    print(mejorSol["valor"])
