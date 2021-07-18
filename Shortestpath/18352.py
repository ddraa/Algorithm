import sys
from heapq import *
input = sys.stdin.readline


def Dijkstra(S):
    dist[S] = 0
    h = []
    heappush(h, (dist[S], S))

    while h:
        c_dist, c_node = heappop(h)
        if c_dist > dist[c_node]:
            continue

        for n_node, w in graph[c_node].items():
            n_dist = c_dist + w
            if dist[n_node] > n_dist:
                dist[n_node] = n_dist
                heappush(h, (n_dist, n_node))


N, M, K, s = map(int, input().split())
graph = {i : {} for  i in range(1, N + 1)}
dist = [sys.maxint for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1


Dijkstra(s)
F = False
for i, n in enumerate(dist):
    if n == K:
        F = True
        print(i)
if not F:
    print(-1)