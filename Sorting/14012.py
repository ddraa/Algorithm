import sys
from heapq import *

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
h = []

for i, j in zip(a, b):
    heappush(h, (i, j))

while h:
    m = heappop(h)
    if m[0] > M:
        break
    else:
        profit = m[1] - m[0]
        if profit > 0:
            M += profit
print(M)