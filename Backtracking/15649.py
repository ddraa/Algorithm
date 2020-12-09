import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

c = permutations(range(1, N + 1), M)
for i in c:
    for j in i:
        print(j, end = " ")
    print("")
        