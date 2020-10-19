from _collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
graph = {}
visited = {}
count = 0
for i in range(1, N+1):
    graph[i] = []
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a]+= [b]
    graph[b]+= [a]

def bfs(s):
    queue = deque([s])
    while queue:
        l = queue.popleft()
        if l not in visited:
            visited[l] = True
            queue += graph[l]

for i in range(1,N+1):
    if i not in visited:
        bfs(i)
        count += 1
print(count)