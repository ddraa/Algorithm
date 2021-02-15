import sys
from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = []
def bfs(x, y):
    queue = deque([[x, y]])
    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1

        for k in range(4):
            tx, ty = x + dx[k], y + dy[k]
            if 0 <= tx <= n - 1 and 0 <= ty <= m - 1 and board[tx][ty] == 1:
                if not visited[tx][ty]:
                    visited[tx][ty] = True
                    queue.append([tx, ty])

    ans.append(count)

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
c = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == 1:
            c += 1
            visited[i][j] = True
            bfs(i, j)
print(c)
print(max(ans)) if ans else print(0)
