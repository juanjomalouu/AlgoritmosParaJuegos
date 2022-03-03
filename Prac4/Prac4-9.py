

def sumaMaxDyV (v, ini, fin):
    if ini>fin:
        result = 0
    else:
        if ini == fin:
            result = v[ini]
        else:
            mitad = (ini+fin) //2
            sumaMaxIzq = sumaMaxDyV(v,ini,mitad)
            sumaMaxDer = sumaMaxDyV(v, mitad +1, fin)
            suma=0
            sumaMaxI= 0
            for i in range(mitad, ini-1, -1):
                suma += v[i]
                if suma>sumaMaxI:
                    sumaMaxI=suma
            suma = 0
            sumaMaxD = 0
            for i in range(mitad+1, fin +1):
                suma += v[i]
                if suma> sumaMaxD:
                    sumaMaxD = suma
                maxSumaCentral = sumaMaxI + sumaMaxD
                result = max(sumaMaxIzq, sumaMaxDer, maxSumaCentral)
    return result

v = [-2, 11, -4, 13, -5, -2]
print("El vector es: ", v)

sumaMax = sumaMaxDyV(v, 0, len(v)-1)
print(sumaMax)