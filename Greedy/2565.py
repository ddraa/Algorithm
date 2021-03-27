import sys

N = int(sys.stdin.readline())
line = []
for _ in range(N):
    line.append(list(map(int, sys.stdin.readline().split())))

line.sort()
B = [k[1] for k in line]

dp = [1 for i in range(N)]

for i in range(N): # LIS, 단조증가
    for j in range(i):
        if B[i] > B[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))