

def BusquedaBinaria(A,ini,fin,x):
    mitad = (ini + fin) // 2
    if ini > fin:
        return False
    else:
        if x == A[mitad]:
            return True
        else:
            if x > A[mitad]:
                return BusquedaBinaria(A,mitad+1,fin,x)
            else:
                return BusquedaBinaria(A,ini,mitad-1,x)



numHabitantes = int(input())
idsHabitantes = list(map(int, input().strip().split(" ")))

numAmochados = int(input())
idsAmochados = list(map(int, input().strip().split(" ")))
idsAmochados.sort()
numComprobados = int(input())
idsComprobados = list(map(int, input().strip().split(" ")))

for i in idsComprobados:
    if BusquedaBinaria(idsAmochados,0,numAmochados-1,i) == False:
        print(":)")
    else:
        print(":_(")