from _collections import deque

N, M = map(int, input().split())

visit = []
matrix = []
result = []
c = 0
opx = [-1,1,0,0]
opy = [0,0,-1,1]

for _ in range(N):
    matrix.append(list(map(int, list(input()))))
for _ in range(N):
    li = []
    for __ in range(M):
        li.append(0)
    visit.append(li)
visit[0][0] = 1
result = []
N-=1
M-=1 #set -> index

def bfs(x,y):
    global c
    queue = deque()
    queue.append([x,y,c])

    while queue:

        ax,ay,cnt = queue.popleft()
        cnt+=1
        #print(ax,ay)
        if ax== N and ay == M:
            result.append(cnt)
            return

        for k in range(4):
            xx = ax+ opx[k]
            yy = ay+ opy[k]
            if 0<=xx<=N and 0<=yy<=M and matrix[xx][yy]==1:
                if not visit[xx][yy]:
                    visit[xx][yy] = 1
                    queue.append([xx,yy,cnt])


bfs(0,0)
print(min(result))

