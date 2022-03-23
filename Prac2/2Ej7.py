x2= int(input())
y2 = int(input())
def powNums (x, y):
    if y == 0:
        return 1
    else:
        return x * powNums(x,y-1)
print(powNums(x2,y2))