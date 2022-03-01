def findLevel(tree, current, search, level):
    if current == search:
        return level
    else:
        for child in tree[current]:
            found = findLevel(tree, child, search, level +1)
            if found:
                return found

if __name__ == '__main__':
    n = int(input().strip())
    tree = []
    for _ in range(n):
        tree.append([])
    for _ in range(n):
        line = input().strip().split()
        v = int(line[0])
        for i in range(1,len(line)):
            tree[v].append(int(line[i]))

    cases = int(input().strip())
    for _ in range(cases):
        node = int(input().strip())
        level = findLevel(tree, 0, node, 1)
        print(str(level))
