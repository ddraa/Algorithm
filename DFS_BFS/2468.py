from _collections import deque
import sys

opx = [1,-1,0,0]
opy = [0,0,-1,1]
N = int(sys.stdin.readline())
town = []
T = 0
MAX = 1
for _ in range(N):
    town.append(list(map(int, sys.stdin.readline().split())))

for i in town:
    t = max(i)
    if T < t:
        T = t

def bfs(x, y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 1

    while queue:
        ax, ay = queue.popleft()

        for k in range(4):
            x = ax + opx[k]
            y = ay + opy[k]
            if 0<=x<=N-1 and 0<=y<=N-1:
                if not visited[x][y] and downtown[x][y]>0:
                    visited[x][y] = 1 # caution ! at the same time with append.
                    queue.append([x,y])


for water in range(1, T):
    downtown = []
    count = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        l = []
        for j in range(N):
            l.append(town[i][j]-water)
        downtown.append(l)
    for i in range(N):
        for j in range(N):
            if downtown[i][j]>0 and not visited[i][j]:
                count += 1
                bfs(i,j)
    if count > MAX:
        MAX = count
print(MAX)