import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):

    N, K = map(int, sys.stdin.readline().split())
    duration = list(map(int, sys.stdin.readline().split()))
    duration.insert(0, 0)

    graph = {i: [] for i in range(1, N + 1)}
    indegree = [0 for _ in range(N + 1)]
    time = [0 for _ in range(N + 1)]
    dq = deque()

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1

    for i in range(1, N + 1):
        if not indegree[i]:
            time[i] = duration[i]
            dq.append(i)

    W = int(sys.stdin.readline())

    while dq:
        t = dq.popleft()
        if t == W:
            break

        for node in graph[t]:
            indegree[node] -= 1
            time[node] = max(time[node], time[t] + duration[node])
            if not indegree[node]:
                dq.append(node)

    print(time[W])
