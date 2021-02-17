import sys
from collections import deque


def bfs(start, c):
    visited = [False for _ in range(f + 1)]
    visited[start], visited[0] = True, True

    queue = deque([(start, c)])

    while queue:
        cur, c = queue.popleft()
        if cur == g:
            return c
        for k in range(2):
            next_ = cur + op[k]
            if 1 <= next_ <= f and not visited[next_]:
                visited[next_] = True
                queue.append((next_, c + 1))
    return f'use the stairs'

f, s, g, u, d = map(int, sys.stdin.readline().split())
op = [u, -d]
print(bfs(s, 0))