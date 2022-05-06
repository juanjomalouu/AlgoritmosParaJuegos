
def algoritmoVoraz(info):
    listaTiempos = list()
    sumaSolucion = 0
    for i in range(len(info)):
        if i == 0:
            listaTiempos.append(info[i][1])
        else:
            listaTiempos.append(info[i][1] + listaTiempos[i-1])
        sumaSolucion+=listaTiempos[-1]
    return  sumaSolucion



if __name__ == "__main__":
    N = int(input())
    info = list()
    for i in range(N):
        info.append(list(map(int,input().strip().split())))

    info.sort(key=lambda x:x[1])
    print(algoritmoVoraz(info))