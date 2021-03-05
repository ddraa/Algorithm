import sys
from collections import deque
from itertools import combinations, product

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    temp = [[x, y]]
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            tx, ty = x + dx[k], y + dy[k]
            if 0 <= tx < N and 0 <= ty < N and not visited[tx][ty] and board[tx][ty] == 1:
                visited[tx][ty] = True
                queue.append([tx,ty])
                temp.append([tx, ty])
    return temp

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
MIN = 10 ** 5

visited = [[False for _ in range(N)] for _ in range(N)]
MAP = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j] == 1:
            visited[i][j] = True
            MAP.append(bfs(i, j))

for i in combinations(range(len(MAP)), 2):
    a, b = i
    for com in product(MAP[a], MAP[b]):
        x1, y1 = com[0][0], com[0][1]
        x2, y2 = com[1][0], com[1][1]
        dist = abs(x2 - x1) + abs(y2 - y1)
        if dist < MIN:
            MIN = dist
print(MIN - 1)