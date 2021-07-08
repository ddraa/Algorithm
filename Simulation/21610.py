import sys
from collections import deque

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]


def create_cloud():
    ncloud = deque()
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and not cl[i][j]:
                ncloud.append((i, j))
                board[i][j] -= 2
    return ncloud


def cross(x, y):
    c = 0
    for k in range(2, 9, 2):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] > 0:
                c += 1
    return c


def biba(move):
    global cloud
    d, s = move[0], move[1]
    for _ in range(len(cloud)):
        x, y = cloud.popleft()
        cloud.append(((x + dx[d] * s) % N, (y + dy[d] * s) % N))

    for x, y in cloud:
        board[x][y] += 1
        cl[x][y] = True

    for x, y in cloud:
        board[x][y] += cross(x, y)

    cloud = create_cloud()


N, M = map(int, sys.stdin.readline().split())
board = []
cloud = deque([(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)])

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for _ in range(M):
    op = list(map(int, sys.stdin.readline().split()))
    cl = [[False for _ in range(N)] for _ in range(N)]
    biba(op)

res = 0
for line in board:
    res += sum(line)
print(res)
