from heapq import *
import sys

input = sys.stdin.readline


def Dijkstra(start):
    h = []
    heappush(h, (dist[start], start))
    while h:
        c_dist, c_node = heappop(h)
        if c_dist > dist[c_node]:
            continue

        for n_node, w in graph[c_node].items():
            n_dist = c_dist + w
            if n_node in edges[c_node] and edges[c_node][n_node][0] <= c_dist <= edges[c_node][n_node][1]:
                wait = edges[c_node][n_node][1] - c_dist + 1
                n_dist += wait

            if dist[n_node] > n_dist:
                dist[n_node] = n_dist
                heappush(h, (n_dist, n_node))


N, M = map(int, input().split())
s, e, K, G = map(int, input().split())
g = list(map(int, input().split()))
graph = {i: {} for i in range(1, N + 1)}
edges = {i: {} for i in range(1, N + 1)}
dist = [float('inf') for _ in range(N + 1)]
dist[s] = K

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b], graph[b][a] = c, c

i, t = 0, 0

while i + 1 < len(g):
    a, b = g[i], g[i + 1]
    st, et = t, t + graph[a][b] - 1
    edges[a][b], edges[b][a] = (st, et), (st, et)
    t = et + 1
    i += 1

Dijkstra(s)
print(dist[e] - K)
