import sys

T = int(sys.stdin.readline())
d = 1000000009
dp = [0, 1, 2, 4] * (10 ** 6 - 2)
for n in range(4, 10 ** 6 + 1):
    dp[n] = (dp[n - 1] % d + dp[n - 2] % d + dp[n - 3] % d) % d

for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])
