import sys
sys.setrecursionlimit(10**6)


dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,-1,1,1,-1]

def dfs(x, y):
    stack = [[x,y]]
    while stack:
        x, y = stack.pop()
        for k in range(8):
            ax = x + dx[k]
            ay = y + dy[k]
            if 0<=ax<=M-1 and 0<=ay<=N-1 and matrix[ax][ay] == 1:
                if not visited[ax][ay]:
                    visited[ax][ay] = 1
                    stack.append([ax,ay])

while True:
    N, M = map(int, input().split())
    count = 0
    if N==0 and M==0:
        break
    matrix = []
    visited = [[0]*N for _ in range(M)]
    for _ in range(M):
        matrix.append(list(map(int, input().split())))
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                count += 1
                dfs(i, j)
    print(count)