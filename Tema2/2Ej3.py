number = int(input())
def sumaParImparRec (n):
    if n/10 == 0:
        return n%10
    elif (n%10) %2 == 0:
        return (n%10) + sumaParImparRec(int(n/10))
    else:
        return -(n%10) + sumaParImparRec(int(n/10))


print(sumaParImparRec(number))