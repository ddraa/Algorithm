import sys, copy
from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread():
    tboard = copy.deepcopy(board)
    count = 0

    Gq = deque([spot[index] for index in g])
    Rq = deque([spot[index] for index in r])

    for x, y in Gq:
        tboard[x][y] = 0
    for x, y in Rq:
        tboard[x][y] = 0

    while Gq and Rq:
        for _ in range(len(Gq)):
            x, y = Gq.popleft()
            if tboard[x][y] == 'F':
                continue

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < M and tboard[nx][ny] == 1:
                    tboard[nx][ny] = 'G'
                    Gq.append((nx, ny))

        for _ in range(len(Rq)):
            x, y = Rq.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if tboard[nx][ny] == 'G':
                        tboard[nx][ny] = 'F' # flower
                        count += 1
                    elif tboard[nx][ny] == 1:
                        tboard[nx][ny] = 0
                        Rq.append((nx, ny))

        for x, y in Gq:
            if tboard[x][y] == 'G': # expired
                tboard[x][y] = 0

    return count

N, M, G, R = map(int, sys.stdin.readline().split())
board, spot = [], []
MAX = 0

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if board[i][j] == 2:
            spot.append((i, j))
            board[i][j] = 1 # visited

for comb in combinations(range(len(spot)), G + R):
    comb = set(comb)

    for g in combinations(comb, G):
        g = set(g)
        r = comb - g

        MAX = max(MAX, spread())
print(MAX)