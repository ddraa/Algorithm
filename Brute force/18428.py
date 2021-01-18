from itertools import combinations

def check():
    for x in range(N):
        for y in range(N):
            if mat[x][y] == 'T':
                tx, ty = x, y
                while x < N and mat[x][y] != 'O':
                    if mat[x][y] == 'S':
                        return False
                    x += 1
                x = tx
                while x >= 0 and mat[x][y] != 'O':
                    if mat[x][y] == 'S':
                        return False
                    x -= 1
                x = tx
                while y >= 0 and mat[x][y] != 'O':
                    if mat[x][y] == 'S':
                        return False
                    y -= 1
                y = ty
                while y < N and mat[x][y] != 'O':
                    if mat[x][y] == 'S':
                        return False
                    y += 1
    return True


O, mat = [], []
N = int(input())
for _ in range(N):
    mat.append(input().split())
for i in range(N):
    for j in range(N):
        if mat[i][j] == 'X':
            O.append([i, j])
for k in combinations(O, 3):
    a, b, c = k # (0, 0), (0, 2), (0, 3)
    mat[a[0]][a[1]] = 'O'
    mat[b[0]][b[1]] = 'O'
    mat[c[0]][c[1]] = 'O'
    if check():
        print("YES")
        break
    mat[a[0]][a[1]] = 'X'
    mat[b[0]][b[1]] = 'X'
    mat[c[0]][c[1]] = 'X'

else:
    print("NO")
