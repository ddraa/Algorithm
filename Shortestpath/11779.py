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
                before[adjacent] = current_vertex # point

    node = e
    while node != s:
        res.append(before[node])
        node = before[node]
    return distances


V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
graph = {i: {} for i in range(1, V + 1)}
before = [-1 for _ in range(V + 1)]

for _ in range(E):
    v1, v2, w = map(int, sys.stdin.readline().split())
    if v2 in graph[v1]:
        graph[v1][v2] = min(graph[v1][v2], w)
    else:
        graph[v1][v2] = w

s, e = map(int, sys.stdin.readline().split())
res = [e]

dist = dijkstra(s)

print(dist[e])
print(len(res))
print(*reversed(res))
