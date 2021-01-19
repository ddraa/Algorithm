import sys
from queue import PriorityQueue

c = 0
N = int(sys.stdin.readline())
start = []
for _ in range(N):
    n, s, e = map(int, sys.stdin.readline().split())
    start.append([s, e])
start = sorted(start, key=lambda x:x[0])

queue = PriorityQueue()
for s in start: # s[0] -> start, s[1] -> end
    if not queue.empty():
        t = queue.get()
        if t > s[0]:
            queue.put(t)
    queue.put(s[1])
    if c < queue.qsize():
        c = queue.qsize()
print(c)

