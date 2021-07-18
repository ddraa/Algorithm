import sys
sys.setrecursionlimit(10 ** 6)

def dfs(li, c):
    if c == M:
        print(*li)
        return

    for num in Used:
        if li[-1] <= num:
            dfs(li + [num], c + 1)


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
Used = {}

for digit in arr:
    if digit in Used:
        Used[digit] += 1
    else:
        Used[digit] = 1
for n in Used:
    dfs([n], 1)

# import sys
# from itertools import combinations
# N, M = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
#
# arr.sort()
# for c in combinations(arr, M):
#     if sorted(c) == list(c):
#         print(*c)
