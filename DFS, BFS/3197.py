import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check():
    while swan:
        x, y = swan.popleft()
        if x == ex and y == ey:
            return True

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and not svisited[nx][ny]:
                svisited[nx][ny] = True
                if board[nx][ny] == '.':
                    swan.append((nx, ny))
                else: # Next pos
                    N_swan.append((nx, ny))

    return False

def melting():
    while water:
        x, y = water.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and not wvisited[nx][ny]:
                wvisited[nx][ny] = True
                if board[nx][ny] == '.':
                    water.append((nx, ny))
                else: # Next pos
                    N_water.append((nx, ny))

    for nw in N_water:
        board[nw[0]][nw[1]] = '.' # melting


r, c = map(int, sys.stdin.readline().split())
board, dest = [], []
swan, water = deque(), deque()
svisited = [[False for _ in range(c)] for _ in range(r)]
wvisited = [[False for _ in range(c)] for _ in range(r)]

for _ in range(r):
    board.append(list(sys.stdin.readline().rstrip()))

for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            dest.append((i, j))
            board[i][j] = '.'
            water.append((i, j))

        elif board[i][j] == '.':
            water.append((i, j))
            wvisited[i][j] = True
ans = 0

sx, sy = dest[0][0], dest[0][1]
ex, ey = dest[1][0], dest[1][1]

swan.append((sx, sy)) # start
svisited[sx][sy] = True


while True:
    N_swan = deque()
    N_water = deque()
    if check():
        break

    ans += 1
    melting()

    swan = N_swan
    water = N_water
print(ans)