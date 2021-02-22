import sys
from collections import deque

h_y = [-2, -1, 1, 2, 2, 1, -1, -2]
h_x = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    global k
    visited = [[[False for _ in range(w)] for _ in range(h)] for _ in range(k + 1)] # visited[k][x][y]
    queue = deque()
    queue.append((0, 0, 0, 0)) # init

    while queue:
        x, y, m, km = queue.popleft()
        if x == h - 1 and y == w - 1:
            return m

        if k - km > 0:
            for i in range(8):
                hx, hy = h_x[i] + x, h_y[i] + y
                if 0 <= hx < h and 0 <= hy < w:
                    if board[hx][hy] == 0 and not visited[km + 1][hx][hy]:
                        visited[km + 1][hx][hy] = True
                        queue.append((hx, hy, m + 1, km + 1))

        for i in range(4):
            hx, hy = dx[i] + x, dy[i] + y
            if 0 <= hx < h and 0 <= hy < w:
                if board[hx][hy] == 0 and not visited[km][hx][hy]:
                    visited[km][hx][hy] = True
                    queue.append((hx, hy, m + 1, km))


k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
board = []
for _ in range(h):
    board.append(list(map(int, sys.stdin.readline().split())))

ans = bfs()
print(ans) if type(ans) == int else print(-1)