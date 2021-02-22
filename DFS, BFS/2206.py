import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0, 1, 0))
    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]

    while queue:
        x, y, c, crushed = queue.popleft()
        if x == n - 1 and y == m - 1:
            return c
        for k in range(4):
            tx, ty = dx[k] + x, dy[k] + y
            if 0 <= tx < n and 0 <= ty < m:
                if crushed < 1:
                    visited[crushed + 1][tx][ty] = True
                    queue.append((tx, ty, c + 1, crushed + 1))

                if board[tx][ty] == 0 and not visited[crushed][tx][ty]:
                    visited[crushed][tx][ty] = True
                    queue.append((tx, ty, c + 1, crushed))


n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip())))
ans = bfs()
print(ans) if ans else print(-1)