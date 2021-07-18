import sys


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1 = find(u)
    r2 = find(v)
    p[r2] = r1


N, E = map(int, sys.stdin.readline().split())
p = [i for i in range(N + 1)]
graph = []

for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().split())
    graph.append([a, b, w])

graph.sort(key=lambda x: x[2], reverse=True)
cost, MAX = 0, 0
while graph:
    a, b, w = graph.pop()
    if find(a) != find(b):
        union(a, b)
        cost += w
        MAX = max(w, MAX)
print(cost - MAX)
