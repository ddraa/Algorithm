import sys
from heapq import *
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(x, y):
    h = []
    dist[x][y] = board[x][y]
    heappush(h, (dist[x][y], x, y))

    while h:
        c_dist, x, y = heappop(h)
        if c_dist > dist[x][y]:
            continue

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                n_dist = c_dist + board[nx][ny]
                if n_dist < dist[nx][ny]:
                    dist[nx][ny] = n_dist
                    heappush(h, (n_dist, nx, ny))

N = int(input())
board, dist = [], [[float('inf') for _ in range(N)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().strip())))


for i in range(N):
    for j in range(N):
        if board[i][j]:
            board[i][j] = 0
        else:
            board[i][j] = 1

dijkstra(0, 0)

print(dist[-1][-1])