import sys
import heapq

N = int(sys.stdin.readline())
h = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
          heapq.heappush(h, (abs(x), x))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)