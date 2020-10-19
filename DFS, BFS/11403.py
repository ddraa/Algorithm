from _collections import deque
import sys

N = int(input())
matrix = []
graph = {}
visited = {}
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    graph[i] = []
for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            graph[i].append(j)

def bfs(s):
    global visited
    visited = {}
    queue = deque([s])
    isFirst = True
    while queue:
        v = queue.popleft()
        if v not in visited:
            if isFirst:
                isFirst = False
                queue+=graph[v]
                continue
            visited[v] = True
            queue+=graph[v]

for i in range(N):
    bfs(i)
    for k in range(N):
        if k in visited:
            print(1, end=" ")
        else:
            print(0, end=' ')
    print("")