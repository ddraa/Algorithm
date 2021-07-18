# 13711
import sys

N = int(sys.stdin.readline())
a = "".join(sys.stdin.readline().split())
b = "".join(sys.stdin.readline().split())

dp = [[0] * len(b) for _ in range(len(a))]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = dp[i - 1][j] if dp[i - 1][j] > dp[i][j - 1] else dp[i][j - 1]

print(dp[len(a) - 1][len(b) - 1])
