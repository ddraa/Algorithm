import sys

a = "0" + sys.stdin.readline().strip()
b = "0" + sys.stdin.readline().strip()
c = "0" + sys.stdin.readline().strip()

dp = [[[str()] * len(c) for _ in range(len(b))] for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        for k in range(1, len(c)):
            if a[i] == b[j] == c[k]:
                dp[i][j][k] += dp[i - 1][j - 1][k - 1] + a[i]
            else:
                an, bn, cn = len(dp[i - 1][j][k]), len(dp[i][j - 1][k]), len(dp[i][j][k - 1])
                res = max(an, bn, cn)
                if res == an:
                    dp[i][j][k] += dp[i - 1][j][k]
                elif res == bn:
                    dp[i][j][k] += dp[i][j - 1][k]
                else:
                    dp[i][j][k] += dp[i][j][k - 1]

res = dp[len(a) - 1][len(b) - 1][len(c) - 1]
print(len(res))
