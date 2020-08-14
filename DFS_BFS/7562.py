opx = [-2,-1,1,2,2,1,-1,-2]
opy = [1,2,2,1,-1,-2,-2,-1]

from _collections import deque
import sys

def bfs(c):
    global x, y, visited
    queue = deque()
    queue.append([x,y,c])

    while queue:
        a, b, c = queue.popleft()
        if not visited[a][b]:
            visited[a][b] = 1
            c += 1
            for k in range(8):
                ax = a+opx[k]
                ay = b+opy[k]
                if ax==tox and ay==toy:
                    return c
                if 0<=ax<=l-1 and 0<=ay<=l-1:
                    queue.append([ax,ay,c])


T = int(input())
for _ in range(T):
    l = int(input())
    x, y = map(int, input().split())
    tox, toy = map(int, input().split())
    if x==tox and y==toy:
        print(0)
        continue
    visited = [[0]*l for _ in range(l)]
    print(bfs(0))