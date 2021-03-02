import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread():
    temp = []
    while fire:
        x, y = fire.pop()
        for k in range(4):
            fx, fy = x + dx[k], y + dy[k]
            if 0 <= fx < h and 0 <= fy < w and board[fx][fy] != '*' and board[fx][fy] != '#':
                temp.append((fx, fy))
                board[fx][fy] = '*'
    return temp


def bfs(x, y):
    global fire

    queue = deque()
    queue.append((x, y, 0))
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[x][y] = True


    while queue:
        fire = spread()
        for _ in range(len(queue)): # level
            x, y, d = queue.popleft()
            if x == 0 or x == h - 1 or y == 0 or y == w - 1:
                return d + 1

            for k in range(4):
                tx, ty = x + dx[k], y + dy[k]
                if 0 <= tx < h and 0 <= ty < w and not visited[tx][ty] and board[tx][ty] == '.':
                    visited[tx][ty] = True
                    queue.append((tx, ty, d + 1))


T = int(sys.stdin.readline())
for _ in range(T):
    board = []
    fire = []
    w, h = map(int, sys.stdin.readline().split())
    for _ in range(h):
        board.append(list(sys.stdin.readline().rstrip()))
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                start = (i, j)
            elif board[i][j] == '*':
                fire.append((i, j))
    ans = bfs(start[0], start[1])
    print(ans) if ans else print("IMPOSSIBLE")