import sys, heapq
from collections import deque

# how to find all of the vertex in shortest path ..

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


def BFS(end, p):

    visited = [False for _ in range(end + 1)]
    visited[end] = True
    queue = deque([end])
    s = set([end])

    while queue:
        u = queue.popleft()
        for v, weight in graph[u].items():
            if dist[u] == dist[v] + weight and not visited[v]:
                visited[v] = True
                s.add(v)
                queue.append(v)
    print(s)
    print("SAVE HIM") if p in s else print("GOOD BYE")



V, E, P = map(int, sys.stdin.readline().split())
graph = {}
save = False
for _ in range(E): # make Bidirectional graph
    v1, v2, w = map(int, sys.stdin.readline().split())

    if v1 not in graph:
        graph[v1] = {v2 : w}
    else:
        graph[v1][v2] = w
    if v2 not in graph:
        graph[v2] = {v1 : w}
    else:
        graph[v2][v1] = w

dist = dijkstra(1)
print(dist)
BFS(V, P)

