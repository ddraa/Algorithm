import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
matrix = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(N):
    matrix.append(list(sys.stdin.readline().strip()))
visited = [[0]*N for _ in range(N)]
def dfs(x, y):
    for k in range(4):
        kx = x + dx[k]
        ky = y + dy[k]
        if 0<=kx<N and 0<=ky<N and not visited[kx][ky]:
            if matrix[kx][ky] == matrix[x][y]:
                visited[kx][ky] = 1
                dfs(kx,ky)


def dfs_RG(x, y):
    for k in range(4):
        kx = x + dx[k]
        ky = y + dy[k]
        if 0<=kx<N and 0<=ky<N and not visited[kx][ky]:
            if matrix[x][y] == 'R' or matrix[x][y] == 'G':
                if matrix[kx][ky] == 'R' or matrix[kx][ky] == 'G':
                    visited[kx][ky] = 1
                    dfs_RG(kx,ky)
            else:
                if matrix[kx][ky] == matrix[x][y]:
                    visited[kx][ky] = 1
                    dfs_RG(kx,ky)

count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            visited[i][j] = 1
            dfs(i, j)
print(count, end=" ")

visited = [[0]*N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            visited[i][j] = 1
            dfs_RG(i, j)
print(count)