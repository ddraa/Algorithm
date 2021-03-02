import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append((n, 0))
    m, ans = 0, 0

    while queue:
        cur, c = queue.popleft()
        if cur == k:
            m = c
            ans += 1

        for Next in [cur + 1, cur - 1, cur * 2]:
            if 0 <= Next <= 10 ** 5 and (not visited[Next] or c + 1 == visited[Next]):
                visited[Next] = c + 1
                queue.append((Next, c + 1))
    return m, ans


n, k = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(10 ** 5 + 1)] # 최단거리 확인 + 방문 체크
visited[n] += 1
a, b = bfs()
print(a)
print(b)