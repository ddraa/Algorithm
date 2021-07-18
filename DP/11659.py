import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0] * (N + 1)
s = 0
for i, n in enumerate(arr):
    s += n
    dp[i + 1] = s

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[b] - dp[a - 1])
