import sys, math
from itertools import combinations

sys.setrecursionlimit(10 ** 6)

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1 = find(u)
    r2 = find(v)
    p[r2] = r1


N = int(sys.stdin.readline())
star, graph = [], []
p = [i for i in range(N)]

for _ in range(N):
    x, y = map(float, sys.stdin.readline().split())
    star.append((x, y))

for cs in combinations(range(N), 2):
    s1n, s2n = cs[0], cs[1]
    dist = math.sqrt((star[s2n][0] - star[s1n][0]) ** 2 + (star[s2n][1] - star[s1n][1]) ** 2)
    graph.append((s1n, s2n, dist))
graph.sort(key = lambda k:k[2])

cost = 0
for a, b, w in graph:
    if find(a) != find(b):
        union(a, b)
        cost += w

print(f'{cost:.2f}')