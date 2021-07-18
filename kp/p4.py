from heapq import *

def solution(ages, wires):
    answer, h = [], []
    graph = [{} for _ in range(len(ages) + 1)]
    N = len(ages) + 1
    for i, age in enumerate(ages):
        heappush(h, (age, i + 1))

    for a, b, w in wires:
        graph[a][b] = w

    visited = [[False for _ in range(N)] for _ in range(N)]

    dist = [0]
    for a in ages:
        dist.append(a)

    while h:
        _, c_node = heappop(h)
        for n_node, w in graph[c_node].items():
            if not visited[c_node][n_node]:
                visited[c_node][n_node] = True
                n_w = dist[c_node] + w

                if n_w < dist[n_node]:
                    dist[n_node] = n_w
                    heappush(h, (dist[n_node], n_node))
                    
    for i, v in enumerate(dist):
        if i != 0:
            heappush(h, (v, i))
    while h:
        answer.append(heappop(h)[1])
    return answer

print(solution([35, 25, 3, 8, 7], [[1,2,5],[2,1,5],[1,3,2],[3,4,2],[3,5,20],[4,5,1]]))