import sys

input = sys.stdin.readline


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1, r2 = find(u), find(v)
    p[r2] = r1


N, M, K = map(int, input().split())
plant = list(map(int, input().split()))
graph, p = [], [i for i in range(N + 1)]
cost = 0

for _ in range(M):
    a, b, w = map(int, input().split())
    graph.append((a, b, w))

graph.sort(key=lambda x: x[2])

i = 0
while i + 1 < len(plant):
    union(plant[i], plant[i + 1])
    i += 1

for a, b, w in graph:
    if find(a) != find(b):
        union(a, b)
        cost += w
print(cost)