import sys, heapq
from collections import deque


# how to find all of the vertex in shortest path ..

def dijkstra(start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [distances[start], start])  # distance, vertex

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if distances[current_vertex] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if adjacent in distances and distances[adjacent] > distance:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances


def BFS(end):
    visited = [False for _ in range(N)]
    visited[end] = True
    queue = deque([end])

    while queue:
        u = queue.popleft()

        for vv in graph:
            for vertex, weight in graph[vv].items():
                if vertex == u and dist[u] == dist[vv] + weight and not visited[vv]:
                    visited[vv] = True
                    queue.append(vv)

    nodes = set()
    for i, val in enumerate(visited):
        if val:
            nodes.add(i)
    return nodes - set([s, e])


while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    graph = {}
    for v in range(N):
        graph[v] = {}

    s, e = map(int, sys.stdin.readline().split())
    for _ in range(M):  # make Bidirectional graph
        v1, v2, w = map(int, sys.stdin.readline().split())
        graph[v1][v2] = w

    dist = dijkstra(s)
    removed = BFS(e)
    for r in removed:
        del graph[r]

    dist = dijkstra(s)
    if dist[e] != float('inf'):
        print(dist[e])
    else:
        print(-1)
