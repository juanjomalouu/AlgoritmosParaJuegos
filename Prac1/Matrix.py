paridad = input()
size = int(input())
start = 2
if paridad == "I":
    start = 1

for i in range(0, size):
    for j in range(0,size):
        print(start,"",end="")
        start+=2
    print("")
