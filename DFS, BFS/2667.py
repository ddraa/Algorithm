from _collections import deque

N = int(input())
matrix = []
visit = []
length = []
for _ in range(N):
    matrix.append(list(map(int, list(input()))))
for _ in range(N):
    li = []
    for __ in range(N):
        li.append(0)
    visit.append(li)
opx = [-1,1,0,0]
opy = [0,0,-1,1]

def bfs(x, y):
    global c
    queue = deque()
    queue.append([x,y])
    visit[x][y] = 1
    while queue:
        ax, ay = queue.popleft()
        #print(ax,ay)
        c+=1
        for k in range(4):
            xx = ax + opx[k]
            yy = ay + opy[k]
            if 0<=xx<=N-1 and 0<=yy<=N-1:
                if visit[xx][yy]==0 and matrix[xx][yy] == 1: # not visited
                    visit[xx][yy] = 1
                    queue.append([xx,yy])



for i in range(N):
    for j in range(N):
        if not visit[i][j] and matrix[i][j]:
            c = 0
            #print(f'i j = {i},{j}')
            bfs(i,j)
            length.append(c)

print(len(length))
length.sort()
for i in length:
    print(i)