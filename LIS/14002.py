import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = []
for n in arr:
    dp.append([n])
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            if len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [arr[i]]

dp.sort(key=lambda x: len(x))
print(len(dp[-1]))
print(*dp[-1])
