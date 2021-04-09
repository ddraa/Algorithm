import sys

N = int(sys.stdin.readline())
dp = [0, 1, 2, 3]

for i in range(4, N + 1):
    dp.append(dp[i-1] + dp[i-2])
print(dp[N] % 10007)