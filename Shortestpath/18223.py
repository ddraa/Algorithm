import sys, heapq

def dijkstra(start, end):
    distances = {vertex : float('inf') for vertex in graph}
    path = {vertex : -1 for vertex in graph}
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
                path[adjacent] = set([current_vertex]) # path init
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
            elif distances[adjacent] == distance:
                if current_vertex not in path[adjacent]:
                    path[adjacent].add(current_vertex) # path update
                    heapq.heappush(queue, [distance, adjacent])
    print(distances)
    return path


def search(n):
    global save
    if n == P:
        save = True
        return
    elif n == 1:
        return
    for i in res[n]:
        search(i)


V, E, P = map(int, sys.stdin.readline().split())
graph = {}
save = False
for _ in range(E): # make graph
    v1, v2, w = map(int, sys.stdin.readline().split())
    if v1 not in graph:
        graph[v1] = {v2 : w}
    else:
        graph[v1][v2] = w
    if v2 not in graph:
        graph[v2] = {v1 : w}
    else:
        graph[v2][v1] = w

res = dijkstra(1, V)
search(V)
print("SAVE HIM") if save else print("GOOD BYE")
