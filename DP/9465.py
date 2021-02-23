import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    board = []
    for _ in range(2):
        board.append(list(map(int, sys.stdin.readline().split())))

    dp = [[0 for _ in range(n)] for _ in range(2)]

    for i in range(n):
        dp[0][i] = board[0][i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = board[1][i] + max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][n - 1], dp[1][n - 1]))