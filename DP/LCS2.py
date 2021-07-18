import sys

a = "0" + sys.stdin.readline().strip()
b = "0" + sys.stdin.readline().strip()

dp = [[str()] * (len(b)) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] += dp[i - 1][j - 1] + a[i]
        else:
            dp[i][j] += dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]

res = dp[len(a) - 1][len(b) - 1]
print(len(res))
