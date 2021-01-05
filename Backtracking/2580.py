import sys
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

li = []
for i in range(9):
    for j in range(9):
        if mat[i][j] == 0:
            li.append([i, j])

def check(x, y, num):
    curx, cury = x // 3, y // 3

    for a in range(3):
        for b in range(3):
            if mat[a + 3 * curx][b + 3 * cury] == num:
                return False
    for a in range(9):
        if mat[a][y] == num or mat[x][a] == num:
            return False
    return True

def extract_num(x, y):
    # part check
    nl = set(range(1, 10))
    curx, cury = x//3, y//3
    for a in range(3):
        for b in range(3):
            if mat[a + 3 * curx][b + 3 * cury] in nl:
                nl.remove(mat[a + 3 * curx][b + 3 * cury])

    for a in range(9):
        if mat[a][y] in nl:
            nl.remove(mat[a][y])
        if mat[x][a] in nl:
            nl.remove(mat[x][a])
    return nl

def DFS(d):
    if d == len(li):
        for ma in mat:
            for m in ma:
                print(m, end=" ")
            print()
        exit(0)
    else:
        curx, cury = li[d]
        # extract num list
        num_list = extract_num(curx, cury)
        for num in num_list:
            mat[curx][cury] = num
            DFS(d + 1)
            mat[curx][cury] = 0
DFS(0)
