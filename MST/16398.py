from itertools import combinations
import sys


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1, r2 = find(u), find(v)
    p[r2] = r1


N = int(sys.stdin.readline())
p = [i for i in range(N)]
graph, edges = [], []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for x, y in combinations(range(N), 2):
    edges.append((x, y, graph[x][y]))

edges.sort(key=lambda k:k[2])
s = 0

for x, y, w in edges:
    if find(x) != find(y):
        union(x, y)
        s += w
print(s)