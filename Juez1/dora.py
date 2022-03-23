empleados = input().split()
d = {}
for i in range(0, 10):
    d[i] = int(0)
for id in empleados:
    if id != "-1":
        d[int(id)] = d[int(id)]+1
    else:
        for clave in d:
            if d[clave] >= 3:
                print(clave, " ", end="")

