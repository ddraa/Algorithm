from _collections import deque

def bfs(x, y, c):
    queue = deque()
    queue.append([x, y])
    while queue:
        ax, ay = queue.popleft()
        c += 1
        for k in range(4):
            xx = ax + opx[k]
            yy = ay + opy[k]
            if 0 <= xx <= N-1 and 0 <= yy <= N-1:
                if matrix[xx][yy] == 1: # not use visited[]..
                    matrix[xx][yy] = 0
                    queue.append([xx, yy])
    return c


N = int(input())
matrix, length = [], []

for _ in range(N):
    matrix.append(list(map(int, list(input()))))

opx = [-1,1,0,0]
opy = [0,0,-1,1]

for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            matrix[i][j] = 0
            length.append(bfs(i, j, 0))

print(len(length))
length.sort()
for l in length:
    print(l)