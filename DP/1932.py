import sys

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = []
for k in range(N):
    dp.append([0 for _ in range(k + 1)])

for d in range(N):
    for i in range(len(board[d])):
        if i == 0:
            dp[d][i] = dp[d-1][i] + board[d][i]
        elif i == len(board[d]) - 1:
            dp[d][i] = dp[d-1][i-1] + board[d][i]
        else:
            dp[d][i] = max(dp[d-1][i-1], dp[d-1][i]) + board[d][i]

print(max(dp[N - 1]))