from _collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
MAX = 100000 #limit
def bfs(N):
    queue = deque()
    queue.append([N,0])
    visited = {}

    while queue:
        s, c = queue.popleft()
        if s not in visited:
            visited[s] = True
            if s == K:
                return c
            c+=1
            if s+1 <= MAX:
                queue.append([s+1,c])
            if 0 <= s-1:
                queue.append([s-1,c])
            if s*2<= MAX:
                queue.append([s*2,c])
print(bfs(N))
