x2= int(input())
y2 = int(input())
def multNums (x, y):
    if y == 0:
        return 0
    else:
        return x + multNums(x,y-1)

print(multNums(x2,y2))