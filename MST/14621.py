import sys

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1, r2 = find(u), find(v)
    p[r2] = r1


N, M = map(int, sys.stdin.readline().split())
graph, p = [], [i for i in range(N)]
mv = sys.stdin.readline().split()
for _ in range(M):
    x, y, w = map(int, sys.stdin.readline().split())
    graph.append((x - 1, y - 1, w))

graph.sort(key=lambda k:k[2])

d, e = 0, 0
for x, y, w in graph:
    if mv[x] != mv[y] and find(x) != find(y):
        union(x, y)
        d += w
        e += 1

        if e == N - 1:
            print(d)
            break
else:
    print(-1)

