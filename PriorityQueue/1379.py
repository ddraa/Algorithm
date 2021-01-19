import sys
import heapq

c, i = 0, 0
N = int(sys.stdin.readline())
start, origin = [], []
dic = {}
for _ in range(N):
    n, s, e = map(int, sys.stdin.readline().split())
    origin.append([n, s, e])
start = sorted(origin, key=lambda x:x[1])

h, l = [], []
for s in start: # s[0] -> n, s[1] -> start, s[2] -> end
    Flag = False
    if h and h[0][0] <= s[1]:
        Flag = True
        _, i = heapq.heappop(h)

    if not Flag:
        heapq.heappush(h, (s[2], len(h) + 1))
        dic[s[0]] = len(h)
        l.append(len(h))
    else:
        heapq.heappush(h, (s[2], i))
        dic[s[0]] = i
        l.append(i)

    if c < len(h):
        c = len(h)
print(c)
for k in range(1, N+1):
    print(dic[k])
