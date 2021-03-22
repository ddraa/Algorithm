# import sys
#
# def dfs(li, c):
#     if c == M:
#         print(*li)
#         return
#
#     for index in range(N):
#         if not Used[index]:
#             if li and li[-1] < arr[index]:
#                 Used[index] = True
#                 dfs(li + [arr[index]], c + 1)
#                 Used[index] = False
#
# N, M = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
# Used = [False for _ in range(N)]
# arr.sort()
#
# for n in arr:
#     dfs([n], 1)

import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
for c in combinations(arr, M):
    if sorted(c) == list(c):
        print(*c)
