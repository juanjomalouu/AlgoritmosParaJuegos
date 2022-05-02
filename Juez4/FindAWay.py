def readLabyrinth():
    n = int(input().strip())
    lab = []
    steps = 0
    for i in range(n):
        lab.append([0] * n)
        line = input().strip().split()
        for j in range(n):
            lab[i][j] = int(line[j])
            if lab[i][j] == 0:
                steps += 1
    return lab, steps


def isFeasible(lab, r, c):
    return 0 <= r < len(lab) and 0 <= c < len(lab) and lab[r][c]==0


def solve(lab, r, c, k, steps):
    if k == steps+1 and r == len(lab)-1 and c == len(lab)-1:
        isSol = True
    else:
        isSol = False
        mov = [[1,0], [0,1], [-1,0], [0,-1]]
        i = 0
        while not isSol and i < len(mov):
            if isFeasible(lab, r + mov[i][0], c + mov[i][1]):
                lab[r + mov[i][0]][c + mov[i][1]] = k
                [lab, isSol] = solve(lab, r + mov[i][0], c + mov[i][1], k+1, steps)
                if not isSol:
                    lab[r + mov[i][0]][c + mov[i][1]] = 0
            i += 1
        return [lab, isSol]


lab, steps = readLabyrinth()
print(lab)
paso = 1
lab[0][0] = 1
[lab, isSol] = solve(lab, 0, 0, paso+1, steps)
print("SI") if isSol else print("NO")

