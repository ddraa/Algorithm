import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
MAX = float('-inf')
dp = [arr[0]] + [0] * (N - 1)
s = 0
for i in range(1, N):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])
print(max(dp))