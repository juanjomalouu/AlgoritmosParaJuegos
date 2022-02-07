ml =int(input())
habitantes = int(input())

nInyecciones = 2000/int(ml)
habitantes=habitantes*1000000

total = int(habitantes/nInyecciones+0.5)
print(total)