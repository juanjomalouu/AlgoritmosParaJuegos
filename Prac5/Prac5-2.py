import copy


def inicializarDatos():
    datos = {'N':5, 'W':100, 'id': list(range(5)),'wi':[10,20,30,40,50], 'vi':[20,30,66,40,60]}
    return datos

def calcularVW(datos):
    datos['vi/wi']=[]
    for i in range(len(datos['wi'])):
        datos['vi/wi'].append(datos['vi'][i]/datos['wi'][i])
    return datos

def inicializarSol(datos):
    sol={'objetos':[], 'valor':0, 'capacidad':datos['W']}
    return sol

def esSolucion(sol):
    return sol['capacidad'] == 0

def esVacio(candidatos):
    return candidatos('N')

def seleccionar(datos):
    indMayor=0
    for i in range(1, datos['N']):
        if datos['vi/wi'][i]>datos['vi/wi'][indMayor]:
            indMayor = i
    seleccionado = {'id':datos['id'][indMayor],
                    'vi': datos['vi'][indMayor],
                    'mi': datos['mi'][indMayor]}
    del datos['id'][indMayor]
    del datos['vi'][indMayor]
    del datos['mi'][indMayor]
    del datos['vi/mi'][indMayor]
    datos['N'] -=1
    return seleccionado, datos

def anyadir(sol, seleccionado):
    if seleccionado['wi'] <= sol['capacidad']:
        sol['objetos'][seleccionado['id']] = 1
        sol['capacidad'] -= seleccionado['wi']
        sol['valor'] += seleccionado['vi']
    else:
        sol['objetos'][seleccionado['id']] = sol['capacidad']/seleccionado['wi']
        sol['capacidad'] = 0
        sol['valor'] += seleccionado['vi'] * sol['objetos'][seleccionado['id']]


def mochilaVoraz(candidatos):
    sol = inicializarSol(candidatos)
    while not esSolucion(sol) and not esVacio(candidatos):
        seleccionado, candidatos = seleccionar(candidatos)
        sol = anyadir(sol, seleccionado)
    return sol




datos = inicializarDatos()
datos = calcularVW(datos)
sol = mochilaVoraz(copy.deepcopy(datos))
