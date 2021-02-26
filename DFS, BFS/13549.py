import sys
from collections import deque

def bfs():
    visited = [False for _ in range(10 ** 5 + 1)]
    queue = deque([(n, 0)])
    while queue:
        cur, c = queue.popleft()
        if cur == k:
            return c

        if 0 <= cur * 2 <= 10 ** 5 and not visited[cur * 2]:
            visited[cur * 2] = True
            queue.appendleft((cur * 2, c))
        if cur - 1 >= 0 and not visited[cur - 1]:
            visited[cur - 1] = True
            queue.append((cur - 1, c + 1))
        if cur + 1 <= 10 ** 5 and not visited[cur + 1]:
            visited[cur + 1] = True
            queue.append((cur + 1, c + 1))


n, k = map(int, sys.stdin.readline().split())
print(bfs())