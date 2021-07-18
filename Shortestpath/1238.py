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


N, M, X = map(int, sys.stdin.readline().split())
graph = {i: {} for i in range(1, N + 1)}

for _ in range(M):
    v1, v2, w = map(int, sys.stdin.readline().split())
    # if v2 in graph[v1]:
    #     graph[v1][v2] = min(graph[v1][v2], w) 중복 간선 체크
    # else:
    graph[v1][v2] = w

MAX = 0
for stu in graph:
    MAX = max(dijkstra(stu)[X] + dijkstra(X)[stu], MAX)
print(MAX)
