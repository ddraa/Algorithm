import sys, copy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, check):
    dq = deque()
    dq.append((i, j))
    nodes = [(i, j)]
    zc = 0

    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and (board[nx][ny] == check or board[nx][ny] == 0):
                    visited[nx][ny] = True
                    dq.append((nx, ny))
                    nodes.append((nx, ny))

                    if board[nx][ny] == 0:
                        zc += 1

    if len(nodes) >= 2:
        nodes.sort(key=lambda v: (v[0], v[1]))
        for x, y in nodes:
            if board[x][y] != 0:
                sx, sy = x, y
                break
        nodes.append((sx, sy, zc))
        return nodes
    else:
        return None


def Autoplay():
    global board
    groups = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] != 0 and board[i][j] != -1 and board[i][j] is not None:
                check = board[i][j]
                visited[i][j] = True
                for x, y in rain:
                    visited[x][y] = False  # refresh

                group = bfs(i, j, check)

                if group:
                    groups.append(group)

    if not groups:
        return 0

    groups.sort(key=lambda v: (len(v), v[-1][2], v[-1][0], v[-1][1]))

    deleted = groups.pop()
    deleted.pop()
    score = len(deleted) ** 2

    while deleted:
        x, y = deleted.pop()
        board[x][y] = None

    gravity()
    rotate()
    gravity()

    return score


def gravity():
    for i in range(N - 1, -1, -1):
        for j in range(N):
            if board[i][j] is None:
                h = i
                while h >= 0:
                    if board[h][j] == -1:
                        break
                    elif board[h][j] is not None:
                        board[i][j] = board[h][j]
                        board[h][j] = None
                        break
                    h -= 1


def rotate():
    temp = copy.deepcopy(board) # origin

    for i in range(N):
        for j in range(N):
            board[N - j - 1][i] = temp[i][j] # rotated


N, M = map(int, sys.stdin.readline().split())
board = []
rain = deque()
ans, sc = 0, 0
for a in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    rain = []
    for a in range(N):
        for b in range(N):
            if board[a][b] == 0:
                rain.append((a, b))
    res = Autoplay()

    if res:
        sc += res
    else:
        break
print(sc)
