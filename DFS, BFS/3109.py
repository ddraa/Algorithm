import sys
sys.setrecursionlimit(10 ** 6)
dx = [1, 0, -1]
dy = [1, 1, 1]

def dfs(cx, cy):
    stack = [(cx, cy)]
    board[cx][cy] = 'x' # start

    while stack:
        x, y = stack.pop()
        if y == C - 1:
            while stack:
                tx, ty = stack.pop()
                board[tx][ty] = '.' # 담아만 놓고, 방문 처리는 했는데 실제 방문하지 않은거 refresh
            return True

        for k in range(3):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != 'x':
                board[nx][ny] = 'x'
                stack.append((nx, ny))
    return False

R, C = map(int, sys.stdin.readline().split())
board = []

for _ in range(R):
    board.append(list(sys.stdin.readline().rstrip()))
c = 0
visited = [[False for _ in range(C)] for _ in range(R)]
for s in range(R):
    if dfs(s, 0):
        c += 1
print(c)