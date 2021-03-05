import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[False for _ in range(N)] for _ in range(N)] # init
    visited[0][0] = True
    queue = deque()
    queue.append([x, y])
    turn = False
    while queue:
        x, y = queue.popleft()
        for lx, ly in light[x][y]:
            if not lighted[lx][ly]:
                lighted[lx][ly] = True
                turn = True

        for k in range(4):
            tx, ty = x + dx[k], y + dy[k]
            if 0 <= tx < N and 0 <= ty < N and not visited[tx][ty] and lighted[tx][ty]:
                visited[tx][ty] = True
                queue.append([tx, ty])
    return turn

N, M = map(int, sys.stdin.readline().split())
light = [[list() for _ in range(N)] for _ in range(N)]
lighted = [[False for _ in range(N)] for _ in range(N)]
lighted[0][0] = True

for _ in range(M):
    i, j, toi, toj = map(int, sys.stdin.readline().split())
    light[i - 1][j - 1].append([toi - 1, toj - 1])

while True:
    if not bfs(0, 0):
        break

ans = 0
for v in lighted:
    ans += v.count(True)
print(ans)
