
def mochilaBT(data, sol, mejorSol, k):
    if esSolucion(sol, data):
        if mejorSol['valor'] < sol['valor']:
            mejorSol['valor'] = sol['valor']
    else:
        for i in range(k, data['N']):
            if esFactible(sol, data, i):
                sol = asignar(sol, i, data)
                mejorSol = mochilaBT(data, sol, mejorSol, i)
                sol = borrar(sol, i, data)
    return  mejorSol

def esFactible(sol, data, i):
    return data["peso"][i] + sol["peso"] <= data["M"] and sol["id"][i] == 0

def esSolucion(sol, data):
    return sol["peso"] + min(data["peso"]) > data["M"]

def asignar(solucion, i, datos):
    solucion["id"][i] += 1
    solucion["valor"] += datos["valor"][i]
    solucion["peso"] += datos["peso"][i]
    return solucion

def borrar(solucion, i, datos):
    solucion["id"][i] -= 1
    solucion["valor"] -= datos["valor"][i]
    solucion["peso"] -= datos["peso"][i]
    return solucion

if __name__ == "__main__":
    data = {}
    N, M = list(map(int,input().strip().split()))
    data["N"] = N
    data["M"] = M
    data["id"] = list()
    data["valor"] = list()
    data["peso"] = list()
    for i in range(N):
        E,V,P = list(map(int,input().strip().split()))
        data["id"].append(E)
        data["valor"].append(V)
        data["peso"].append(P)

    sol = {}
    sol["id"] = [0] * N
    sol["valor"] = 0
    sol["peso"] = 0

    mejorSol = {}
    mejorSol["id"] = [0] * N
    mejorSol["valor"] = 0
    mejorSol["peso"] = 0

    mejorSol = mochilaBT(data, sol, mejorSol, 0)
    print(mejorSol["valor"])