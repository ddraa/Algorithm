N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = 1

for i ,v in enumerate(arr):
    m = float('-inf') # max
    up = 0
    for j in range(i):
        if v > arr[j]:
            if m < dp[j]:
                m = dp[j] # sch max dp idx
                up = dp[j]
    dp[i] = up + 1

print(max(dp))