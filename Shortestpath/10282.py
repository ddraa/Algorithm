from heapq import *
import sys

input = sys.stdin.readline


def Dijkstra(s):
    h = []
    heappush(h, (0, s))
    dist[s] = 0

    while h:
        c_dist, c_node = heappop(h)
        if dist[c_node] < c_dist:
            continue

        for n_node, weight in graph[c_node].items():
            n_dist = c_dist + weight
            if dist[n_node] > n_dist:
                dist[n_node] = n_dist
                heappush(h, (n_dist, n_node))


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = {i: {} for i in range(1, n + 1)}
    dist = [float('inf') for _ in range(n + 1)]

    for _ in range(d):
        a, b, w = map(int, input().split())
        graph[b][a] = w

    Dijkstra(c)
    count = 0
    M = 0
    for d in dist:
        if d != float('inf'):
            count += 1
            if d > M:
                M = d
    print(count, M)
