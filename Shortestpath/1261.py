import sys
from heapq import *

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(x, y):
    h = []
    dist[x][y] = 0
    heappush(h, (dist[x][y], x, y))

    while h:
        c_dist, x, y = heappop(h)
        if c_dist > dist[x][y]:
            continue

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                n_dist = c_dist + board[nx][ny]
                if n_dist < dist[nx][ny]:
                    dist[nx][ny] = n_dist
                    heappush(h, (n_dist, nx, ny))


M, N = map(int, input().split())
board, dist = [], [[float('inf') for _ in range(M)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().strip())))

dijkstra(0, 0)
print(dist[-1][-1])
