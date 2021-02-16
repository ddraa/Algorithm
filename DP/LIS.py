import sys
N = int(sys.stdin.readline())
child = [int(sys.stdin.readline()) for _ in range(N)]
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if child[i] > child[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))