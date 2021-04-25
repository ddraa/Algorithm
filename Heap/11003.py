import sys
from heapq import *

N, L = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
h = []
removed = []

i = 0
r = i - L
while i < N:
    if r >= 0:
        heappush(removed, arr[r])
    heappush(h, arr[i])

    while removed and removed[0] == h[0]:
        heappop(removed)
        heappop(h)

    print(h[0], end=" ")

    i += 1
    r += 1