import sys, heapq

def dijkstra(start):
    distances = {vertex : float('inf') for vertex in graph}
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [distances[start], start]) # distance, vertex

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

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {}
for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    if a in graph:
        if b in graph[a]:
            graph[a][b] = min(graph[a][b], w) # 다중 간선 처리 (같은 출발, 목적지가 여러 간선을 가질 수 있음)
        else:
            graph[a][b] = w
    else:
        graph[a] = {b : w}
    if b not in graph:
        graph[b] = {}

s, e = map(int, sys.stdin.readline().split())
dist = dijkstra(s)
print(dist[e])