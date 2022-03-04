info = input().split()
longLado = int(info[0])
numCortes3 = int(info[1])
sandia = list()
for _ in range(longLado):
    sandia.append(list(map(int, input().strip().split(" "))))




def getNumSemillas(sandia,numCortes, cortesMax,ini,fin,ini2,fin2):
    if numCortes == cortesMax:
        semillasSandia = 0
        for i in range(ini, fin+1):
            for j in range(ini2, fin2+1):
                semillasSandia += sandia[i][j]
        return semillasSandia
    else:
        mitad = (ini+fin)//2
        mitad2 = (ini2+fin2)//2
        a = getNumSemillas(sandia, numCortes+1, cortesMax, ini, mitad, ini2, mitad2)
        b = getNumSemillas(sandia, numCortes+1, cortesMax, mitad+1, fin, ini2, mitad2)
        c = getNumSemillas(sandia, numCortes+1, cortesMax, ini, mitad, mitad2+1, fin2)
        d = getNumSemillas(sandia, numCortes+1, cortesMax, mitad+1, fin, mitad2+1, fin2)
        return min(a,b,c,d)






print(getNumSemillas(sandia, 0, numCortes3,0,longLado-1,0,longLado-1))

