from heapq import *
import sys
input = sys.stdin.readline
INF = 1e6

def dijkstra(s):
    h = [(0, s)]
    while h:
        c_dist, c_node = heappop(h)
        if c_dist > dist[c_node]:
            continue
        for n_node, w in graph[c_node]:
            n_dist = c_dist + w
            if dist[n_node] > n_dist:
                dist[n_node] = n_dist
                heappush(h, (n_dist, n_node))


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    res = [0] * (N + 1)

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    K = int(input())
    pos = list(map(int, input().split()))
    v = 0

    for p in pos:
        dist = [INF] * (N + 1)
        dist[p] = 0
        dijkstra(p)
        mv = INF
        for i in range(N + 1):
            res[i] += dist[i]
            if mv > res[i]:
                mv = res[i]
                v = i

    print(v)