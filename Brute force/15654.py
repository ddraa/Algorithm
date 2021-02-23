import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

coms = permutations(arr, m)
for k in sorted(coms):
    print(*k)