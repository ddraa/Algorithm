import sys
from collections import deque

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

    # p[r2] = r1


N = int(sys.stdin.readline())
E = int(sys.stdin.readline())

#init
p = [i for i in range(N + 1)]
rank = [0 for i in range(N + 1)]
rank[0], cost, edges = -1, 0, 0
graph = []

for _ in range(E):
    graph.append(tuple(map(int, sys.stdin.readline().split())))
graph = deque(sorted(graph, key=lambda x:x[2]))
print(graph)
while True:
    if edges == N - 1:
        break
    a, b, w = graph.popleft()
    if find(a) != find(b):
        union(a, b)
        cost += w
        edges += 1
        print(p, a, b)
        print(rank)
print(cost)