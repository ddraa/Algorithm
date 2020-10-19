from _collections import deque
import sys
inputs = sys.stdin.readline
opx = [1,-1,0,0]
opy = [0,0,-1,1]

m, n, k = map(int, input().split())
matrix = [[1 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

for i in range(k):
    lx, ly, rx, ry = map(int, inputs().split())

    ax = m-1-ly; ay = lx
    bx = m-ry; by = rx-1
    for x in range(m):
        for y in range(n):
            if bx<=x<=ax and ay<=y<=by:
                matrix[x][y] = 0 # square
state = 0
l = []


def bfs(a, b):
    Num = 0
    queue = deque()
    queue.append([a,b])

    while queue:
        a, b = queue.popleft()
        if not visited[a][b] and matrix[a][b]:
            visited[a][b] = 1
            Num+=1
            for k in range(4):
                tx, ty = a+opx[k], b+opy[k]
                if 0<=tx<m and 0<=ty<n:
                    queue.append([tx, ty])
    l.append(Num)


for i in range(m):
    for j in range(n):
        if not visited[i][j] and matrix[i][j]:
            state += 1
            bfs(i,j)
print(state)
l.sort()
for k in l:
    print(k, end=" ")