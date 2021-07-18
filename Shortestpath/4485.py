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
        if dist[x][y] < c_dist:
            continue

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                n_dist = c_dist + board[nx][ny]

                if n_dist < dist[nx][ny]:
                    dist[nx][ny] = n_dist
                    heappush(h, (n_dist, nx, ny))

c = 1
while True:
    N = int(input())
    if N == 0:
        break

    board, dist = [], [[float('inf') for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        board.append(list(map(int, input().split())))

    dijkstra(0, 0)
    print(f'Problem {c}: {dist[-1][-1]}')
    c += 1