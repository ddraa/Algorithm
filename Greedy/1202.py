import heapq
import sys
ru = []

re = 0
i = 0

N, K = map(int, sys.stdin.readline().split())
ruby = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bag = [int(sys.stdin.readline()) for _ in range(K)]
ruby.sort()
bag.sort()

for b in bag:
    while i < N and b >= ruby[i][0]:
        heapq.heappush(ru, -ruby[i][1])
        i += 1
    if ru:
        re += heapq.heappop(ru)
print(-re)
