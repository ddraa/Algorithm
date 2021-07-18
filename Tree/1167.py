import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node):
    global farthest_node
    for adj in graph[node]:
        if not visited[adj]:
            visited[adj] = True
            dist[adj] = dist[node] + graph[node][adj]

            if dist[adj] > dist[farthest_node]: # check
                farthest_node = adj
            dfs(adj)


N = int(sys.stdin.readline())
graph = {i: {} for i in range(1, N + 1)}
root = 1 # anything
farthest_node = root

for _ in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    node = l[0]
    for i in range(2, len(l) - 1, 2):
        graph[node][l[i - 1]] = l[i]
        graph[l[i - 1]][node] = l[i]

dist = [0 for _ in range(N + 1)]
dist[root] = 0  # init
visited = [False for _ in range(N + 1)]
visited[root] = True
dfs(root)

dist = [0 for _ in range(N + 1)]
dist[farthest_node] = 0  # init
visited = [False for _ in range(N + 1)]
visited[farthest_node] = True
dfs(farthest_node)
print(max(dist))
