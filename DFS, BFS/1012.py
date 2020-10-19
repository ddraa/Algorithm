import sys

T = int(sys.stdin.readline())
opx = [1,-1,0,0]
opy = [0,0,-1,1]
def dfs(x, y):
    stack = [[x,y]]

    while stack:
        ax, ay = stack.pop()
        if not visited[ax][ay]:
            visited[ax][ay] = 1
            for t in range(4):
                x = ax + opx[t]
                y = ay + opy[t]
                if 0<=x<=n-1 and 0<=y<=m-1:
                    if matrix[x][y] == 1:
                        stack.append([x,y])
for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())

    matrix = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    c = 0
    for __ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        matrix[b][a] = 1 # bc
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                c += 1
                dfs(i,j)
    print(c)

