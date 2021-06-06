import sys
input = sys.stdin.readline


def BellmanFord(start):
    dist[start] = 0
    for _ in range(N - 1):
        for u, v, weight in edges:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight


def n_cycle():
    for u, v, weight in edges:
        if dist[v] > dist[u] + weight:
            return True
    return False


N, M = map(int, input().split())
edges = []
dist = [float('inf') for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    edges.append((a, b, w))

BellmanFord(1)
if n_cycle():
    print(-1)
else:
    for i in range(2, N + 1):
        print(dist[i]) if dist[i] != float('inf') else print(-1)
