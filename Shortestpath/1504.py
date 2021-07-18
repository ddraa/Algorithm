import sys, heapq


def dijkstra(start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = []  # heap
    heapq.heappush(queue, [distances[start], start])  # distance, vertex

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if distances[current_vertex] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distances[adjacent] > distance:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances


N, E = map(int, sys.stdin.readline().split())
graph = {i: {} for i in range(1, N + 1)}

for _ in range(E):
    v1, v2, w = map(int, sys.stdin.readline().split())
    if v2 in graph[v1]:
        graph[v1][v2] = min(graph[v1][v2], w)
    else:
        graph[v1][v2] = w

    if v1 in graph[v2]:
        graph[v2][v1] = min(graph[v2][v1], w)
    else:
        graph[v2][v1] = w

a, b = map(int, sys.stdin.readline().split())

madist = dijkstra(a)
mbdist = dijkstra(b)
ml = madist[b]

dist = dijkstra(1)
path1 = dist[a] + ml + mbdist[N]
path2 = dist[b] + ml + madist[N]

print(min(path1, path2)) if E != 0 else print(-1)
