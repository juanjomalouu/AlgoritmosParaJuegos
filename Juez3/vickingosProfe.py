
def solve(series, t, series_aux):
    tiempo = 0
    puntuacion = 0
    playlist = []

    while tiempo < t:
        act_serie = series.pop(0)
        playlist.append(act_serie)
        if tiempo + act_serie[3] <= t:
            tiempo += act_serie[3]
            puntuacion += act_serie[2]
        else:
            tiempo_proporcional = t-tiempo
            puntuacion += act_serie[2] * tiempo_proporcional/act_serie[3]
            tiempo += act_serie[3]
    for s in series_aux:
        if s in playlist:
            print(s[1])
    print(int(puntuacion))




n,t = map(int, input().strip().split(" "))
series = []

for _ in range(n):
    nombre, puntuacion, tiempo = input().strip().split()
    puntuacion = int(puntuacion)
    tiempo = int(tiempo)
    series.append((tiempo/puntuacion,nombre,puntuacion,tiempo))

series_aux = sorted(series)
solve(series_aux,t,series)