import sys, heapq

h = []
N = int(sys.stdin.readline())
for _ in range(N):
    n = int(sys.stdin.readline())
    if n > 0:
        heapq.heappush(h, n)
    else:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)