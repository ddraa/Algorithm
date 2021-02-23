import sys

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
dp = [[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
    for j in range(3):
        dp[i][j] = board[i][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])
print(min(dp[N - 1]))