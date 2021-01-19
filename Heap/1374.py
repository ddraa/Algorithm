import sys
import heapq

c = 0
N = int(sys.stdin.readline())
start = []
for _ in range(N):
    n, s, e = map(int, sys.stdin.readline().split())
    start.append([s, e])
start = sorted(start, key=lambda x:x[0])

h = []
for s in start: # s[0] -> start, s[1] -> end
    if h and h[0] <= s[0]:
        heapq.heappop(h)
    heapq.heappush(h, s[1])
    if c < len(h):
        c = len(h)
print(c)

