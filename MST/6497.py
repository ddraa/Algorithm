import sys
from collections import deque
sys.setrecursionlimit(10**8)


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1 = find(u)
    r2 = find(v)

    if rank[r1] > rank[r2]:
        p[r2] = r1
    else:
        p[r1] = r2
        if rank[r1] == rank[r2]:
            rank[r2] += 1

while True:
    N, E = map(int, sys.stdin.readline().split())
    if N == 0 and E == 0:
        break
    p = [i for i in range(N)]
    rank = [0 for i in range(N)]
    # p = {i : i for i in range(N)}
    # rank = {i : 0 for i in range(N)}

    cost, edges, s = 0, 0, 0
    graph = []
    for _ in range(E):
        graph.append(tuple(map(int, sys.stdin.readline().split())))
    graph = deque(sorted(graph, key=lambda x:x[2]))
    for g in graph:
        s += g[2]

    while True:
        if edges == N - 1:
            break

        a, b, w = graph.popleft()
        if find(a) != find(b):
            union(a, b)
            edges += 1
            cost += w
    print(s - cost)