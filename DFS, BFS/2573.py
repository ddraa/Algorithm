import sys
from collections import deque

def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy))

    while queue:
        ax, ay = queue.popleft()
        for l in range(4):
            bx, by = ax + dx[l], ay + dy[l]
            if 0 <= bx < N and 0 <= by < M and board[bx][by] and not visited[bx][by]:
                visited[bx][by] = True
                queue.append((bx, by))

N, M = map(int, sys.stdin.readline().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
ice = []

for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            ice.append((i, j, board[i][j]))

ans = 0
while True:
    ans += 1
    Next = []
    visited = [[False for _ in range(M)] for _ in range(N)]

    while ice:
        x, y, h = ice.pop()
        ic = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not board[nx][ny]:
                ic += 1

        res = 0 if ic >= h else h - ic
        Next.append((x, y, res))

    search = []
    while Next:
        x, y, h = Next.pop()
        if h != 0:
            search.append((x, y, h))
        board[x][y] = h

    c = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] and not visited[i][j]:
                c += 1
                visited[i][j] = True
                bfs(i, j)
    if c >= 2:
        print(ans)
        break
    ice = search
    if not ice:
        print(0)
        break