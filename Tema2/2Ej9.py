
divisor = int(input())
tope= int(input())
def MultiplosRec (top, div):
    if top < div:
        return ""
    else:
        if top % div == 0:
            return MultiplosRec(top-1, div)+ " " + str(top)
        else:
            return MultiplosRec(top-1,div)

print(MultiplosRec(tope,divisor))