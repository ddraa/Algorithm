# 상범 빌딩

import sys
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [0, 0, 1, -1, 0, 0]


def bfs(x, y, z, d):
    queue = deque([(x, y, z, d)])
    visited[x][y][z] = True

    while queue:
        x, y, z, d = queue.popleft()
        if x == ex and y == ey and z == ez:
            return d

        for k in range(6):
            tx = x + dx[k]
            ty = y + dy[k]
            tz = z + dz[k]

            if 0 <= tx < l and 0 <= ty < r and 0 <= tz < c and (board[tx][ty][tz] == '.' or board[tx][ty][tz] == 'E'): # E 지점 체크 주의
                if not visited[tx][ty][tz]:
                    visited[tx][ty][tz] = True
                    queue.append((tx, ty, tz, d + 1))

while True:
    l, r, c = map(int, sys.stdin.readline().split())
    if l == 0 and r == 0 and c == 0:
        break
    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]
    board = []
    for _ in range(l):
        board.append([list(sys.stdin.readline().rstrip()) for _ in range(r)])
        input()

    for tl in range(l):
        for tr in range(r):
            for tc in range(c):
                if board[tl][tr][tc] == 'S':
                    sx, sy, sz = tl, tr, tc
                elif board[tl][tr][tc] == 'E':
                    ex, ey, ez = tl, tr, tc

    ans = bfs(sx, sy, sz, 0)
    print(f'Escaped in {ans} minute(s).') if ans else print("Trapped!")