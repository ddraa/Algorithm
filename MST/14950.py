import sys
input = sys.stdin.readline

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1, r2 = find(u), find(v)
    p[r2] = r1


N, M, t = map(int, input().split())
p = [i for i in range(N)]
graph = []

for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a - 1, b - 1, c))

graph.sort(key=lambda x:x[2])

cost, ad = 0, 0

for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        cost += c + ad
        ad += t

print(cost)