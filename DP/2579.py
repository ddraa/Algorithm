import sys

N = int(sys.stdin.readline())
stair, dp = [0], [0] * (N + 1)

for _ in range(N):
    stair.append(int(sys.stdin.readline()))

dp[1] = stair[1]

for l in range(2, N + 1):
    if l == 2:
        dp[l] = stair[1] + stair[2]
    else:
        dp[l] = max(stair[l] + dp[l - 2], stair[l] + stair[l - 1] + dp[l - 3])
print(dp[N])