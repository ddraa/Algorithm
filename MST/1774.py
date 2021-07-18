import sys
import math
from itertools import combinations

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1 = find(u)
    r2 = find(v)
    p[r2] = r1


N, M = map(int, sys.stdin.readline().split())
graph, edges = [], []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    graph.append((x, y))

p = [i for i in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    union(a - 1, b - 1)

for x, y in combinations(range(N), 2):
    edges.append((x, y, math.sqrt((graph[x][1] - graph[y][1]) ** 2 + (graph[x][0] - graph[y][0]) ** 2)))

edges.sort(key=lambda k:k[2])

s = 0
for x, y, w in edges:
    if find(x) != find(y):
        union(x, y)
        s += w

print(f'{s:.2f}')

