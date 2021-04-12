import sys
# 0-1 knapsack, 분할가능 배낭문제
# N, limit = map(int, sys.stdin.readline().split())
# bag = []
# for _ in range(N):
#     bag.append(list(map(int, sys.stdin.readline().split())))
# bag.sort(key=lambda x: x[1] / x[0])
#
# MAX = 0
# weight, value = 0, 0
# while bag:
#     w, v = bag.pop()
#     weight += w
#
#     if weight <= limit:
#         value += v
#         if value > MAX:
#             MAX = value
#     else: # clear
#         weight, value = 0, 0
# print(MAX)

N, K = map(int, sys.stdin.readline().split())
bag = []
for _ in range(N):
    bag.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = bag[i - 1]
    for j in range(1, K + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[-1][-1])
