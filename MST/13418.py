import sys
input = sys.stdin.readline


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1, r2 = find(u), find(v)
    p[r2] = r1


N, M = map(int, input().split())
p, graph = [i for i in range(N + 1)], []

for _ in range(M + 1):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

graph.sort(key=lambda x: -x[2])
MIN = 0
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        if c == 0:
            MIN += 1

graph.sort(key=lambda x: x[2])
p = [i for i in range(N + 1)]
MAX = 0
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        if c == 0:
            MAX += 1
print(MAX ** 2 - MIN ** 2)
