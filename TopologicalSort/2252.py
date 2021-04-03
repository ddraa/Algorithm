import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = {i : [] for i in range(1, N + 1)}
indegree = [0 for _ in range(N + 1)]
dq = deque()
res = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, N + 1):
    if not indegree[i]:
        dq.append(i)

while dq:
    t = dq.popleft()
    res.append(t)

    for node in graph[t]:
        indegree[node] -= 1
        if not indegree[node]:
            dq.append(node)
print(*res)