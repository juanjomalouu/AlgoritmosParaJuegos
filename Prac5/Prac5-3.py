
def inicializar():
    sol = {'Mayores':[],'Menores' :[],'Valor' :0}
    return sol

def seleccionar(candidatos):
    indMayor = 0
    for i in range(1, len(candidatos)):
        if candidatos[i]>candidatos[indMayor]:
            indMayor = i
    seleccionado = candidatos[indMayor]
    del candidatos[indMayor]
    return seleccionado, candidatos

def anyadir(sol,seleccionado):
    sol['Mayores'].append(seleccionado)
    return sol

def anyadirRestantes(sol,candidatos):
    sol['Menores'] = candidatos
    return sol

def calcularValor(sol):
    valor = 0
    for elem in sol['Mayores']:
        valor+=elem
    for elem in sol['Menores']:
        valor-=elem
    sol['Valor']=valor
    return sol



def difSumasMax(arr,K):
    sol = inicializar()
    NIter = max(K, len(arr)-K)

    for i in range(NIter):
        seleccionado,candidatos = seleccionar(arr)
        sol = anyadir(sol, seleccionado)
    sol = anyadirRestantes(sol,candidatos)
    sol = calcularValor(sol)
    return sol


array = [9,4,5,2,10]
K = 2
sol = difSumasMax(array[:], K)
print("La solucion es: ", sol)