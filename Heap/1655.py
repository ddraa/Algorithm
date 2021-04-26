import sys
from heapq import *

N = int(sys.stdin.readline())
min_h, max_h = [] ,[]
for _ in range(N):
    n = int(sys.stdin.readline())

    if len(max_h) == len(min_h):
        heappush(max_h, -n)
    else:
        heappush(min_h, n)
    if min_h and min_h[0] < -max_h[0]:
        heappush(min_h, -heappop(max_h))
        heappush(max_h, -heappop(min_h))

    print(-max_h[0])