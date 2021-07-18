from heapq import *
import sys
input = sys.stdin.readline


def Dijkstra(s):
    dist[s] = 0
    h = []
    heappush(h, (0, s))

    while h:
        c_dist, c_node = heappop(h)
        if c_dist > dist[c_node]:
            continue

        for n_node, w in graph[c_node].items():
            n_dist = w + c_dist
            if dist[n_node] > n_dist:
                dist[n_node] = n_dist
                heappush(h, (dist[n_node], n_node))
                edges[n_node] = (c_node, n_node)


N, M = map(int, input().split())
graph = {i : {} for i in range(1, N + 1)}
dist = [float('inf') for i in range(N + 1)]
edges = {}
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c


Dijkstra(1)
print(len(edges))
for k in edges.values():
    print(*k)