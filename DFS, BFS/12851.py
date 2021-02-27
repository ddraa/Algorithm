import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

def bfs():
    global ans
    queue = deque()
    queue.append((n, 0))
    m = 0

    while queue:
        cur, c = queue.popleft()
        if cur == k:
            m = c
            ans += 1

        if cur + 1 <= 10 ** 5 and (not visited[cur + 1] or c + 1 == visited[cur + 1]):
            visited[cur + 1] = c + 1
            queue.append((cur + 1, c + 1))

        if 0 <= cur - 1 and (not visited[cur - 1] or c + 1 == visited[cur - 1]):
            visited[cur - 1] = c + 1
            queue.append((cur - 1, c + 1))

        if cur * 2 <= 10 ** 5 and (not visited[cur * 2] or c + 1 == visited[cur * 2]):
            visited[cur * 2] = c + 1
            queue.append((cur * 2, c + 1))
    return m


n, k = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(10 ** 5 + 1)]
visited[n] += 1
ans = 0
MIN = bfs()
print(MIN)
print(ans)