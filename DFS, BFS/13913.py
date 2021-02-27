import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append((n, 0))

    while queue:
        cur, c = queue.popleft()
        if cur == k:
            return c

        for Next in [cur + 1, cur - 1, cur * 2]:
            if 0 <= Next <= 10 ** 5 and not visited[Next]:
                visited[Next] = True
                queue.append((Next, c + 1))
                par[Next] = cur


n, k = map(int, sys.stdin.readline().split())
visited = [False for _ in range(10 ** 5 + 1)]
visited[n] = True
par = {}
m = bfs()
print(m)
li = deque([k])
while k in par:
    li.appendleft(par[k])
    k = par[k]
print(*li)
