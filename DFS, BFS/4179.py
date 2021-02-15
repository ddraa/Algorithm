import sys, copy
from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = None

def fired():
    t = set()
    for f in fire:
        x, y = f[0], f[1]
        for k in range(4):
            fx, fy = x + dx[k], y + dy[k]
            if 0 <= fx <= r - 1 and 0 <= fy <= c - 1 and board[fx][fy] == '.':
                board[fx][fy] = 'F'
                t.add((fx, fy))
    return t

def bfs(x, y, d):
    global fire
    visited[x][y] = True
    queue = deque([[x, y, d]])
    temp = deque([[x, y, d]]) # init

    while temp:
        fire = fired()
        if not queue: # set
            queue = deque(temp)
        temp = []

        while queue:
            x, y, d = queue.popleft()
            if x == 0 or x == r - 1 or y == 0 or y == c - 1:
                return d + 1

            for k in range(4):
                tx, ty = x + dx[k], y + dy[k]
                if 0 <= tx <= r - 1 and 0 <= ty <= c - 1 and board[tx][ty] == '.':
                    if not visited[tx][ty]:
                        visited[tx][ty] = True
                        temp.append((tx, ty, d + 1))


r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
fire = set()

for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            s = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'F':
            fire.add((i, j))


ans = bfs(s[0], s[1], 0) # start
print(ans) if ans else print("IMPOSSIBLE")