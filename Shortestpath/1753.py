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

v, e = map(int, sys.stdin.readline().split())
s = int(sys.stdin.readline())

graph = {}
for g in range(1, v + 1):
    graph[g] = {} # init

for _ in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], w) # 다중 간선 처리 (같은 출발, 목적지가 여러 간선을 가질 수 있음)
    else:
        graph[a][b] = w

dist = dijkstra(s)
for i in range(1, v + 1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])