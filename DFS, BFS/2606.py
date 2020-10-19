N = int(input())
edges = int(input())
graph = {}
visited = [1]
sck = []
for i in range(1, N+1):
    graph[i] = list()
count = 0


def dfs(s):
    global count
    for adjNode in graph[s]:
        if adjNode not in visited:
            visited.append(adjNode)
            dfs(adjNode)

for  _ in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(len(visited)-1)