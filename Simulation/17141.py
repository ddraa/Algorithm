import sys, copy
from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global board
    MIN = N * N
    for com in coms:
        dq = deque()
        visited = [[False for _ in range(N)] for _ in range(N)]
        board = copy.deepcopy(origin)
        for x, y in com:
            dq.append((x, y))
            visited[x][y] = True
            board[x][y] = 0  # start

        time = 1
        ttime = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                x, y = dq.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == -1:
                        visited[nx][ny] = True
                        dq.append((nx, ny))
                        board[nx][ny] = time
                        ttime = time
            time += 1

        c = 0
        for line in board:
            c += line.count(-1)
        if c == 0:
            MIN = min(MIN, ttime)

    return MIN if MIN != N * N else -1


N, M = map(int, sys.stdin.readline().split())
board, virus = [], []

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if board[i][j] == 1:
            board[i][j] = '.'
        elif board[i][j] == 2:
            virus.append((i, j))
            board[i][j] = -1
        else:
            board[i][j] = -1

origin = copy.deepcopy(board)
coms = combinations(virus, M)
print(bfs())
