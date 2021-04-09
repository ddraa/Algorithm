import sys, bisect

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
position = [N] + [0] * N
dp = [0] + [1] * N

for index in range(N):
    position[arr[index]] = index

MAX = 0
for number in arr:
    if position[number] > position[number - 1]:
        dp[number] = dp[number - 1] + 1
        MAX = max(dp[number], MAX)
#print(N - MAX)
print(dp)