import sys, heapq
from collections import deque

# how to find all of the vertex in shortest path ..

def dijkstra(start):
    dist = {vertex : float('inf') for vertex in graph}
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [dist[start], start]) # distance, vertex

    while queue:
        cur_dist, cur_v = heapq.heappop(queue)
        if dist[cur_v] < cur_dist:
            continue

        for adj, weight in graph[cur_v].items():
            distance = cur_dist + weight
            if dist[adj] > distance:
                dist[adj] = distance
                heapq.heappush(queue, [distance, adj])
    return dist

def BFS(end):

    queue = deque([end])
    deleted = []
    while queue:
        to = queue.popleft()
        for pre, weight in rgraph[to].items():
            if dis[to] == dis[pre] + weight:
                if [pre, to] not in deleted:
                    deleted.append([pre, to])
                    queue.append(pre)

    for u, v in deleted:
        del graph[u][v]


while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    graph, rgraph = {}, {}

    for i in range(N):
        graph[i], rgraph[i] = {}, {}

    s, e = map(int, sys.stdin.readline().split())

    for _ in range(M): # make Bidirectional graph
        v1, v2, w = map(int, sys.stdin.readline().split())
        graph[v1][v2] = w
        rgraph[v2][v1] = w

    dis = dijkstra(s)
    BFS(e)
    dis = dijkstra(s)

    print(dis[e]) if dis[e] != float('inf') else print(-1)