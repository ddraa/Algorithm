from heapq import *
import sys

h = []
N = int(sys.stdin.readline())
for _ in range(N):
    heappush(h, int(sys.stdin.readline()))

ans = 0
while h:
    a = heappop(h)
    if not h:
        break
    b = heappop(h)
    ans += a + b
    if not h:
        break
    heappush(h, a + b)
print(ans)