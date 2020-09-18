import sys
sys.setrecursionlimit(10**8)

leftTowardx = [-1,0,1,0]
leftTowardy = [0,1,0,-1]
backTowardx = [1,0,-1,0]
backTowardy = [0,-1,0,1]

def turnLeft(cur_d):
    if cur_d == 0:
        return 3 # west
    elif cur_d == 1:
        return 0 # north
    elif cur_d == 2:
        return 1 # east
    else:
        return 2 # south


def dfs(a, b, cur_d):

    matrix[a][b] = -1  # cleaning

    for k in range(4):
        new_d = turnLeft(cur_d)
        ax = a + leftTowardx[new_d]
        ay = b + leftTowardy[new_d]

        if 0<=ax<=N-1 and 0<=ay<=M-1 and not matrix[ax][ay]:
            dfs(ax, ay, new_d)
        else:
            cur_d = new_d

    bx = a + backTowardx[cur_d]
    by = b + backTowardy[cur_d]
    if 0<=bx<=N-1 and 0<=by<=M-1 and matrix[bx][by] != 1: # not wall
        dfs(bx, by, cur_d)
    else: # exit
        count = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == -1:
                    count += 1
        print(count)
        sys.exit(0)



N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
dfs(r, c, d)
