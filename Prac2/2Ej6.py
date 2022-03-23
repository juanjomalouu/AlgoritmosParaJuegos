start = int(input())
end = int(input())
def naturalNums (ini, fin):
    if fin == ini:
        return str(fin)
    else:
        return str(ini) + " " + naturalNums(ini +1,fin)

print(naturalNums(start,end))