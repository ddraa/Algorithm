import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

c = 0
for n in range(1, N+1):
    for t in combinations(arr, n):
        if sum(t) == S:
            c += 1
print(c)
