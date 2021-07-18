import sys
input = sys.stdin.readline


def dfs(n):
    global c
    for i in range(n, N * M):
        x, y = i // M, i % M
        if board[x - 1][y - 1] == True and board[x - 1][y] == True and board[x][y - 1] == True:
            continue
        else:
            c += 1
            board[x][y] = True
            dfs(i + 1)
            board[x][y] = False

N, M = map(int, input().split())
board = [[False for _ in range(M)] for _ in range(N)]
c = 1
dfs(0)
print(c)